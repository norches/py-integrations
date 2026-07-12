from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional

from core.logger import setup_logger
from core.mariadb import mariadb_ops


logger = setup_logger("chatgpt_regos_assistant.billing")

_SCHEMA_LOCK = asyncio.Lock()
_SCHEMA_READY = False
_MIGRATIONS_DIR = Path(__file__).with_name("migrations")
_TARIFF_TABLE = mariadb_ops.table_name("chatgpt", "regos", "assistant", "tariff")
_DAILY_TABLE = mariadb_ops.table_name("chatgpt", "regos", "assistant", "usage", "daily")
_LOG_TABLE = mariadb_ops.table_name("chatgpt", "regos", "assistant", "usage", "log")


class BillingUnavailableError(RuntimeError):
    pass


@dataclass(frozen=True)
class ChatBillingTariff:
    code: str
    free_requests_per_day: int
    billable_request_price: str
    currency: str


@dataclass(frozen=True)
class ChatUsageReservation:
    request_log_id: int
    usage_date: str
    api_login: str
    connected_integration_id: str
    tariff_code: str
    request_number: int
    free_limit: int
    billable: bool
    billable_request_price: str
    currency: str
    free_remaining: int


def _text(value: Any, default: str = "") -> str:
    text = str(value or "").strip()
    return text if text else default


def _int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _sql_statements(sql: str) -> List[str]:
    statements: List[str] = []
    current: List[str] = []
    quote = ""
    escaped = False

    for char in sql:
        current.append(char)
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = ""
            continue
        if char in {"'", '"'}:
            quote = char
            continue
        if char == ";":
            statement = "".join(current).strip().rstrip(";").strip()
            if statement:
                statements.append(statement)
            current = []

    tail = "".join(current).strip()
    if tail:
        statements.append(tail)
    return statements


async def ensure_schema(*, force: bool = False) -> bool:
    global _SCHEMA_READY
    if _SCHEMA_READY and not force:
        return True

    async with _SCHEMA_LOCK:
        if _SCHEMA_READY and not force:
            return True
        try:
            for migration_path in sorted(_MIGRATIONS_DIR.glob("*.sql")):
                sql = migration_path.read_text(encoding="utf-8").strip()
                if not sql:
                    continue
                for statement in _sql_statements(sql):
                    await mariadb_ops.execute(statement)
                logger.info(
                    "Applied ChatGPT REGOS Assistant MariaDB migration: %s",
                    migration_path.name,
                )
        except Exception as exc:
            raise BillingUnavailableError("REGOS Assistant billing database is unavailable") from exc
        _SCHEMA_READY = True
        return True


async def _fetch_active_tariff(cursor: Any) -> ChatBillingTariff:
    await cursor.execute(
        f"""
        SELECT `code`, `free_requests_per_day`, `billable_request_price`, `currency`
        FROM {_TARIFF_TABLE}
        WHERE `is_active` = 1
        ORDER BY `is_default` DESC, `code` ASC
        LIMIT 1
        """
    )
    row = await cursor.fetchone()
    if not row:
        raise BillingUnavailableError("REGOS Assistant billing tariff is not configured")
    return ChatBillingTariff(
        code=_text(row[0], "default"),
        free_requests_per_day=max(_int(row[1]), 0),
        billable_request_price=str(row[2] or "0"),
        currency=_text(row[3], "UZS").upper()[:3],
    )


async def reserve_chat_request(
    *,
    connected_integration_id: str,
    api_login: str,
    model: str,
) -> ChatUsageReservation:
    ci = _text(connected_integration_id)
    normalized_api_login = _text(api_login)
    if not ci or not normalized_api_login:
        raise BillingUnavailableError("connected_integration_id and api_login are required")

    await ensure_schema()
    usage_date = date.today().isoformat()

    try:
        async with mariadb_ops.transaction() as connection:
            async with connection.cursor() as cursor:
                tariff = await _fetch_active_tariff(cursor)
                normalized_free_limit = tariff.free_requests_per_day
                await cursor.execute(
                    f"""
                    SELECT `request_count`
                    FROM {_DAILY_TABLE}
                    WHERE `usage_date` = %s AND `api_login` = %s
                    FOR UPDATE
                    """,
                    (usage_date, normalized_api_login),
                )
                row = await cursor.fetchone()
                request_count = _int(row[0]) if row else 0
                request_number = request_count + 1
                billable = request_number > normalized_free_limit
                free_remaining = max(normalized_free_limit - request_number, 0)

                if row:
                    await cursor.execute(
                        f"""
                        UPDATE {_DAILY_TABLE}
                        SET `connected_integration_id` = %s,
                            `tariff_code` = %s,
                            `free_limit` = %s,
                            `request_count` = `request_count` + 1,
                            `updated_at` = CURRENT_TIMESTAMP
                        WHERE `usage_date` = %s AND `api_login` = %s
                        """,
                        (
                            ci,
                            tariff.code,
                            normalized_free_limit,
                            usage_date,
                            normalized_api_login,
                        ),
                    )
                else:
                    await cursor.execute(
                        f"""
                        INSERT INTO {_DAILY_TABLE}
                            (`usage_date`, `api_login`, `connected_integration_id`,
                             `tariff_code`, `free_limit`, `request_count`)
                        VALUES (%s, %s, %s, %s, %s, 1)
                        """,
                        (
                            usage_date,
                            normalized_api_login,
                            ci,
                            tariff.code,
                            normalized_free_limit,
                        ),
                    )

                await cursor.execute(
                    f"""
                    INSERT INTO {_LOG_TABLE}
                        (`usage_date`, `api_login`, `connected_integration_id`, `tariff_code`,
                         `model`, `status`, `request_number`, `free_limit`, `billable`,
                         `billable_request_price`, `currency`)
                    VALUES (%s, %s, %s, %s, %s, 'reserved', %s, %s, %s, %s, %s)
                    """,
                    (
                        usage_date,
                        normalized_api_login,
                        ci,
                        tariff.code,
                        _text(model),
                        request_number,
                        normalized_free_limit,
                        1 if billable else 0,
                        tariff.billable_request_price,
                        tariff.currency,
                    ),
                )
                request_log_id = int(getattr(cursor, "lastrowid", None) or 0)
    except BillingUnavailableError:
        raise
    except Exception as exc:
        raise BillingUnavailableError("Failed to reserve REGOS Assistant request") from exc

    if request_log_id <= 0:
        raise BillingUnavailableError("Failed to reserve REGOS Assistant request")

    return ChatUsageReservation(
        request_log_id=request_log_id,
        usage_date=usage_date,
        api_login=normalized_api_login,
        connected_integration_id=ci,
        tariff_code=tariff.code,
        request_number=request_number,
        free_limit=normalized_free_limit,
        billable=billable,
        billable_request_price=tariff.billable_request_price,
        currency=tariff.currency,
        free_remaining=free_remaining,
    )


async def complete_chat_request(
    reservation: Optional[ChatUsageReservation],
    *,
    status: str,
    response_id: str = "",
    usage: Optional[Dict[str, Any]] = None,
    tool_call_count: int = 0,
    error_code: str = "",
    error_description: str = "",
) -> None:
    if not reservation:
        return

    usage = usage if isinstance(usage, dict) else {}
    input_tokens = _int(usage.get("input_tokens"))
    output_tokens = _int(usage.get("output_tokens"))
    total_tokens = _int(usage.get("total_tokens"), input_tokens + output_tokens)
    safe_status = _text(status, "completed")[:64]
    safe_response_id = _text(response_id)[:128]
    safe_error_code = _text(error_code)[:128]
    safe_error_description = _text(error_description)[:512]
    billable_statuses = {"answered", "requires_confirmation", "tool_round_limit_reached"}
    count_for_billing = safe_status in billable_statuses
    free_delta = 1 if count_for_billing and not reservation.billable else 0
    billable_delta = 1 if count_for_billing and reservation.billable else 0

    try:
        async with mariadb_ops.transaction() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(
                    f"""
                    UPDATE {_DAILY_TABLE}
                    SET `input_tokens` = `input_tokens` + %s,
                        `output_tokens` = `output_tokens` + %s,
                        `total_tokens` = `total_tokens` + %s,
                        `free_request_count` = `free_request_count` + %s,
                        `billable_request_count` = `billable_request_count` + %s,
                        `updated_at` = CURRENT_TIMESTAMP
                    WHERE `usage_date` = %s AND `api_login` = %s
                    """,
                    (
                        input_tokens,
                        output_tokens,
                        total_tokens,
                        free_delta,
                        billable_delta,
                        reservation.usage_date,
                        reservation.api_login,
                    ),
                )
                await cursor.execute(
                    f"""
                    UPDATE {_LOG_TABLE}
                    SET `status` = %s,
                        `response_id` = %s,
                        `input_tokens` = %s,
                        `output_tokens` = %s,
                        `total_tokens` = %s,
                        `tool_call_count` = %s,
                        `error_code` = %s,
                        `error_description` = %s,
                        `completed_at` = CURRENT_TIMESTAMP
                    WHERE `id` = %s
                    """,
                    (
                        safe_status,
                        safe_response_id,
                        input_tokens,
                        output_tokens,
                        total_tokens,
                        max(int(tool_call_count or 0), 0),
                        safe_error_code,
                        safe_error_description,
                        reservation.request_log_id,
                    ),
                )
    except Exception:
        logger.exception(
            "Failed to complete ChatGPT REGOS billing record: log_id=%s",
            reservation.request_log_id,
        )


__all__ = [
    "BillingUnavailableError",
    "ChatUsageReservation",
    "complete_chat_request",
    "ensure_schema",
    "reserve_chat_request",
]

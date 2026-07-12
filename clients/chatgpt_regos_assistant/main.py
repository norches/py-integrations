from __future__ import annotations

import json
import secrets
import time
from typing import Any, Dict, List, Optional

import httpx
from starlette.responses import HTMLResponse, JSONResponse

from clients.base import ClientBase
from config.settings import settings as app_settings
from core.api.regos_api import RegosAPI
from core.logger import setup_logger

from .config import ChatGptRegosAssistantConfig
from .embed_auth import (
    access_token_from_session,
    build_embed_session,
    exchange_embed_token,
    expected_origin,
    oauth_client_id,
    public_embed_session,
    session_ttl_from_oauth_payload,
)
from .models import (
    RegosTool,
    RuntimeConfig,
    json_dumps,
    jsonable,
    parse_bool,
    parse_float,
    parse_int,
)
from .openai_responses import (
    build_openai_input,
    extract_openai_text,
    extract_openai_tool_calls,
    post_openai_response,
)
from .redis_state import ChatGptRegosAssistantRedisState
from .tools import REGOS_TOOLS
from .ui import (
    ChatGptRegosAssistantUiContext,
    render_chatgpt_regos_assistant_ui,
)

logger = setup_logger("chatgpt_regos_assistant")

# Backward-compatible alias for quick local checks and older imports.
_TOOLS = REGOS_TOOLS


class ChatGptRegosAssistantIntegration(ClientBase):
    def __init__(self) -> None:
        self.connected_integration_id: Optional[str] = None

    @staticmethod
    def _external_base_url(connected_integration_id: str) -> str:
        # The iframe UI and Embed OAuth callback must stay on the REGOS-facing
        # integration origin. proxy_integration_url is used by webhook-style
        # integrations and can point to another host.
        base_url = (
            str(app_settings.integration_url or "").strip()
            or str(app_settings.proxy_integration_url or "").strip()
        )
        return f"{base_url.rstrip('/')}/external/{connected_integration_id}/"

    def _ci(self) -> str:
        return str(self.connected_integration_id or "").strip()

    @staticmethod
    def _mapping_value(mapping: Dict[str, Any], key: str) -> Any:
        target = key.lower()
        for raw_key, value in mapping.items():
            if str(raw_key or "").lower() == target:
                return value
        return None

    @classmethod
    def _query_value(cls, envelope: Dict[str, Any], key: str) -> str:
        query = envelope.get("query") if isinstance(envelope.get("query"), dict) else {}
        value = cls._mapping_value(query, key)
        if isinstance(value, list):
            value = value[0] if value else None
        return str(value or "").strip()

    @staticmethod
    def _normalize_arguments(arguments: Any, extra: Dict[str, Any]) -> Dict[str, Any]:
        if arguments is None:
            payload = dict(extra)
        elif isinstance(arguments, str):
            try:
                parsed = json.loads(arguments)
            except json.JSONDecodeError:
                parsed = {"value": arguments}
            payload = parsed if isinstance(parsed, dict) else {"value": parsed}
            payload.update(extra)
        elif isinstance(arguments, dict):
            payload = dict(arguments)
            payload.update(extra)
        else:
            payload = {"value": arguments}
            payload.update(extra)

        for key in ("tool_name", "name", "confirmation_id", "approved"):
            payload.pop(key, None)
        return payload

    @staticmethod
    def _session_token_hash(session_token: str) -> str:
        import hashlib

        return hashlib.sha256(str(session_token or "").encode("utf-8")).hexdigest()

    @staticmethod
    def _action_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
        data = payload.get("data")
        return data if isinstance(data, dict) else payload

    @staticmethod
    def _payload_text(payload: Dict[str, Any], *keys: str) -> str:
        lower_map = {str(key).lower(): value for key, value in payload.items()}
        for key in keys:
            value = lower_map.get(str(key).lower())
            if value is not None:
                return str(value or "").strip()
        return ""

    @staticmethod
    def _error_payload(error: str, description: str) -> Dict[str, Any]:
        return {
            "ok": False,
            "status": "error",
            "error": error,
            "description": description,
        }

    @classmethod
    async def _fetch_settings_map(
        cls, connected_integration_id: str, *, force_refresh: bool = False
    ) -> Dict[str, str]:
        cache_key = ChatGptRegosAssistantRedisState.settings_cache_key(
            connected_integration_id
        )
        if not force_refresh:
            cached = await ChatGptRegosAssistantRedisState.get(cache_key)
            if cached:
                try:
                    payload = json.loads(cached)
                    if isinstance(payload, dict):
                        return {
                            str(key).lower(): str(value or "")
                            for key, value in payload.items()
                        }
                except Exception:
                    logger.debug(
                        "Failed to parse ChatGPT assistant settings cache",
                        exc_info=True,
                    )

        async with RegosAPI(connected_integration_id=connected_integration_id) as api:
            response = await api.integrations.connected_integration_setting.get(
                {"connected_integration_id": connected_integration_id}
            )

        settings_map: Dict[str, str] = {}
        for row in getattr(response, "result", None) or []:
            key = str(getattr(row, "key", "") or "").strip().lower()
            if key:
                settings_map[key] = str(getattr(row, "value", "") or "").strip()

        await ChatGptRegosAssistantRedisState.set(
            cache_key,
            json_dumps(settings_map),
            ChatGptRegosAssistantConfig.SETTINGS_TTL_SEC,
        )
        return settings_map

    @classmethod
    def _build_runtime(cls, settings_map: Dict[str, str]) -> RuntimeConfig:
        api_key = (
            settings_map.get("chatgpt_openai_api_key")
            or settings_map.get("openai_api_key")
            or settings_map.get("assistant_api_key")
            or ""
        ).strip()
        model = (
            settings_map.get("chatgpt_openai_model")
            or settings_map.get("openai_model")
            or ChatGptRegosAssistantConfig.DEFAULT_OPENAI_MODEL
        ).strip()
        prompt = (
            settings_map.get("chatgpt_assistant_prompt")
            or settings_map.get("assistant_prompt")
            or ChatGptRegosAssistantConfig.DEFAULT_PROMPT
        ).strip()
        return RuntimeConfig(
            openai_api_key=api_key,
            openai_model=model,
            assistant_prompt=prompt,
            temperature=parse_float(
                settings_map.get("chatgpt_temperature"),
                ChatGptRegosAssistantConfig.DEFAULT_TEMPERATURE,
                minimum=0.0,
                maximum=2.0,
            ),
            max_tool_rounds=parse_int(
                settings_map.get("chatgpt_max_tool_rounds"),
                ChatGptRegosAssistantConfig.DEFAULT_MAX_TOOL_ROUNDS,
                minimum=1,
                maximum=10,
            ),
            max_output_tokens=parse_int(
                settings_map.get("chatgpt_max_output_tokens"),
                ChatGptRegosAssistantConfig.DEFAULT_MAX_OUTPUT_TOKENS,
                minimum=256,
                maximum=8000,
            ),
            confirmation_ttl_sec=parse_int(
                settings_map.get("chatgpt_confirmation_ttl_sec"),
                ChatGptRegosAssistantConfig.DEFAULT_CONFIRMATION_TTL_SEC,
                minimum=60,
                maximum=3600,
            ),
        )

    async def _load_runtime(self, connected_integration_id: str) -> RuntimeConfig:
        settings_map = await self._fetch_settings_map(connected_integration_id)
        return self._build_runtime(settings_map)

    @classmethod
    async def _clear_settings_cache(cls, connected_integration_id: str) -> None:
        await ChatGptRegosAssistantRedisState.delete(
            ChatGptRegosAssistantRedisState.settings_cache_key(connected_integration_id)
        )

    async def connect(self, **_: Any) -> Dict[str, Any]:
        ci = self._ci()
        if not ci:
            return {"status": "error", "error": "connected_integration_id is required"}
        settings_map = await self._fetch_settings_map(ci, force_refresh=True)
        runtime = self._build_runtime(settings_map)
        return {
            "status": "connected",
            "integration_key": ChatGptRegosAssistantConfig.INTEGRATION_KEY,
            "external_url": self._external_base_url(ci),
            "ui_url": f"{self._external_base_url(ci)}ui",
            "embed_backend_url": f"{self._external_base_url(ci)}embed/consume",
            "embed_sdk_url": ChatGptRegosAssistantConfig.EMBED_SDK_URL,
            "openai_api_chat_enabled": bool(runtime.openai_api_key),
            "model": runtime.openai_model,
            "tools_count": len(REGOS_TOOLS),
            "confirmation_required_for_mutations": True,
            "confirmation_ttl_sec": runtime.confirmation_ttl_sec,
            "embed_auth_enabled": bool(oauth_client_id()),
        }

    async def disconnect(self, **_: Any) -> Dict[str, Any]:
        ci = self._ci()
        if ci:
            await self._clear_settings_cache(ci)
        return {"status": "disconnected"}

    async def reconnect(self, **_: Any) -> Dict[str, Any]:
        await self.disconnect()
        return await self.connect()

    async def update_settings(
        self, settings: Optional[dict] = None, **_: Any
    ) -> Dict[str, Any]:
        _ = settings
        ci = self._ci()
        if ci:
            await self._clear_settings_cache(ci)
        return {"status": "settings updated"}

    async def handle_webhook(
        self, data: Optional[dict] = None, **_: Any
    ) -> Dict[str, Any]:
        return {
            "status": "ignored",
            "reason": "webhooks_are_not_used",
            "data": data or {},
        }

    async def metadata(self, **_: Any) -> Dict[str, Any]:
        ci = self._ci()
        return {
            "integration_key": ChatGptRegosAssistantConfig.INTEGRATION_KEY,
            "name": "REGOS ChatGPT Assistant",
            "external_url": self._external_base_url(ci) if ci else None,
            "ui_url": f"{self._external_base_url(ci)}ui" if ci else None,
            "actions": [
                "list_tools",
                "execute_tool",
                "confirm_action",
                "chat",
                "embed_login",
                "consume_embed_token",
            ],
            "embed_backend_url": f"{self._external_base_url(ci)}embed/consume" if ci else None,
            "embed_sdk_url": ChatGptRegosAssistantConfig.EMBED_SDK_URL,
            "confirmation_required_for_mutations": True,
        }

    async def consume_embed_token(
        self,
        embed_token: Optional[str] = None,
        embedToken: Optional[str] = None,
        connected_integration_id: Optional[str] = None,
        connectedIntegrationId: Optional[str] = None,
        nonce: Optional[str] = None,
        origin: Optional[str] = None,
        **_: Any,
    ) -> Dict[str, Any]:
        ci = self._ci()
        provided_ci = str(
            connected_integration_id or connectedIntegrationId or ""
        ).strip()
        if not ci and provided_ci:
            self.connected_integration_id = provided_ci
            ci = provided_ci
        if not ci:
            return self._error_payload(
                "missing_connected_integration_id",
                "connected_integration_id is required",
            )
        if provided_ci and provided_ci != ci:
            return self._error_payload(
                "connected_integration_id_mismatch",
                "embed token was issued for another connected integration",
            )

        iframe_origin = str(origin or "").strip()
        expected_iframe_origin = expected_origin(self._external_base_url(ci))
        if iframe_origin and expected_iframe_origin and iframe_origin != expected_iframe_origin:
            return self._error_payload(
                "origin_mismatch",
                "embed token origin does not match this integration URL",
            )

        try:
            oauth_payload = await exchange_embed_token(embed_token or embedToken or "")
        except httpx.HTTPStatusError as exc:
            logger.warning(
                "REGOS embed token exchange failed: ci=%s status=%s",
                ci,
                exc.response.status_code if exc.response else None,
            )
            return self._error_payload(
                "embed_token_exchange_failed",
                "REGOS OAuth rejected the embed token",
            )
        except Exception as exc:
            logger.warning("REGOS embed token exchange failed: ci=%s error=%s", ci, exc)
            return self._error_payload("embed_token_exchange_failed", str(exc))

        ttl_sec = session_ttl_from_oauth_payload(oauth_payload)
        session_token = secrets.token_urlsafe(40)
        session = build_embed_session(
            connected_integration_id=ci,
            oauth_payload=oauth_payload,
            ttl_sec=ttl_sec,
            nonce=str(nonce or "").strip(),
            origin=iframe_origin,
        )
        await ChatGptRegosAssistantRedisState.store_embed_session(
            ci,
            session_token,
            session,
            ttl_sec,
        )
        public_session = public_embed_session(session)
        return {
            "ok": True,
            "status": "authorized",
            "embed_session_token": session_token,
            "expires_in": ttl_sec,
            "session": public_session,
            "user": public_session.get("user") or {},
        }

    async def embed_login(self, **kwargs: Any) -> Dict[str, Any]:
        return await self.consume_embed_token(**kwargs)

    async def _load_embed_session(
        self, embed_session_token: Optional[str]
    ) -> tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
        token = str(embed_session_token or "").strip()
        if not token:
            return None, None
        ci = self._ci()
        if not ci:
            return None, self._error_payload(
                "missing_connected_integration_id",
                "connected_integration_id is required",
            )
        session = await ChatGptRegosAssistantRedisState.get_embed_session(ci, token)
        if not session:
            return None, self._error_payload(
                "embed_session_expired",
                "iframe session is expired or not found",
            )
        if str(session.get("connected_integration_id") or "").strip() != ci:
            return None, self._error_payload(
                "embed_session_mismatch",
                "iframe session belongs to another connected integration",
            )
        if int(session.get("expires_at") or 0) <= int(time.time()):
            return None, self._error_payload(
                "embed_session_expired",
                "iframe session is expired or not found",
            )
        return session, None

    @staticmethod
    def _assistant_instructions(
        runtime: RuntimeConfig,
        embed_session: Optional[Dict[str, Any]],
    ) -> str:
        if not embed_session:
            return runtime.assistant_prompt
        session_context = public_embed_session(embed_session)
        return (
            runtime.assistant_prompt
            + "\n\nCurrent REGOS iframe user context, received from REGOS Embed OAuth. "
            + "Use it only for authorization/audit context and never expose token values: "
            + json_dumps(session_context)
        )

    @staticmethod
    def _message_text(message: Optional[str], messages: Optional[List[Any]]) -> str:
        parts: List[str] = []
        if message:
            parts.append(str(message))
        for item in messages or []:
            if isinstance(item, dict):
                content = item.get("content")
                if isinstance(content, str):
                    parts.append(content)
                elif isinstance(content, list):
                    for part in content:
                        if isinstance(part, dict) and isinstance(part.get("text"), str):
                            parts.append(part["text"])
            elif isinstance(item, str):
                parts.append(item)
        return " ".join(parts).lower()

    @staticmethod
    def _tool_category(tool_name: str) -> str:
        if tool_name.startswith(("client_", "deal_", "ticket_")):
            return "crm"
        if tool_name.startswith(("chat_", "quick_reply_")):
            return "chat"
        if tool_name.startswith(
            (
                "doc_",
                "inventory_operation_",
                "movement_operation_",
                "in_out_operation_",
                "purchase_operation_",
                "whole_sale_operation_",
                "stock_aggregation_operation_",
            )
        ):
            return "store"
        return "references"

    @classmethod
    def _select_tools_for_chat(
        cls,
        *,
        message: Optional[str],
        messages: Optional[List[Any]],
    ) -> List[RegosTool]:
        text = cls._message_text(message, messages)
        categories: set[str] = set()

        if any(
            keyword in text
            for keyword in (
                "клиент",
                "сделк",
                "лид",
                "тикет",
                "воронк",
                "этап",
                "crm",
                "client",
                "deal",
                "ticket",
            )
        ):
            categories.add("crm")
        if any(
            keyword in text
            for keyword in (
                "товар",
                "номенклат",
                "склад",
                "остат",
                "цена",
                "штрих",
                "инвентар",
                "перемещ",
                "оприход",
                "списан",
                "закуп",
                "поступ",
                "продаж",
                "отгруз",
                "barcode",
                "item",
                "stock",
                "inventory",
                "movement",
                "purchase",
                "warehouse",
            )
        ):
            categories.update({"references", "store"})
        if any(
            keyword in text
            for keyword in (
                "чат",
                "сообщ",
                "переписк",
                "message",
                "chat",
            )
        ):
            categories.add("chat")

        core_names = (
            "client_get",
            "deal_get",
            "ticket_get",
            "item_get",
            "item_get_short",
            "item_search",
            "item_get_quantity",
            "item_get_current_quantity",
            "item_price_get",
            "item_operation_get",
            "stock_get",
            "doc_inventory_get",
            "inventory_operation_get",
            "doc_movement_get",
            "movement_operation_get",
            "doc_in_out_get",
            "in_out_operation_get",
            "doc_purchase_get",
            "purchase_operation_get",
            "doc_whole_sale_get",
            "whole_sale_operation_get",
            "chat_get",
            "chat_message_get",
            "chat_message_add",
        )
        selected: List[RegosTool] = []
        seen: set[str] = set()

        def add_tool(name: str, tool: Optional[RegosTool] = None) -> None:
            resolved = tool or REGOS_TOOLS.get(name)
            if resolved is None or resolved.name in seen:
                return
            if len(selected) >= ChatGptRegosAssistantConfig.MAX_OPENAI_TOOLS:
                return
            selected.append(resolved)
            seen.add(resolved.name)

        for name in core_names:
            add_tool(name)

        if not categories:
            return selected

        for name, tool in REGOS_TOOLS.items():
            if cls._tool_category(name) in categories:
                add_tool(name, tool)
        return selected

    async def _build_ui_context(
        self, envelope: Optional[Dict[str, Any]] = None
    ) -> ChatGptRegosAssistantUiContext:
        envelope = envelope or {}
        ci = (
            self._ci()
            or self._query_value(envelope, "ci")
            or str(envelope.get("connected_integration_id") or "").strip()
        )
        if ci and not self.connected_integration_id:
            self.connected_integration_id = ci

        settings_map: Dict[str, str] = {}
        error = ""
        if ci:
            try:
                settings_map = await self._fetch_settings_map(ci)
            except Exception as exc:
                error = str(exc)
                logger.warning("Failed to load ChatGPT assistant UI settings: ci=%s error=%s", ci, exc)

        runtime = self._build_runtime(settings_map)
        mode = (
            "server_chat_ready"
            if runtime.openai_api_key
            else "missing_openai_api_key"
            if ci
            else "missing_connection"
        )
        external_url = self._external_base_url(ci) if ci else ""
        embed_parent_origin = (
            str(settings_map.get("chatgpt_regos_parent_origin") or "").strip()
            or ChatGptRegosAssistantConfig.EMBED_PARENT_ORIGIN
        )
        return ChatGptRegosAssistantUiContext(
            connected_integration_id=ci,
            api_url=f"/clients/{ChatGptRegosAssistantConfig.INTEGRATION_KEY}",
            external_url=external_url,
            embed_backend_url=f"{external_url}embed/consume" if external_url else "",
            embed_sdk_url=ChatGptRegosAssistantConfig.EMBED_SDK_URL,
            oauth_client_id=oauth_client_id(),
            embed_parent_origin=embed_parent_origin,
            model=runtime.openai_model,
            tools_count=len(REGOS_TOOLS),
            confirmation_ttl_sec=runtime.confirmation_ttl_sec,
            openai_api_chat_enabled=bool(runtime.openai_api_key),
            mode=mode,
            error=error,
        )

    async def handle_ui(self, envelope: Dict[str, Any]) -> HTMLResponse:
        ctx = await self._build_ui_context(envelope)
        return HTMLResponse(render_chatgpt_regos_assistant_ui(ctx))

    async def list_tools(self, **_: Any) -> Dict[str, Any]:
        return {
            "tools": [tool.as_openai_tool() for tool in REGOS_TOOLS.values()],
            "confirmation_required_for_mutations": True,
        }

    async def execute_tool(
        self,
        tool_name: Optional[str] = None,
        arguments: Any = None,
        name: Optional[str] = None,
        embed_session_token: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        ci = self._ci()
        if not ci:
            return {"status": "error", "error": "connected_integration_id is required"}

        embed_session, session_error = await self._load_embed_session(embed_session_token)
        if session_error:
            return session_error

        resolved_name = str(tool_name or name or "").strip()
        tool = REGOS_TOOLS.get(resolved_name)
        if tool is None:
            return {
                "status": "error",
                "error": f"Unknown tool: {resolved_name}",
                "available_tools": sorted(REGOS_TOOLS),
            }

        meta_keys = {"user_id", "session_id", "reason", "source"}
        meta = {key: kwargs.pop(key) for key in list(kwargs.keys()) if key in meta_keys}
        if embed_session:
            meta["embed_session_hash"] = self._session_token_hash(embed_session_token or "")
            meta["embed_user"] = public_embed_session(embed_session).get("user") or {}
        args = self._normalize_arguments(arguments, kwargs)

        if tool.mutating:
            runtime = await self._load_runtime(ci)
            confirmation_id = secrets.token_urlsafe(18)
            pending = {
                "confirmation_id": confirmation_id,
                "connected_integration_id": ci,
                "tool_name": tool.name,
                "regos_method": tool.regos_method,
                "arguments": args,
                "meta": meta,
                "created_at": int(time.time()),
                "expires_in_sec": runtime.confirmation_ttl_sec,
            }
            await ChatGptRegosAssistantRedisState.store_pending(
                ci,
                confirmation_id,
                pending,
                runtime.confirmation_ttl_sec,
            )
            return {
                "status": "requires_confirmation",
                "requires_confirmation": True,
                "confirmation_id": confirmation_id,
                "expires_in_sec": runtime.confirmation_ttl_sec,
                "tool_name": tool.name,
                "regos_method": tool.regos_method,
                "arguments": args,
                "message": (
                    f"Confirm execution of {tool.regos_method}. "
                    f"Call confirm_action with confirmation_id={confirmation_id}."
                ),
            }

        return await self._run_tool(ci, tool, args, embed_session=embed_session)

    async def confirm_action(
        self,
        confirmation_id: Optional[str] = None,
        approved: Any = True,
        embed_session_token: Optional[str] = None,
        **_: Any,
    ) -> Dict[str, Any]:
        ci = self._ci()
        if not ci:
            return {"status": "error", "error": "connected_integration_id is required"}
        embed_session, session_error = await self._load_embed_session(embed_session_token)
        if session_error:
            return session_error
        confirmation_id = str(confirmation_id or "").strip()
        if not confirmation_id:
            return {"status": "error", "error": "confirmation_id is required"}

        pending = await ChatGptRegosAssistantRedisState.pop_pending(ci, confirmation_id)
        if not pending:
            return {
                "status": "expired_or_not_found",
                "confirmation_id": confirmation_id,
                "executed": False,
            }

        if not parse_bool(approved, default=True):
            return {
                "status": "cancelled",
                "confirmation_id": confirmation_id,
                "executed": False,
                "tool_name": pending.get("tool_name"),
            }

        pending_meta = pending.get("meta") if isinstance(pending.get("meta"), dict) else {}
        pending_session_hash = str(pending_meta.get("embed_session_hash") or "").strip()
        if pending_session_hash and pending_session_hash != self._session_token_hash(
            embed_session_token or ""
        ):
            return {
                "status": "forbidden",
                "error": "embed_session_mismatch",
                "confirmation_id": confirmation_id,
                "executed": False,
            }

        tool_name = str(pending.get("tool_name") or "").strip()
        tool = REGOS_TOOLS.get(tool_name)
        if tool is None:
            return {
                "status": "error",
                "error": f"Unknown pending tool: {tool_name}",
                "confirmation_id": confirmation_id,
                "executed": False,
            }
        result = await self._run_tool(
            ci,
            tool,
            pending.get("arguments") or {},
            embed_session=embed_session,
        )
        result["confirmation_id"] = confirmation_id
        result["confirmed"] = True
        return result

    async def _run_tool(
        self,
        connected_integration_id: str,
        tool: RegosTool,
        arguments: Dict[str, Any],
        *,
        embed_session: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        async with RegosAPI(
            connected_integration_id=connected_integration_id,
            bearer_token=access_token_from_session(embed_session),
        ) as api:
            target: Any = api
            for attr in tool.service_path:
                target = getattr(target, attr)
            payload: Any = arguments
            if tool.payload_key:
                payload = arguments.get(tool.payload_key, arguments)
            result = await target(payload)

        return {
            "status": "executed",
            "requires_confirmation": False,
            "tool_name": tool.name,
            "regos_method": tool.regos_method,
            "mutating": tool.mutating,
            "result": jsonable(result),
        }

    async def chat(
        self,
        message: Optional[str] = None,
        messages: Optional[List[Any]] = None,
        embed_session_token: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        ci = self._ci()
        if not ci:
            return {"status": "error", "error": "connected_integration_id is required"}

        embed_session, session_error = await self._load_embed_session(embed_session_token)
        if session_error:
            return session_error

        runtime = await self._load_runtime(ci)
        if not runtime.openai_api_key:
            return {
                "status": "error",
                "error": "chatgpt_openai_api_key or openai_api_key is required for server-side chat mode",
                "hint": "Add an OpenAI API key to the connected integration settings.",
                "tools": sorted(REGOS_TOOLS),
            }

        selected_tools = self._select_tools_for_chat(message=message, messages=messages)
        openai_tools = [tool.as_openai_tool() for tool in selected_tools]
        payload: Dict[str, Any] = {
            "model": runtime.openai_model,
            "instructions": self._assistant_instructions(runtime, embed_session),
            "input": build_openai_input(
                message=message,
                messages=messages,
                kwargs=kwargs,
            ),
            "tools": openai_tools,
            "temperature": runtime.temperature,
            "max_output_tokens": runtime.max_output_tokens,
        }

        last_response: Dict[str, Any] = {}
        tool_results: List[Dict[str, Any]] = []
        async with httpx.AsyncClient(timeout=90) as client:
            for _round in range(runtime.max_tool_rounds):
                last_response = await post_openai_response(client, runtime, payload)
                calls = extract_openai_tool_calls(last_response)
                if not calls:
                    return {
                        "status": "answered",
                        "reply": extract_openai_text(last_response),
                        "response_id": last_response.get("id"),
                        "tool_results": tool_results,
                    }

                function_outputs: List[Dict[str, Any]] = []
                for call in calls:
                    tool_result = await self.execute_tool(
                        tool_name=call.name,
                        arguments=call.arguments,
                        source="openai_responses",
                        embed_session_token=embed_session_token,
                    )
                    tool_results.append(tool_result)
                    if tool_result.get("requires_confirmation"):
                        return {
                            "status": "requires_confirmation",
                            "reply": tool_result.get("message"),
                            "response_id": last_response.get("id"),
                            "pending_action": tool_result,
                            "tool_results": tool_results,
                        }
                    function_outputs.append(
                        {
                            "type": "function_call_output",
                            "call_id": call.call_id,
                            "output": json_dumps(tool_result),
                        }
                    )

                payload = {
                    "model": runtime.openai_model,
                    "previous_response_id": last_response.get("id"),
                    "input": function_outputs,
                    "tools": openai_tools,
                    "temperature": runtime.temperature,
                    "max_output_tokens": runtime.max_output_tokens,
                }

        return {
            "status": "tool_round_limit_reached",
            "reply": extract_openai_text(last_response),
            "response_id": last_response.get("id"),
            "tool_results": tool_results,
        }

    async def handle_external(self, envelope: Dict[str, Any]) -> Any:
        body = envelope.get("body")
        payload = body if isinstance(body, dict) else {}

        path = str(envelope.get("external_path") or "").strip("/")
        action = str(payload.get("action") or path.split("/", 1)[0] or "").strip().lower()
        embed_response = await self._handle_embed_external(path, payload)
        if embed_response is not None:
            return embed_response
        action_payload = self._action_payload(payload)
        if action in {"ui", "app"}:
            return await self.handle_ui(envelope)
        if action in {"", "metadata", "info"}:
            return await self.metadata()
        if action in {"tools", "list_tools"}:
            return await self.list_tools()
        if action in {"execute", "execute_tool"}:
            return await self.execute_tool(
                tool_name=action_payload.get("tool_name") or action_payload.get("name"),
                arguments=action_payload.get("arguments")
                or action_payload.get("args")
                or action_payload.get("payload"),
                embed_session_token=self._payload_text(
                    action_payload,
                    "embed_session_token",
                    "embedSessionToken",
                ),
            )
        if action in {"confirm", "confirm_action"}:
            return await self.confirm_action(
                confirmation_id=action_payload.get("confirmation_id"),
                approved=action_payload.get("approved", True),
                embed_session_token=self._payload_text(
                    action_payload,
                    "embed_session_token",
                    "embedSessionToken",
                ),
            )
        if action == "chat":
            return await self.chat(
                message=action_payload.get("message")
                or action_payload.get("text")
                or action_payload.get("prompt"),
                messages=action_payload.get("messages")
                if isinstance(action_payload.get("messages"), list)
                else None,
                embed_session_token=self._payload_text(
                    action_payload,
                    "embed_session_token",
                    "embedSessionToken",
                ),
            )
        return {"status": "error", "error": f"Unsupported external action: {action}"}

    async def _handle_embed_external(
        self, path: str, payload: Dict[str, Any]
    ) -> Any:
        normalized_path = str(path or "").strip("/").lower()
        action = str(payload.get("action") or "").strip().lower()
        if normalized_path != "embed/consume" and action not in {
            "embed",
            "embed_login",
            "consume_embed_token",
        }:
            return None

        data = self._action_payload(payload)
        result = await self.consume_embed_token(
            embed_token=self._payload_text(data, "embed_token", "embedToken"),
            connected_integration_id=self._payload_text(
                data,
                "connected_integration_id",
                "connectedIntegrationId",
            ),
            nonce=self._payload_text(data, "nonce"),
            origin=self._payload_text(data, "origin"),
        )
        if result.get("ok") is False:
            return JSONResponse(status_code=400, content=result)
        return result

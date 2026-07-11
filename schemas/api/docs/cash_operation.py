"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class CashAmountDetailsGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)


class CashOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    type: CashOperationType | None = PydField(default=None)
    payment_type_id: int | None = PydField(default=None)
    payment_type_name: str | None = PydField(default=None)
    session_uuid: str | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    user_full_name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CashOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class CashOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CashOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class CashOperationType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CashAmountDetailsRegosObjectResult, Error


CashOperationGetAmountDetailsRequest: TypeAlias = CashAmountDetailsGet
CashOperationGetAmountDetailsResponse: TypeAlias = CashAmountDetailsRegosObjectResult
CashOperationGetRequest: TypeAlias = CashOperationGet
CashOperationGetResponse: TypeAlias = CashOperationRegosOffsettedArrayResult


_MODEL_NAMES = ['CashAmountDetailsGet', 'CashOperation', 'CashOperationGet', 'CashOperationRegosOffsettedArrayResult', 'CashOperationType']


__all__ = [
    'CashAmountDetailsGet',
    'CashOperation',
    'CashOperationGet',
    'CashOperationRegosOffsettedArrayResult',
    'CashOperationType',
    'CashOperationGetRequest',
    'CashOperationGetResponse',
    'CashOperationGetAmountDetailsRequest',
    'CashOperationGetAmountDetailsResponse'
]

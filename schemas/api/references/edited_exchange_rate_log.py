"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class EditedExchangeRateLog(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user: User | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    date: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class EditedExchangeRateLogGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    currency_id: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class EditedExchangeRateLogRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[EditedExchangeRateLog] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency


EditedExchangeRateLogGetRequest: TypeAlias = EditedExchangeRateLogGet
EditedExchangeRateLogGetResponse: TypeAlias = EditedExchangeRateLogRegosOffsettedArrayResult


_MODEL_NAMES = ['EditedExchangeRateLog', 'EditedExchangeRateLogGet', 'EditedExchangeRateLogRegosOffsettedArrayResult']


__all__ = [
    'EditedExchangeRateLog',
    'EditedExchangeRateLogGet',
    'EditedExchangeRateLogRegosOffsettedArrayResult',
    'EditedExchangeRateLogGetRequest',
    'EditedExchangeRateLogGetResponse'
]

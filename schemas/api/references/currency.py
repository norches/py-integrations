"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Currency(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code_num: int | None = PydField(default=None)
    code_chr: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    is_base: bool | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CurrencyAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code_num: int | None = PydField(default=None)
    code_chr: str | None = PydField(default=None)
    name: str | None = PydField(default=None)


class CurrencyDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class CurrencyEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    code_num: int | None = PydField(default=None)
    code_chr: str | None = PydField(default=None)
    name: str | None = PydField(default=None)


class CurrencyEditExchangeRate(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)


class CurrencyGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[CurrencySortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class CurrencyRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Currency] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class CurrencySortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: CurrencySortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class CurrencySortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


CurrencyAddRequest: TypeAlias = CurrencyAdd
CurrencyAddResponse: TypeAlias = InsertResult
CurrencyDeleteRequest: TypeAlias = CurrencyDelete
CurrencyDeleteResponse: TypeAlias = UpdateResult
CurrencyEditExchangeRateRequest: TypeAlias = CurrencyEditExchangeRate
CurrencyEditExchangeRateResponse: TypeAlias = UpdateResult
CurrencyEditRequest: TypeAlias = CurrencyEdit
CurrencyEditResponse: TypeAlias = UpdateResult
CurrencyGetRequest: TypeAlias = CurrencyGet
CurrencyGetResponse: TypeAlias = CurrencyRegosOffsettedArrayResult


_MODEL_NAMES = ['Currency', 'CurrencyAdd', 'CurrencyDelete', 'CurrencyEdit', 'CurrencyEditExchangeRate', 'CurrencyGet', 'CurrencyRegosOffsettedArrayResult', 'CurrencySortOrder']


__all__ = [
    'Currency',
    'CurrencyAdd',
    'CurrencyDelete',
    'CurrencyEdit',
    'CurrencyEditExchangeRate',
    'CurrencyGet',
    'CurrencyRegosOffsettedArrayResult',
    'CurrencySortOrder',
    'CurrencySortOrderColumn',
    'CurrencyGetRequest',
    'CurrencyGetResponse',
    'CurrencyAddRequest',
    'CurrencyAddResponse',
    'CurrencyEditRequest',
    'CurrencyEditResponse',
    'CurrencyDeleteRequest',
    'CurrencyDeleteResponse',
    'CurrencyEditExchangeRateRequest',
    'CurrencyEditExchangeRateResponse'
]

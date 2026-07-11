"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PriceType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    round_to: _Decimal | None = PydField(default=None)
    markup: _Decimal | None = PydField(default=None)
    max_discount: _Decimal | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    currency_additional: Currency | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PriceTypeAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    currency_additional_id: int | None = PydField(default=None)
    round_to: _Decimal | None = PydField(default=None)
    markup: _Decimal | None = PydField(default=None)
    max_discount: _Decimal | None = PydField(default=None)


class PriceTypeDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PriceTypeEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    currency_additional_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    round_to: _Decimal | None = PydField(default=None)
    markup: _Decimal | None = PydField(default=None)
    max_discount: _Decimal | None = PydField(default=None)


class PriceTypeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    currency_ids: list[int] | None = PydField(default=None)
    sort_orders: list[PriceType_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class PriceTypeRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PriceType] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class PriceType_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: PriceType_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class PriceType_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.currency import Currency


PriceTypeAddRequest: TypeAlias = PriceTypeAdd
PriceTypeAddResponse: TypeAlias = InsertResult
PriceTypeDeleteRequest: TypeAlias = PriceTypeDelete
PriceTypeDeleteResponse: TypeAlias = UpdateResult
PriceTypeEditRequest: TypeAlias = PriceTypeEdit
PriceTypeEditResponse: TypeAlias = UpdateResult
PriceTypeGetRequest: TypeAlias = PriceTypeGet
PriceTypeGetResponse: TypeAlias = PriceTypeRegosOffsettedArrayResult


_MODEL_NAMES = ['PriceType', 'PriceTypeAdd', 'PriceTypeDelete', 'PriceTypeEdit', 'PriceTypeGet', 'PriceTypeRegosOffsettedArrayResult', 'PriceType_SortOrder']


__all__ = [
    'PriceType',
    'PriceTypeAdd',
    'PriceTypeDelete',
    'PriceTypeEdit',
    'PriceTypeGet',
    'PriceTypeRegosOffsettedArrayResult',
    'PriceType_SortOrder',
    'PriceType_SortOrderColumn',
    'PriceTypeGetRequest',
    'PriceTypeGetResponse',
    'PriceTypeAddRequest',
    'PriceTypeAddResponse',
    'PriceTypeEditRequest',
    'PriceTypeEditResponse',
    'PriceTypeDeleteRequest',
    'PriceTypeDeleteResponse'
]

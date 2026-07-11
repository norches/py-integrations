"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Stock(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    area: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class StockAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    address: str | None = PydField(default=None)
    area: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class StockDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class StockDeleteConfirm(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    confirm_code: str | None = PydField(default=None)


class StockDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class StockEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    area: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class StockGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    sort_orders: list[Stock_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class StockRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Stock] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class Stock_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: Stock_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class Stock_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ApiResult, ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.firm import Firm


StockAddRequest: TypeAlias = StockAdd
StockAddResponse: TypeAlias = InsertResult
StockDeleteConfirmRequest: TypeAlias = StockDeleteConfirm
StockDeleteConfirmResponse: TypeAlias = ApiResult
StockDeleteMarkRequest: TypeAlias = StockDeleteMark
StockDeleteMarkResponse: TypeAlias = UpdateResult
StockDeleteRequest: TypeAlias = StockDelete
StockDeleteResponse: TypeAlias = ApiResult
StockEditRequest: TypeAlias = StockEdit
StockEditResponse: TypeAlias = UpdateResult
StockGetRequest: TypeAlias = StockGet
StockGetResponse: TypeAlias = StockRegosOffsettedArrayResult


_MODEL_NAMES = ['Stock', 'StockAdd', 'StockDelete', 'StockDeleteConfirm', 'StockDeleteMark', 'StockEdit', 'StockGet', 'StockRegosOffsettedArrayResult', 'Stock_SortOrder']


__all__ = [
    'Stock',
    'StockAdd',
    'StockDelete',
    'StockDeleteConfirm',
    'StockDeleteMark',
    'StockEdit',
    'StockGet',
    'StockRegosOffsettedArrayResult',
    'Stock_SortOrder',
    'Stock_SortOrderColumn',
    'StockGetRequest',
    'StockGetResponse',
    'StockAddRequest',
    'StockAddResponse',
    'StockEditRequest',
    'StockEditResponse',
    'StockDeleteMarkRequest',
    'StockDeleteMarkResponse',
    'StockDeleteRequest',
    'StockDeleteResponse',
    'StockDeleteConfirmRequest',
    'StockDeleteConfirmResponse'
]

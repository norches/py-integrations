"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailReturnReason(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailReturnReasonAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class RetailReturnReasonDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class RetailReturnReasonEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class RetailReturnReasonGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)
    sort_orders: list[RetailReturnReason_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailReturnReasonRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailReturnReason] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailReturnReason_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: RetailReturnReason_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class RetailReturnReason_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


RetailReturnReasonAddRequest: TypeAlias = RetailReturnReasonAdd
RetailReturnReasonAddResponse: TypeAlias = InsertResult
RetailReturnReasonDeleteRequest: TypeAlias = RetailReturnReasonDelete
RetailReturnReasonDeleteResponse: TypeAlias = UpdateResult
RetailReturnReasonEditRequest: TypeAlias = RetailReturnReasonEdit
RetailReturnReasonEditResponse: TypeAlias = UpdateResult
RetailReturnReasonGetRequest: TypeAlias = RetailReturnReasonGet
RetailReturnReasonGetResponse: TypeAlias = RetailReturnReasonRegosOffsettedArrayResult


_MODEL_NAMES = ['RetailReturnReason', 'RetailReturnReasonAdd', 'RetailReturnReasonDelete', 'RetailReturnReasonEdit', 'RetailReturnReasonGet', 'RetailReturnReasonRegosOffsettedArrayResult', 'RetailReturnReason_SortOrder']


__all__ = [
    'RetailReturnReason',
    'RetailReturnReasonAdd',
    'RetailReturnReasonDelete',
    'RetailReturnReasonEdit',
    'RetailReturnReasonGet',
    'RetailReturnReasonRegosOffsettedArrayResult',
    'RetailReturnReason_SortOrder',
    'RetailReturnReason_SortOrderColumn',
    'RetailReturnReasonGetRequest',
    'RetailReturnReasonGetResponse',
    'RetailReturnReasonAddRequest',
    'RetailReturnReasonAddResponse',
    'RetailReturnReasonEditRequest',
    'RetailReturnReasonEditResponse',
    'RetailReturnReasonDeleteRequest',
    'RetailReturnReasonDeleteResponse'
]

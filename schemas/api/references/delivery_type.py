"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DeliveryType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DeliveryTypeAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)


class DeliveryTypeDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DeliveryTypeEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class DeliveryTypeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[DeliveryType_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DeliveryTypeRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DeliveryType] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DeliveryType_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DeliveryType_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DeliveryType_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


DeliveryTypeAddRequest: TypeAlias = DeliveryTypeAdd
DeliveryTypeAddResponse: TypeAlias = InsertResult
DeliveryTypeDeleteRequest: TypeAlias = DeliveryTypeDelete
DeliveryTypeDeleteResponse: TypeAlias = UpdateResult
DeliveryTypeEditRequest: TypeAlias = DeliveryTypeEdit
DeliveryTypeEditResponse: TypeAlias = UpdateResult
DeliveryTypeGetRequest: TypeAlias = DeliveryTypeGet
DeliveryTypeGetResponse: TypeAlias = DeliveryTypeRegosOffsettedArrayResult


_MODEL_NAMES = ['DeliveryType', 'DeliveryTypeAdd', 'DeliveryTypeDelete', 'DeliveryTypeEdit', 'DeliveryTypeGet', 'DeliveryTypeRegosOffsettedArrayResult', 'DeliveryType_SortOrder']


__all__ = [
    'DeliveryType',
    'DeliveryTypeAdd',
    'DeliveryTypeDelete',
    'DeliveryTypeEdit',
    'DeliveryTypeGet',
    'DeliveryTypeRegosOffsettedArrayResult',
    'DeliveryType_SortOrder',
    'DeliveryType_SortOrderColumn',
    'DeliveryTypeGetRequest',
    'DeliveryTypeGetResponse',
    'DeliveryTypeAddRequest',
    'DeliveryTypeAddResponse',
    'DeliveryTypeEditRequest',
    'DeliveryTypeEditResponse',
    'DeliveryTypeDeleteRequest',
    'DeliveryTypeDeleteResponse'
]

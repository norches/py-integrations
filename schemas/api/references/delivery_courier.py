"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DeliveryCourier(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DeliveryCourierAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DeliveryCourierDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DeliveryCourierEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DeliveryCourierGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[DeliveryCourier_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DeliveryCourierRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DeliveryCourier] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DeliveryCourier_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DeliveryCourier_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DeliveryCourier_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


DeliveryCourierAddRequest: TypeAlias = DeliveryCourierAdd
DeliveryCourierAddResponse: TypeAlias = InsertResult
DeliveryCourierDeleteRequest: TypeAlias = DeliveryCourierDelete
DeliveryCourierDeleteResponse: TypeAlias = UpdateResult
DeliveryCourierEditRequest: TypeAlias = DeliveryCourierEdit
DeliveryCourierEditResponse: TypeAlias = UpdateResult
DeliveryCourierGetRequest: TypeAlias = DeliveryCourierGet
DeliveryCourierGetResponse: TypeAlias = DeliveryCourierRegosOffsettedArrayResult


_MODEL_NAMES = ['DeliveryCourier', 'DeliveryCourierAdd', 'DeliveryCourierDelete', 'DeliveryCourierEdit', 'DeliveryCourierGet', 'DeliveryCourierRegosOffsettedArrayResult', 'DeliveryCourier_SortOrder']


__all__ = [
    'DeliveryCourier',
    'DeliveryCourierAdd',
    'DeliveryCourierDelete',
    'DeliveryCourierEdit',
    'DeliveryCourierGet',
    'DeliveryCourierRegosOffsettedArrayResult',
    'DeliveryCourier_SortOrder',
    'DeliveryCourier_SortOrderColumn',
    'DeliveryCourierGetRequest',
    'DeliveryCourierGetResponse',
    'DeliveryCourierAddRequest',
    'DeliveryCourierAddResponse',
    'DeliveryCourierEditRequest',
    'DeliveryCourierEditResponse',
    'DeliveryCourierDeleteRequest',
    'DeliveryCourierDeleteResponse'
]

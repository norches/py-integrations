"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DeliveryFrom(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DeliveryFromAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)


class DeliveryFromDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DeliveryFromEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class DeliveryFromGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[DeliveryFrom_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DeliveryFromRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DeliveryFrom] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DeliveryFrom_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DeliveryFrom_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DeliveryFrom_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


DeliveryFromAddRequest: TypeAlias = DeliveryFromAdd
DeliveryFromAddResponse: TypeAlias = InsertResult
DeliveryFromDeleteRequest: TypeAlias = DeliveryFromDelete
DeliveryFromDeleteResponse: TypeAlias = UpdateResult
DeliveryFromEditRequest: TypeAlias = DeliveryFromEdit
DeliveryFromEditResponse: TypeAlias = UpdateResult
DeliveryFromGetRequest: TypeAlias = DeliveryFromGet
DeliveryFromGetResponse: TypeAlias = DeliveryFromRegosOffsettedArrayResult


_MODEL_NAMES = ['DeliveryFrom', 'DeliveryFromAdd', 'DeliveryFromDelete', 'DeliveryFromEdit', 'DeliveryFromGet', 'DeliveryFromRegosOffsettedArrayResult', 'DeliveryFrom_SortOrder']


__all__ = [
    'DeliveryFrom',
    'DeliveryFromAdd',
    'DeliveryFromDelete',
    'DeliveryFromEdit',
    'DeliveryFromGet',
    'DeliveryFromRegosOffsettedArrayResult',
    'DeliveryFrom_SortOrder',
    'DeliveryFrom_SortOrderColumn',
    'DeliveryFromGetRequest',
    'DeliveryFromGetResponse',
    'DeliveryFromAddRequest',
    'DeliveryFromAddResponse',
    'DeliveryFromEditRequest',
    'DeliveryFromEditResponse',
    'DeliveryFromDeleteRequest',
    'DeliveryFromDeleteResponse'
]

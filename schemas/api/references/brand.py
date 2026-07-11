"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Brand(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class BrandAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)


class BrandDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class BrandEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class BrandGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[BrandSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class BrandRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Brand] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class BrandSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: BrandSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class BrandSortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


BrandAddRequest: TypeAlias = BrandAdd
BrandAddResponse: TypeAlias = InsertResult
BrandDeleteRequest: TypeAlias = BrandDelete
BrandDeleteResponse: TypeAlias = UpdateResult
BrandEditRequest: TypeAlias = BrandEdit
BrandEditResponse: TypeAlias = UpdateResult
BrandGetRequest: TypeAlias = BrandGet
BrandGetResponse: TypeAlias = BrandRegosOffsettedArrayResult


_MODEL_NAMES = ['Brand', 'BrandAdd', 'BrandDelete', 'BrandEdit', 'BrandGet', 'BrandRegosOffsettedArrayResult', 'BrandSortOrder']


__all__ = [
    'Brand',
    'BrandAdd',
    'BrandDelete',
    'BrandEdit',
    'BrandGet',
    'BrandRegosOffsettedArrayResult',
    'BrandSortOrder',
    'BrandSortOrderColumn',
    'BrandGetRequest',
    'BrandGetResponse',
    'BrandAddRequest',
    'BrandAddResponse',
    'BrandEditRequest',
    'BrandEditResponse',
    'BrandDeleteRequest',
    'BrandDeleteResponse'
]

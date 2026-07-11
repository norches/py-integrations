"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Color(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ColorAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)


class ColorDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ColorEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class ColorGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[ColorSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ColorRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Color] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ColorSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: ColorSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class ColorSortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


ColorAddRequest: TypeAlias = ColorAdd
ColorAddResponse: TypeAlias = InsertResult
ColorDeleteRequest: TypeAlias = ColorDelete
ColorDeleteResponse: TypeAlias = UpdateResult
ColorEditRequest: TypeAlias = ColorEdit
ColorEditResponse: TypeAlias = UpdateResult
ColorGetRequest: TypeAlias = ColorGet
ColorGetResponse: TypeAlias = ColorRegosOffsettedArrayResult


_MODEL_NAMES = ['Color', 'ColorAdd', 'ColorDelete', 'ColorEdit', 'ColorGet', 'ColorRegosOffsettedArrayResult', 'ColorSortOrder']


__all__ = [
    'Color',
    'ColorAdd',
    'ColorDelete',
    'ColorEdit',
    'ColorGet',
    'ColorRegosOffsettedArrayResult',
    'ColorSortOrder',
    'ColorSortOrderColumn',
    'ColorGetRequest',
    'ColorGetResponse',
    'ColorAddRequest',
    'ColorAddResponse',
    'ColorEditRequest',
    'ColorEditResponse',
    'ColorDeleteRequest',
    'ColorDeleteResponse'
]

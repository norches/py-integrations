"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Department(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DepartmentAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)


class DepartmentDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DepartmentEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class DepartmentGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[DepartmentSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DepartmentRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Department] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DepartmentSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DepartmentSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DepartmentSortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


DepartmentAddRequest: TypeAlias = DepartmentAdd
DepartmentAddResponse: TypeAlias = InsertResult
DepartmentDeleteRequest: TypeAlias = DepartmentDelete
DepartmentDeleteResponse: TypeAlias = UpdateResult
DepartmentEditRequest: TypeAlias = DepartmentEdit
DepartmentEditResponse: TypeAlias = UpdateResult
DepartmentGetRequest: TypeAlias = DepartmentGet
DepartmentGetResponse: TypeAlias = DepartmentRegosOffsettedArrayResult


_MODEL_NAMES = ['Department', 'DepartmentAdd', 'DepartmentDelete', 'DepartmentEdit', 'DepartmentGet', 'DepartmentRegosOffsettedArrayResult', 'DepartmentSortOrder']


__all__ = [
    'Department',
    'DepartmentAdd',
    'DepartmentDelete',
    'DepartmentEdit',
    'DepartmentGet',
    'DepartmentRegosOffsettedArrayResult',
    'DepartmentSortOrder',
    'DepartmentSortOrderColumn',
    'DepartmentGetRequest',
    'DepartmentGetResponse',
    'DepartmentAddRequest',
    'DepartmentAddResponse',
    'DepartmentEditRequest',
    'DepartmentEditResponse',
    'DepartmentDeleteRequest',
    'DepartmentDeleteResponse'
]

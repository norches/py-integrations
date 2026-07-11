"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RolePermission(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    role: Role | None = PydField(default=None)
    permission: Permission | None = PydField(default=None)
    value: bool | None = PydField(default=None)


class RolePermissionEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    role_id: int | None = PydField(default=None)
    permission_id: int | None = PydField(default=None)
    value: bool | None = PydField(default=None)


class RolePermissionGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    role_id: int | None = PydField(default=None)
    permission_id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    value: bool | None = PydField(default=None)
    sort_orders: list[RolePermission_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RolePermissionRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RolePermission] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RolePermission_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: RolePermission_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class RolePermission_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, Permission, UpdateResult
from schemas.api.rbac.role import Role


RolePermissionEditRequest: TypeAlias = list[RolePermissionEdit]
RolePermissionEditResponse: TypeAlias = UpdateResult
RolePermissionGetRequest: TypeAlias = RolePermissionGet
RolePermissionGetResponse: TypeAlias = RolePermissionRegosOffsettedArrayResult


_MODEL_NAMES = ['RolePermission', 'RolePermissionEdit', 'RolePermissionGet', 'RolePermissionRegosOffsettedArrayResult', 'RolePermission_SortOrder']


__all__ = [
    'RolePermission',
    'RolePermissionEdit',
    'RolePermissionGet',
    'RolePermissionRegosOffsettedArrayResult',
    'RolePermission_SortOrder',
    'RolePermission_SortOrderColumn',
    'RolePermissionGetRequest',
    'RolePermissionGetResponse',
    'RolePermissionEditRequest',
    'RolePermissionEditResponse'
]

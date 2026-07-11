"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserPermissionExt(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user: User | None = PydField(default=None)
    permission: Permission | None = PydField(default=None)
    value: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class UserPermissionExtArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserPermissionExt] | Error | None = PydField(default=None)


class UserPermissionGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_ids: list[int] | None = PydField(default=None)
    permission_ids: list[int] | None = PydField(default=None)


class UserPermissionGetEx(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    permission_group_id: int | None = PydField(default=None)


class UserPermissionShort(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    permission_id: int | None = PydField(default=None)
    value: bool | None = PydField(default=None)


class UserPermissionShortRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserPermissionShort] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, Permission
from schemas.api.rbac.user import User


UserPermissionGetExtRequest: TypeAlias = UserPermissionGetEx
UserPermissionGetExtResponse: TypeAlias = UserPermissionExtArrayRegosObjectResult


_MODEL_NAMES = ['UserPermissionExt', 'UserPermissionExtArrayRegosObjectResult', 'UserPermissionGet', 'UserPermissionGetEx', 'UserPermissionShort', 'UserPermissionShortRegosArrayResult']


__all__ = [
    'UserPermissionExt',
    'UserPermissionExtArrayRegosObjectResult',
    'UserPermissionGet',
    'UserPermissionGetEx',
    'UserPermissionShort',
    'UserPermissionShortRegosArrayResult',
    'UserPermissionGetExtRequest',
    'UserPermissionGetExtResponse'
]

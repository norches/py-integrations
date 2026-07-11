"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserRole(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    role: Role | None = PydField(default=None)


class UserRoleGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)


class UserRoleRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserRole] | Error | None = PydField(default=None)


class UserRoleRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserRoleSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    role_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.rbac.role import Role


UserRoleGetRequest: TypeAlias = UserRoleGet
UserRoleGetResponse: TypeAlias = UserRoleRegosArrayResult
UserRoleRemoveRequest: TypeAlias = UserRoleRemove
UserRoleRemoveResponse: TypeAlias = UpdateResult
UserRoleSetRequest: TypeAlias = UserRoleSet
UserRoleSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['UserRole', 'UserRoleGet', 'UserRoleRegosArrayResult', 'UserRoleRemove', 'UserRoleSet']


__all__ = [
    'UserRole',
    'UserRoleGet',
    'UserRoleRegosArrayResult',
    'UserRoleRemove',
    'UserRoleSet',
    'UserRoleGetRequest',
    'UserRoleGetResponse',
    'UserRoleSetRequest',
    'UserRoleSetResponse',
    'UserRoleRemoveRequest',
    'UserRoleRemoveResponse'
]

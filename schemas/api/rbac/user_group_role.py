"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserGroupRole(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    role: Role | None = PydField(default=None)


class UserGroupRoleGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    group_id: int | None = PydField(default=None)


class UserGroupRoleRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserGroupRole] | Error | None = PydField(default=None)


class UserGroupRoleRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserGroupRoleSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    group_id: int | None = PydField(default=None)
    role_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.rbac.role import Role


UserGroupRoleGetRequest: TypeAlias = UserGroupRoleGet
UserGroupRoleGetResponse: TypeAlias = UserGroupRoleRegosArrayResult
UserGroupRoleRemoveRequest: TypeAlias = UserGroupRoleRemove
UserGroupRoleRemoveResponse: TypeAlias = UpdateResult
UserGroupRoleSetRequest: TypeAlias = UserGroupRoleSet
UserGroupRoleSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['UserGroupRole', 'UserGroupRoleGet', 'UserGroupRoleRegosArrayResult', 'UserGroupRoleRemove', 'UserGroupRoleSet']


__all__ = [
    'UserGroupRole',
    'UserGroupRoleGet',
    'UserGroupRoleRegosArrayResult',
    'UserGroupRoleRemove',
    'UserGroupRoleSet',
    'UserGroupRoleGetRequest',
    'UserGroupRoleGetResponse',
    'UserGroupRoleSetRequest',
    'UserGroupRoleSetResponse',
    'UserGroupRoleRemoveRequest',
    'UserGroupRoleRemoveResponse'
]

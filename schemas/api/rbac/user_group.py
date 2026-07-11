"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    child_count: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class UserGroupAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class UserGroupArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserGroup] | Error | None = PydField(default=None)


class UserGroupDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserGroupEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class UserGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


UserGroupAddRequest: TypeAlias = UserGroupAdd
UserGroupAddResponse: TypeAlias = InsertResult
UserGroupDeleteRequest: TypeAlias = UserGroupDelete
UserGroupDeleteResponse: TypeAlias = UpdateResult
UserGroupEditRequest: TypeAlias = UserGroupEdit
UserGroupEditResponse: TypeAlias = UpdateResult
UserGroupGetRequest: TypeAlias = UserGroupGet
UserGroupGetResponse: TypeAlias = UserGroupArrayRegosObjectResult


_MODEL_NAMES = ['UserGroup', 'UserGroupAdd', 'UserGroupArrayRegosObjectResult', 'UserGroupDelete', 'UserGroupEdit', 'UserGroupGet']


__all__ = [
    'UserGroup',
    'UserGroupAdd',
    'UserGroupArrayRegosObjectResult',
    'UserGroupDelete',
    'UserGroupEdit',
    'UserGroupGet',
    'UserGroupGetRequest',
    'UserGroupGetResponse',
    'UserGroupAddRequest',
    'UserGroupAddResponse',
    'UserGroupEditRequest',
    'UserGroupEditResponse',
    'UserGroupDeleteRequest',
    'UserGroupDeleteResponse'
]

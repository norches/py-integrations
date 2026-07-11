"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserAccount(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    account: Account | None = PydField(default=None)


class UserAccountGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)


class UserAccountRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserAccount] | Error | None = PydField(default=None)


class UserAccountRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserAccountSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    account_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.references.account import Account


UserAccountGetRequest: TypeAlias = UserAccountGet
UserAccountGetResponse: TypeAlias = UserAccountRegosArrayResult
UserAccountRemoveRequest: TypeAlias = UserAccountRemove
UserAccountRemoveResponse: TypeAlias = UpdateResult
UserAccountSetRequest: TypeAlias = UserAccountSet
UserAccountSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['UserAccount', 'UserAccountGet', 'UserAccountRegosArrayResult', 'UserAccountRemove', 'UserAccountSet']


__all__ = [
    'UserAccount',
    'UserAccountGet',
    'UserAccountRegosArrayResult',
    'UserAccountRemove',
    'UserAccountSet',
    'UserAccountGetRequest',
    'UserAccountGetResponse',
    'UserAccountSetRequest',
    'UserAccountSetResponse',
    'UserAccountRemoveRequest',
    'UserAccountRemoveResponse'
]

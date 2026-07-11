"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class NotifyEntityEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15


class UserNotify(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    entity: NotifyEntityEnum | None = PydField(default=None)
    notification_key: str | None = PydField(default=None)
    value: bool | None = PydField(default=None)


class UserNotifyGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)


class UserNotifyRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserNotify] | Error | None = PydField(default=None)


class UserNotifySet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    notification_key: str | None = PydField(default=None)
    value: bool | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, UpdateResult


UserNotifyGetRequest: TypeAlias = UserNotifyGet
UserNotifyGetResponse: TypeAlias = UserNotifyRegosArrayResult
UserNotifySetRequest: TypeAlias = list[UserNotifySet]
UserNotifySetResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['UserNotify', 'UserNotifyGet', 'UserNotifyRegosArrayResult', 'UserNotifySet']


__all__ = [
    'NotifyEntityEnum',
    'UserNotify',
    'UserNotifyGet',
    'UserNotifyRegosArrayResult',
    'UserNotifySet',
    'UserNotifyGetRequest',
    'UserNotifyGetResponse',
    'UserNotifySetRequest',
    'UserNotifySetResponse'
]

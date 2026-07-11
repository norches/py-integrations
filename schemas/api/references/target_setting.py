"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class TargetSetting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    target_id: int | None = PydField(default=None)
    type: TargetSettingTypeEnum | None = PydField(default=None)
    value: str | None = PydField(default=None)
    include: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TargetSettingAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    target_id: int | None = PydField(default=None)
    type: TargetSettingTypeEnum | None = PydField(default=None)
    value: str | None = PydField(default=None)
    include: bool | None = PydField(default=None)


class TargetSettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    target_id: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    type: TargetSettingTypeEnum | None = PydField(default=None)


class TargetSettingRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[TargetSetting] | Error | None = PydField(default=None)


class TargetSettingTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, Error, InsertResult, UpdateResult


TargetSettingAddRequest: TypeAlias = list[TargetSettingAdd]
TargetSettingAddResponse: TypeAlias = InsertResult
TargetSettingAddSingleRequest: TypeAlias = TargetSettingAdd
TargetSettingAddSingleResponse: TypeAlias = InsertResult
TargetSettingDeleteRequest: TypeAlias = Base_ID
TargetSettingDeleteResponse: TypeAlias = UpdateResult
TargetSettingGetRequest: TypeAlias = TargetSettingGet
TargetSettingGetResponse: TypeAlias = TargetSettingRegosArrayResult


_MODEL_NAMES = ['TargetSetting', 'TargetSettingAdd', 'TargetSettingGet', 'TargetSettingRegosArrayResult']


__all__ = [
    'TargetSetting',
    'TargetSettingAdd',
    'TargetSettingGet',
    'TargetSettingRegosArrayResult',
    'TargetSettingTypeEnum',
    'TargetSettingGetRequest',
    'TargetSettingGetResponse',
    'TargetSettingAddSingleRequest',
    'TargetSettingAddSingleResponse',
    'TargetSettingAddRequest',
    'TargetSettingAddResponse',
    'TargetSettingDeleteRequest',
    'TargetSettingDeleteResponse'
]

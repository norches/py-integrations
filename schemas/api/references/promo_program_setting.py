"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PromoProgramSetting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    program_id: int | None = PydField(default=None)
    program_type_id: int | None = PydField(default=None)
    type: PromoProgramSettingType | None = PydField(default=None)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PromoProgramSettingAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    program_id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)


class PromoProgramSettingArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PromoProgramSetting] | Error | None = PydField(default=None)


class PromoProgramSettingDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PromoProgramSettingEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)


class PromoProgramSettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    type_ids: list[int] | None = PydField(default=None)
    program_id: int | None = PydField(default=None)
    program_ids: list[int] | None = PydField(default=None)
    key: str | None = PydField(default=None)


class PromoProgramSettingType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


PromoProgramSettingAddRequest: TypeAlias = list[PromoProgramSettingAdd]
PromoProgramSettingAddResponse: TypeAlias = InsertResult
PromoProgramSettingAddSingleRequest: TypeAlias = PromoProgramSettingAdd
PromoProgramSettingAddSingleResponse: TypeAlias = InsertResult
PromoProgramSettingDeleteRequest: TypeAlias = PromoProgramSettingDelete
PromoProgramSettingDeleteResponse: TypeAlias = UpdateResult
PromoProgramSettingEditRequest: TypeAlias = list[PromoProgramSettingEdit]
PromoProgramSettingEditResponse: TypeAlias = UpdateResult
PromoProgramSettingGetRequest: TypeAlias = PromoProgramSettingGet
PromoProgramSettingGetResponse: TypeAlias = PromoProgramSettingArrayRegosObjectResult


_MODEL_NAMES = ['PromoProgramSetting', 'PromoProgramSettingAdd', 'PromoProgramSettingArrayRegosObjectResult', 'PromoProgramSettingDelete', 'PromoProgramSettingEdit', 'PromoProgramSettingGet']


__all__ = [
    'PromoProgramSetting',
    'PromoProgramSettingAdd',
    'PromoProgramSettingArrayRegosObjectResult',
    'PromoProgramSettingDelete',
    'PromoProgramSettingEdit',
    'PromoProgramSettingGet',
    'PromoProgramSettingType',
    'PromoProgramSettingGetRequest',
    'PromoProgramSettingGetResponse',
    'PromoProgramSettingAddSingleRequest',
    'PromoProgramSettingAddSingleResponse',
    'PromoProgramSettingAddRequest',
    'PromoProgramSettingAddResponse',
    'PromoProgramSettingEditRequest',
    'PromoProgramSettingEditResponse',
    'PromoProgramSettingDeleteRequest',
    'PromoProgramSettingDeleteResponse'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ApplicationSetting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    app_id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    dataType: DataType | None = PydField(default=None)
    default_value: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    system: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ApplicationSettingAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    app_id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    dataType: DataType | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    default_value: str | None = PydField(default=None)


class ApplicationSettingArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ApplicationSetting] | Error | None = PydField(default=None)


class ApplicationSettingDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    app_id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)


class ApplicationSettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    app_id: int | None = PydField(default=None)
    keys: list[str] | None = PydField(default=None)


class ApplicationSettingValue(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    dataType: DataType | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ApplicationSettingValueArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ApplicationSettingValue] | Error | None = PydField(default=None)


class ApplicationSettingValuesEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    app_id: int | None = PydField(default=None)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)


class ApplicationSettingValuesGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    app_id: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    keys: list[str] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DataType, Error, InsertResult, UpdateResult


ApplicationSettingAddRequest: TypeAlias = ApplicationSettingAdd
ApplicationSettingAddResponse: TypeAlias = InsertResult
ApplicationSettingDeleteRequest: TypeAlias = ApplicationSettingDelete
ApplicationSettingDeleteResponse: TypeAlias = UpdateResult
ApplicationSettingEditValuesRequest: TypeAlias = list[ApplicationSettingValuesEdit]
ApplicationSettingEditValuesResponse: TypeAlias = UpdateResult
ApplicationSettingGetRequest: TypeAlias = ApplicationSettingGet
ApplicationSettingGetResponse: TypeAlias = ApplicationSettingArrayRegosObjectResult
ApplicationSettingGetValuesRequest: TypeAlias = ApplicationSettingValuesGet
ApplicationSettingGetValuesResponse: TypeAlias = ApplicationSettingValueArrayRegosObjectResult


_MODEL_NAMES = ['ApplicationSetting', 'ApplicationSettingAdd', 'ApplicationSettingArrayRegosObjectResult', 'ApplicationSettingDelete', 'ApplicationSettingGet', 'ApplicationSettingValue', 'ApplicationSettingValueArrayRegosObjectResult', 'ApplicationSettingValuesEdit', 'ApplicationSettingValuesGet']


__all__ = [
    'ApplicationSetting',
    'ApplicationSettingAdd',
    'ApplicationSettingArrayRegosObjectResult',
    'ApplicationSettingDelete',
    'ApplicationSettingGet',
    'ApplicationSettingValue',
    'ApplicationSettingValueArrayRegosObjectResult',
    'ApplicationSettingValuesEdit',
    'ApplicationSettingValuesGet',
    'ApplicationSettingGetValuesRequest',
    'ApplicationSettingGetValuesResponse',
    'ApplicationSettingEditValuesRequest',
    'ApplicationSettingEditValuesResponse',
    'ApplicationSettingAddRequest',
    'ApplicationSettingAddResponse',
    'ApplicationSettingGetRequest',
    'ApplicationSettingGetResponse',
    'ApplicationSettingDeleteRequest',
    'ApplicationSettingDeleteResponse'
]

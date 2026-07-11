"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class SysConfig(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    dataType: DataType | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class SysConfigArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[SysConfig] | Error | None = PydField(default=None)


class SysConfigEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)


class SysConfigGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DataType, Error, UpdateResult


SysConfigEditRequest: TypeAlias = list[SysConfigEdit]
SysConfigEditResponse: TypeAlias = UpdateResult
SysConfigGetRequest: TypeAlias = SysConfigGet
SysConfigGetResponse: TypeAlias = SysConfigArrayRegosObjectResult


_MODEL_NAMES = ['SysConfig', 'SysConfigArrayRegosObjectResult', 'SysConfigEdit', 'SysConfigGet']


__all__ = [
    'SysConfig',
    'SysConfigArrayRegosObjectResult',
    'SysConfigEdit',
    'SysConfigGet',
    'SysConfigGetRequest',
    'SysConfigGetResponse',
    'SysConfigEditRequest',
    'SysConfigEditResponse'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Storage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    capacity: int | None = PydField(default=None)
    used: int | None = PydField(default=None)
    free: int | None = PydField(default=None)
    entities: list[StorageEntity] | None = PydField(default=None)


class StorageCleanup(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    entities: list[StorageEntityEnum] | None = PydField(default=None)


class StorageEntity(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    entity: StorageEntityEnum | None = PydField(default=None)
    used: int | None = PydField(default=None)


class StorageEntityEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class StorageGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    pass


class StorageRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Storage | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BooleanRegosObjectResult, Error


StorageCleanupRequest: TypeAlias = StorageCleanup
StorageCleanupResponse: TypeAlias = BooleanRegosObjectResult
StorageGetRequest: TypeAlias = StorageGet
StorageGetResponse: TypeAlias = StorageRegosObjectResult


_MODEL_NAMES = ['Storage', 'StorageCleanup', 'StorageEntity', 'StorageGet', 'StorageRegosObjectResult']


__all__ = [
    'Storage',
    'StorageCleanup',
    'StorageEntity',
    'StorageEntityEnum',
    'StorageGet',
    'StorageRegosObjectResult',
    'StorageGetRequest',
    'StorageGetResponse',
    'StorageCleanupRequest',
    'StorageCleanupResponse'
]

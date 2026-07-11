"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class CommonFileDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class CommonFileEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)
    folder_id: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    duration_ms: int | None = PydField(default=None)


class CommonFileGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    folder_id: int | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)


class CommonFileRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CommonFile] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseSortColumn, CommonFile, CommonFileAccessLevelEnum, Error, InsertResult, UpdateResult


FileAddResponse: TypeAlias = InsertResult
FileDeleteRequest: TypeAlias = CommonFileDelete
FileDeleteResponse: TypeAlias = UpdateResult
FileEditRequest: TypeAlias = CommonFileEdit
FileEditResponse: TypeAlias = UpdateResult
FileGetRequest: TypeAlias = CommonFileGet
FileGetResponse: TypeAlias = CommonFileRegosOffsettedArrayResult


_MODEL_NAMES = ['CommonFileDelete', 'CommonFileEdit', 'CommonFileGet', 'CommonFileRegosOffsettedArrayResult']


__all__ = [
    'CommonFileDelete',
    'CommonFileEdit',
    'CommonFileGet',
    'CommonFileRegosOffsettedArrayResult',
    'FileGetRequest',
    'FileGetResponse',
    'FileAddResponse',
    'FileEditRequest',
    'FileEditResponse',
    'FileDeleteRequest',
    'FileDeleteResponse'
]

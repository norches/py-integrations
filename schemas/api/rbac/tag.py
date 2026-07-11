"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Tag(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    data: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TagAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    data: str | None = PydField(default=None)


class TagDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class TagEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    data: str | None = PydField(default=None)


class TagGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)


class TagRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Tag] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


TagAddRequest: TypeAlias = TagAdd
TagAddResponse: TypeAlias = InsertResult
TagDeleteRequest: TypeAlias = TagDelete
TagDeleteResponse: TypeAlias = UpdateResult
TagEditRequest: TypeAlias = TagEdit
TagEditResponse: TypeAlias = UpdateResult
TagGetRequest: TypeAlias = TagGet
TagGetResponse: TypeAlias = TagRegosArrayResult


_MODEL_NAMES = ['Tag', 'TagAdd', 'TagDelete', 'TagEdit', 'TagGet', 'TagRegosArrayResult']


__all__ = [
    'Tag',
    'TagAdd',
    'TagDelete',
    'TagEdit',
    'TagGet',
    'TagRegosArrayResult',
    'TagGetRequest',
    'TagGetResponse',
    'TagAddRequest',
    'TagAddResponse',
    'TagEditRequest',
    'TagEditResponse',
    'TagDeleteRequest',
    'TagDeleteResponse'
]

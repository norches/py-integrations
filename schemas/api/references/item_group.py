"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ItemGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    path: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    child_count: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ItemGroupAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class ItemGroupArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemGroup] | Error | None = PydField(default=None)


class ItemGroupDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ItemGroupEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class ItemGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)
    name: str | None = PydField(default=None)
    path: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


ItemGroupAddRequest: TypeAlias = ItemGroupAdd
ItemGroupAddResponse: TypeAlias = InsertResult
ItemGroupDeleteRequest: TypeAlias = ItemGroupDelete
ItemGroupDeleteResponse: TypeAlias = UpdateResult
ItemGroupEditRequest: TypeAlias = ItemGroupEdit
ItemGroupEditResponse: TypeAlias = UpdateResult
ItemGroupGetRequest: TypeAlias = ItemGroupGet
ItemGroupGetResponse: TypeAlias = ItemGroupArrayRegosObjectResult


_MODEL_NAMES = ['ItemGroup', 'ItemGroupAdd', 'ItemGroupArrayRegosObjectResult', 'ItemGroupDelete', 'ItemGroupEdit', 'ItemGroupGet']


__all__ = [
    'ItemGroup',
    'ItemGroupAdd',
    'ItemGroupArrayRegosObjectResult',
    'ItemGroupDelete',
    'ItemGroupEdit',
    'ItemGroupGet',
    'ItemGroupGetRequest',
    'ItemGroupGetResponse',
    'ItemGroupAddRequest',
    'ItemGroupAddResponse',
    'ItemGroupEditRequest',
    'ItemGroupEditResponse',
    'ItemGroupDeleteRequest',
    'ItemGroupDeleteResponse'
]

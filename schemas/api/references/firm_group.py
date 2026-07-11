"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class FirmGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    child_count: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class FirmGroupAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class FirmGroupArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[FirmGroup] | Error | None = PydField(default=None)


class FirmGroupDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class FirmGroupEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class FirmGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


FirmGroupAddRequest: TypeAlias = FirmGroupAdd
FirmGroupAddResponse: TypeAlias = InsertResult
FirmGroupDeleteRequest: TypeAlias = FirmGroupDelete
FirmGroupDeleteResponse: TypeAlias = UpdateResult
FirmGroupEditRequest: TypeAlias = FirmGroupEdit
FirmGroupEditResponse: TypeAlias = UpdateResult
FirmGroupGetRequest: TypeAlias = FirmGroupGet
FirmGroupGetResponse: TypeAlias = FirmGroupArrayRegosObjectResult


_MODEL_NAMES = ['FirmGroup', 'FirmGroupAdd', 'FirmGroupArrayRegosObjectResult', 'FirmGroupDelete', 'FirmGroupEdit', 'FirmGroupGet']


__all__ = [
    'FirmGroup',
    'FirmGroupAdd',
    'FirmGroupArrayRegosObjectResult',
    'FirmGroupDelete',
    'FirmGroupEdit',
    'FirmGroupGet',
    'FirmGroupGetRequest',
    'FirmGroupGetResponse',
    'FirmGroupAddRequest',
    'FirmGroupAddResponse',
    'FirmGroupEditRequest',
    'FirmGroupEditResponse',
    'FirmGroupDeleteRequest',
    'FirmGroupDeleteResponse'
]

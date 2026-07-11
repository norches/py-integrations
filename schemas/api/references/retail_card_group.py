"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailCardGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    child_count: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailCardGroupAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class RetailCardGroupArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCardGroup] | Error | None = PydField(default=None)


class RetailCardGroupDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class RetailCardGroupEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class RetailCardGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


RetailCardGroupAddRequest: TypeAlias = RetailCardGroupAdd
RetailCardGroupAddResponse: TypeAlias = InsertResult
RetailCardGroupDeleteRequest: TypeAlias = RetailCardGroupDelete
RetailCardGroupDeleteResponse: TypeAlias = UpdateResult
RetailCardGroupEditRequest: TypeAlias = RetailCardGroupEdit
RetailCardGroupEditResponse: TypeAlias = UpdateResult
RetailCardGroupGetRequest: TypeAlias = RetailCardGroupGet
RetailCardGroupGetResponse: TypeAlias = RetailCardGroupArrayRegosObjectResult


_MODEL_NAMES = ['RetailCardGroup', 'RetailCardGroupAdd', 'RetailCardGroupArrayRegosObjectResult', 'RetailCardGroupDelete', 'RetailCardGroupEdit', 'RetailCardGroupGet']


__all__ = [
    'RetailCardGroup',
    'RetailCardGroupAdd',
    'RetailCardGroupArrayRegosObjectResult',
    'RetailCardGroupDelete',
    'RetailCardGroupEdit',
    'RetailCardGroupGet',
    'RetailCardGroupGetRequest',
    'RetailCardGroupGetResponse',
    'RetailCardGroupAddRequest',
    'RetailCardGroupAddResponse',
    'RetailCardGroupEditRequest',
    'RetailCardGroupEditResponse',
    'RetailCardGroupDeleteRequest',
    'RetailCardGroupDeleteResponse'
]

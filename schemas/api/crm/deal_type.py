"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DealType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DealTypeAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class DealTypeDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DealTypeEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class DealTypeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DealTypeRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DealType] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


DealTypeAddRequest: TypeAlias = DealTypeAdd
DealTypeAddResponse: TypeAlias = InsertResult
DealTypeDeleteRequest: TypeAlias = DealTypeDelete
DealTypeDeleteResponse: TypeAlias = UpdateResult
DealTypeEditRequest: TypeAlias = DealTypeEdit
DealTypeEditResponse: TypeAlias = UpdateResult
DealTypeGetRequest: TypeAlias = DealTypeGet
DealTypeGetResponse: TypeAlias = DealTypeRegosOffsettedArrayResult


_MODEL_NAMES = ['DealType', 'DealTypeAdd', 'DealTypeDelete', 'DealTypeEdit', 'DealTypeGet', 'DealTypeRegosOffsettedArrayResult']


__all__ = [
    'DealType',
    'DealTypeAdd',
    'DealTypeDelete',
    'DealTypeEdit',
    'DealTypeGet',
    'DealTypeRegosOffsettedArrayResult',
    'DealTypeGetRequest',
    'DealTypeGetResponse',
    'DealTypeAddRequest',
    'DealTypeAddResponse',
    'DealTypeEditRequest',
    'DealTypeEditResponse',
    'DealTypeDeleteRequest',
    'DealTypeDeleteResponse'
]

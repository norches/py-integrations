"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class QuickReply(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    text: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class QuickReplyAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    text: str | None = PydField(default=None)


class QuickReplyDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class QuickReplyGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class QuickReplyRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[QuickReply] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


QuickReplyAddRequest: TypeAlias = QuickReplyAdd
QuickReplyAddResponse: TypeAlias = InsertResult
QuickReplyDeleteRequest: TypeAlias = QuickReplyDelete
QuickReplyDeleteResponse: TypeAlias = UpdateResult
QuickReplyGetRequest: TypeAlias = QuickReplyGet
QuickReplyGetResponse: TypeAlias = QuickReplyRegosOffsettedArrayResult


_MODEL_NAMES = ['QuickReply', 'QuickReplyAdd', 'QuickReplyDelete', 'QuickReplyGet', 'QuickReplyRegosOffsettedArrayResult']


__all__ = [
    'QuickReply',
    'QuickReplyAdd',
    'QuickReplyDelete',
    'QuickReplyGet',
    'QuickReplyRegosOffsettedArrayResult',
    'QuickReplyGetRequest',
    'QuickReplyGetResponse',
    'QuickReplyAddRequest',
    'QuickReplyAddResponse',
    'QuickReplyDeleteRequest',
    'QuickReplyDeleteResponse'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocEnumerator(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    table_name: str | None = PydField(default=None)
    mask: str | None = PydField(default=None)
    counter: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocEnumeratorEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    mask: str | None = PydField(default=None)


class DocEnumeratorGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    table_ids: list[int] | None = PydField(default=None)


class DocEnumeratorRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocEnumerator] | Error | None = PydField(default=None)


class DocEnumeratorReset(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, UpdateResult


DocumentEnumeratorEditRequest: TypeAlias = DocEnumeratorEdit
DocumentEnumeratorEditResponse: TypeAlias = UpdateResult
DocumentEnumeratorGetRequest: TypeAlias = DocEnumeratorGet
DocumentEnumeratorGetResponse: TypeAlias = DocEnumeratorRegosArrayResult
DocumentEnumeratorResetRequest: TypeAlias = DocEnumeratorReset
DocumentEnumeratorResetResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocEnumerator', 'DocEnumeratorEdit', 'DocEnumeratorGet', 'DocEnumeratorRegosArrayResult', 'DocEnumeratorReset']


__all__ = [
    'DocEnumerator',
    'DocEnumeratorEdit',
    'DocEnumeratorGet',
    'DocEnumeratorRegosArrayResult',
    'DocEnumeratorReset',
    'DocumentEnumeratorGetRequest',
    'DocumentEnumeratorGetResponse',
    'DocumentEnumeratorEditRequest',
    'DocumentEnumeratorEditResponse',
    'DocumentEnumeratorResetRequest',
    'DocumentEnumeratorResetResponse'
]

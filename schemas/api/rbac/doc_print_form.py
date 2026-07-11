"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocPrintForm(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    data: str | None = PydField(default=None)
    version: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocPrintFormDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocPrintFormGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)
    version: int | None = PydField(default=None)


class DocPrintFormPrepare(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    print_form_type_id: int | None = PydField(default=None)
    data: Any = PydField(default=None)
    version: int | None = PydField(default=None)


class DocPrintFormPreparedFile(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    file_name: str | None = PydField(default=None)
    data: str | None = PydField(default=None)
    version: int | None = PydField(default=None)


class DocPrintFormPreparedFileRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: DocPrintFormPreparedFile | Error | None = PydField(default=None)


class DocPrintFormRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocPrintForm] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


DocPrintFormAddResponse: TypeAlias = InsertResult
DocPrintFormDeleteRequest: TypeAlias = DocPrintFormDelete
DocPrintFormDeleteResponse: TypeAlias = UpdateResult
DocPrintFormEditResponse: TypeAlias = UpdateResult
DocPrintFormGetRequest: TypeAlias = DocPrintFormGet
DocPrintFormGetResponse: TypeAlias = DocPrintFormRegosArrayResult
DocPrintFormPrepareRequest: TypeAlias = DocPrintFormPrepare
DocPrintFormPrepareResponse: TypeAlias = DocPrintFormPreparedFileRegosObjectResult


_MODEL_NAMES = ['DocPrintForm', 'DocPrintFormDelete', 'DocPrintFormGet', 'DocPrintFormPrepare', 'DocPrintFormPreparedFile', 'DocPrintFormPreparedFileRegosObjectResult', 'DocPrintFormRegosArrayResult']


__all__ = [
    'DocPrintForm',
    'DocPrintFormDelete',
    'DocPrintFormGet',
    'DocPrintFormPrepare',
    'DocPrintFormPreparedFile',
    'DocPrintFormPreparedFileRegosObjectResult',
    'DocPrintFormRegosArrayResult',
    'DocPrintFormGetRequest',
    'DocPrintFormGetResponse',
    'DocPrintFormPrepareRequest',
    'DocPrintFormPrepareResponse',
    'DocPrintFormAddResponse',
    'DocPrintFormEditResponse',
    'DocPrintFormDeleteRequest',
    'DocPrintFormDeleteResponse'
]

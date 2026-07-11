"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocContractFile(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    file: CommonFile | None = PydField(default=None)


class DocContractFileDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocContractFileGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    file_ids: list[int] | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)


class DocContractFileRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocContractFile] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CommonFile, Error, InsertResult, UpdateResult


DocContractFileAddResponse: TypeAlias = InsertResult
DocContractFileDeleteRequest: TypeAlias = DocContractFileDelete
DocContractFileDeleteResponse: TypeAlias = UpdateResult
DocContractFileGetRequest: TypeAlias = DocContractFileGet
DocContractFileGetResponse: TypeAlias = DocContractFileRegosArrayResult


_MODEL_NAMES = ['DocContractFile', 'DocContractFileDelete', 'DocContractFileGet', 'DocContractFileRegosArrayResult']


__all__ = [
    'DocContractFile',
    'DocContractFileDelete',
    'DocContractFileGet',
    'DocContractFileRegosArrayResult',
    'DocContractFileGetRequest',
    'DocContractFileGetResponse',
    'DocContractFileAddResponse',
    'DocContractFileDeleteRequest',
    'DocContractFileDeleteResponse'
]

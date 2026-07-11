"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PrintFormType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    type: DocumentType | None = PydField(default=None)
    printform: DocPrintForm | None = PydField(default=None)
    version: int | None = PydField(default=None)


class PrintFormTypeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    type_ids: list[int] | None = PydField(default=None)
    printform_ids: list[int] | None = PydField(default=None)
    version: int | None = PydField(default=None)


class PrintFormTypeRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PrintFormType] | Error | None = PydField(default=None)


class PrintFormTypeRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PrintFormTypeSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type_id: int | None = PydField(default=None)
    printform_id: int | None = PydField(default=None)
    version: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.docs.document_type import DocumentType
from schemas.api.rbac.doc_print_form import DocPrintForm


PrintFormTypeGetRequest: TypeAlias = PrintFormTypeGet
PrintFormTypeGetResponse: TypeAlias = PrintFormTypeRegosArrayResult
PrintFormTypeRemoveRequest: TypeAlias = PrintFormTypeRemove
PrintFormTypeRemoveResponse: TypeAlias = UpdateResult
PrintFormTypeSetRequest: TypeAlias = PrintFormTypeSet
PrintFormTypeSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['PrintFormType', 'PrintFormTypeGet', 'PrintFormTypeRegosArrayResult', 'PrintFormTypeRemove', 'PrintFormTypeSet']


__all__ = [
    'PrintFormType',
    'PrintFormTypeGet',
    'PrintFormTypeRegosArrayResult',
    'PrintFormTypeRemove',
    'PrintFormTypeSet',
    'PrintFormTypeGetRequest',
    'PrintFormTypeGetResponse',
    'PrintFormTypeSetRequest',
    'PrintFormTypeSetResponse',
    'PrintFormTypeRemoveRequest',
    'PrintFormTypeRemoveResponse'
]

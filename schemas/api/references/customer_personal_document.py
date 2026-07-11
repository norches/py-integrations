"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class CustomerPersonalDocument(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    personal_doc_type: PersonalDocType | None = PydField(default=None)
    file: CommonFile | None = PydField(default=None)
    value: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CustomerPersonalDocumentDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    personal_doc_type_id: int | None = PydField(default=None)


class CustomerPersonalDocumentGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    personal_doc_type_id: int | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)


class CustomerPersonalDocumentRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CustomerPersonalDocument] | Error | None = PydField(default=None)


class CustomerPersonalDocumentRemoveFile(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    personal_doc_type_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CommonFile, Error, InsertResult, UpdateResult
from schemas.api.references.personal_doc_type import PersonalDocType


CustomerPersonalDocumentAddResponse: TypeAlias = InsertResult
CustomerPersonalDocumentDeleteRequest: TypeAlias = CustomerPersonalDocumentDelete
CustomerPersonalDocumentDeleteResponse: TypeAlias = UpdateResult
CustomerPersonalDocumentEditResponse: TypeAlias = UpdateResult
CustomerPersonalDocumentGetRequest: TypeAlias = CustomerPersonalDocumentGet
CustomerPersonalDocumentGetResponse: TypeAlias = CustomerPersonalDocumentRegosArrayResult
CustomerPersonalDocumentRemoveFileRequest: TypeAlias = CustomerPersonalDocumentRemoveFile
CustomerPersonalDocumentRemoveFileResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['CustomerPersonalDocument', 'CustomerPersonalDocumentDelete', 'CustomerPersonalDocumentGet', 'CustomerPersonalDocumentRegosArrayResult', 'CustomerPersonalDocumentRemoveFile']


__all__ = [
    'CustomerPersonalDocument',
    'CustomerPersonalDocumentDelete',
    'CustomerPersonalDocumentGet',
    'CustomerPersonalDocumentRegosArrayResult',
    'CustomerPersonalDocumentRemoveFile',
    'CustomerPersonalDocumentGetRequest',
    'CustomerPersonalDocumentGetResponse',
    'CustomerPersonalDocumentAddResponse',
    'CustomerPersonalDocumentEditResponse',
    'CustomerPersonalDocumentRemoveFileRequest',
    'CustomerPersonalDocumentRemoveFileResponse',
    'CustomerPersonalDocumentDeleteRequest',
    'CustomerPersonalDocumentDeleteResponse'
]

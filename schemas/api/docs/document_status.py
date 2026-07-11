"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocumentStatus(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_type_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    order: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocumentStatusGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_type_id: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)


class DocumentStatusRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocumentStatus] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error


DocumentStatusGetRequest: TypeAlias = DocumentStatusGet
DocumentStatusGetResponse: TypeAlias = DocumentStatusRegosArrayResult


_MODEL_NAMES = ['DocumentStatus', 'DocumentStatusGet', 'DocumentStatusRegosArrayResult']


__all__ = [
    'DocumentStatus',
    'DocumentStatusGet',
    'DocumentStatusRegosArrayResult',
    'DocumentStatusGetRequest',
    'DocumentStatusGetResponse'
]

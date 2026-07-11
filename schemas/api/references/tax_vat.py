"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class TaxVat(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    name: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TaxVatAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    value: _Decimal | None = PydField(default=None)
    name: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class TaxVatDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class TaxVatEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    name: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class TaxVatGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class TaxVatRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[TaxVat] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


TaxVatAddRequest: TypeAlias = TaxVatAdd
TaxVatAddResponse: TypeAlias = InsertResult
TaxVatDeleteRequest: TypeAlias = TaxVatDelete
TaxVatDeleteResponse: TypeAlias = UpdateResult
TaxVatEditRequest: TypeAlias = TaxVatEdit
TaxVatEditResponse: TypeAlias = UpdateResult
TaxVatGetRequest: TypeAlias = TaxVatGet
TaxVatGetResponse: TypeAlias = TaxVatRegosArrayResult


_MODEL_NAMES = ['TaxVat', 'TaxVatAdd', 'TaxVatDelete', 'TaxVatEdit', 'TaxVatGet', 'TaxVatRegosArrayResult']


__all__ = [
    'TaxVat',
    'TaxVatAdd',
    'TaxVatDelete',
    'TaxVatEdit',
    'TaxVatGet',
    'TaxVatRegosArrayResult',
    'TaxVatGetRequest',
    'TaxVatGetResponse',
    'TaxVatAddRequest',
    'TaxVatAddResponse',
    'TaxVatEditRequest',
    'TaxVatEditResponse',
    'TaxVatDeleteRequest',
    'TaxVatDeleteResponse'
]

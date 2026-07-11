"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Barcode(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    barcode_type: BarcodeType | None = PydField(default=None)
    value: str | None = PydField(default=None)
    base_: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class BarcodeAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    barcode_type_id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)
    forced: bool | None = PydField(default=None)


class BarcodeAddEAN13(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)


class BarcodeArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Barcode] | Error | None = PydField(default=None)


class BarcodeDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class BarcodeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    value: str | None = PydField(default=None)


class Barcode_SetBase(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)


class EAN13(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    value: int | None = PydField(default=None)


class EAN13RegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: EAN13 | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.references.barcode_type import BarcodeType


BarcodeAddEan13Request: TypeAlias = BarcodeAddEAN13
BarcodeAddEan13Response: TypeAlias = InsertResult
BarcodeAddRequest: TypeAlias = BarcodeAdd
BarcodeAddResponse: TypeAlias = InsertResult
BarcodeDeleteRequest: TypeAlias = BarcodeDelete
BarcodeDeleteResponse: TypeAlias = UpdateResult
BarcodeFillEmptyBarcodeItemsResponse: TypeAlias = UpdateResult
BarcodeGenerateEan13Response: TypeAlias = EAN13RegosObjectResult
BarcodeGetRequest: TypeAlias = BarcodeGet
BarcodeGetResponse: TypeAlias = BarcodeArrayRegosObjectResult
BarcodeSetBaseRequest: TypeAlias = Barcode_SetBase
BarcodeSetBaseResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Barcode', 'BarcodeAdd', 'BarcodeAddEAN13', 'BarcodeArrayRegosObjectResult', 'BarcodeDelete', 'BarcodeGet', 'Barcode_SetBase', 'EAN13', 'EAN13RegosObjectResult']


__all__ = [
    'Barcode',
    'BarcodeAdd',
    'BarcodeAddEAN13',
    'BarcodeArrayRegosObjectResult',
    'BarcodeDelete',
    'BarcodeGet',
    'Barcode_SetBase',
    'EAN13',
    'EAN13RegosObjectResult',
    'BarcodeGetRequest',
    'BarcodeGetResponse',
    'BarcodeAddRequest',
    'BarcodeAddResponse',
    'BarcodeAddEan13Request',
    'BarcodeAddEan13Response',
    'BarcodeSetBaseRequest',
    'BarcodeSetBaseResponse',
    'BarcodeDeleteRequest',
    'BarcodeDeleteResponse',
    'BarcodeGenerateEan13Response',
    'BarcodeFillEmptyBarcodeItemsResponse'
]

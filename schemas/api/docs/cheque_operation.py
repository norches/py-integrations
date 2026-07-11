"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ChequePosition(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    document_uuid: str | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    order_opr_id: int | None = PydField(default=None)
    order_opr_quantity: _Decimal | None = PydField(default=None)
    uuid: str | None = PydField(default=None)
    has_storno: bool | None = PydField(default=None)
    storno_uuid: str | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    order: int | None = PydField(default=None)
    sort_order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    label: str | None = PydField(default=None)
    barcode: str | None = PydField(default=None)


class ChequePositionAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    label: str | None = PydField(default=None)


class ChequePositionArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChequePosition] | Error | None = PydField(default=None)


class ChequePositionGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuids: list[str] | None = PydField(default=None)
    exclude_storno: bool | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)


class ChequePosition_AddByBarcode(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_uuid: str | None = PydField(default=None)
    barcode: str | None = PydField(default=None)


class ChequePosition_Storno(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)


class ChequePostion_Edit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    label: str | None = PydField(default=None)


class Cheque_SetRowPercentDiscount(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    percent: _Decimal | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, Insert_uuid_Result, UpdateResult
from schemas.api.references.item import Item


ChequeOperationAddByBarcodeRequest: TypeAlias = ChequePosition_AddByBarcode
ChequeOperationAddByBarcodeResponse: TypeAlias = Insert_uuid_Result
ChequeOperationAddRequest: TypeAlias = ChequePositionAdd
ChequeOperationAddResponse: TypeAlias = Insert_uuid_Result
ChequeOperationEditRequest: TypeAlias = ChequePostion_Edit
ChequeOperationEditResponse: TypeAlias = UpdateResult
ChequeOperationGetRequest: TypeAlias = ChequePositionGet
ChequeOperationGetResponse: TypeAlias = ChequePositionArrayRegosObjectResult
ChequeOperationSetPercentDiscountRequest: TypeAlias = Cheque_SetRowPercentDiscount
ChequeOperationSetPercentDiscountResponse: TypeAlias = UpdateResult
ChequeOperationStornoRequest: TypeAlias = ChequePosition_Storno
ChequeOperationStornoResponse: TypeAlias = UpdateResult
DocChequeOperation: TypeAlias = ChequePosition
DocChequeOperationGetRequest: TypeAlias = ChequePositionGet
DocChequeOperationGetResponse: TypeAlias = ChequePositionArrayRegosObjectResult


_MODEL_NAMES = ['ChequePosition', 'ChequePositionAdd', 'ChequePositionArrayRegosObjectResult', 'ChequePositionGet', 'ChequePosition_AddByBarcode', 'ChequePosition_Storno', 'ChequePostion_Edit', 'Cheque_SetRowPercentDiscount']


__all__ = [
    'ChequePosition',
    'ChequePositionAdd',
    'ChequePositionArrayRegosObjectResult',
    'ChequePositionGet',
    'ChequePosition_AddByBarcode',
    'ChequePosition_Storno',
    'ChequePostion_Edit',
    'Cheque_SetRowPercentDiscount',
    'ChequeOperationGetRequest',
    'ChequeOperationGetResponse',
    'ChequeOperationAddRequest',
    'ChequeOperationAddResponse',
    'ChequeOperationAddByBarcodeRequest',
    'ChequeOperationAddByBarcodeResponse',
    'ChequeOperationEditRequest',
    'ChequeOperationEditResponse',
    'ChequeOperationStornoRequest',
    'ChequeOperationStornoResponse',
    'ChequeOperationSetPercentDiscountRequest',
    'ChequeOperationSetPercentDiscountResponse',
    'DocChequeOperation',
    'DocChequeOperationGetRequest',
    'DocChequeOperationGetResponse'
]

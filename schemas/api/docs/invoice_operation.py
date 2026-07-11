"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class InvoiceOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    total: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_amount: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class InvoiceOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)


class InvoiceOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class InvoiceOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)


class InvoiceOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class InvoiceOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[InvoiceOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class InvoiceRoamingOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    name: str | None = PydField(default=None)
    icps: str | None = PydField(default=None)
    barcode: str | None = PydField(default=None)
    package_code: str | None = PydField(default=None)
    package_name: str | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    labels: list[str] | None = PydField(default=None)
    group_labels: list[str] | None = PydField(default=None)
    transport_labels: list[str] | None = PydField(default=None)
    origin: int | None = PydField(default=None)
    vat_rate: int | None = PydField(default=None)


class InvoiceRoamingOperationArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[InvoiceRoamingOperation] | Error | None = PydField(default=None)


class InvoiceRoamingOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsMovement, Error, SetPriceByPriceType_Model, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


InvoiceOperationAddRequest: TypeAlias = list[InvoiceOperationAdd]
InvoiceOperationAddResponse: TypeAlias = UpdateResult
InvoiceOperationDeleteRequest: TypeAlias = list[InvoiceOperationDelete]
InvoiceOperationDeleteResponse: TypeAlias = UpdateResult
InvoiceOperationEditRequest: TypeAlias = list[InvoiceOperationEdit]
InvoiceOperationEditResponse: TypeAlias = UpdateResult
InvoiceOperationGetOperationsFromRoamingRequest: TypeAlias = InvoiceRoamingOperationGet
InvoiceOperationGetOperationsFromRoamingResponse: TypeAlias = InvoiceRoamingOperationArrayRegosObjectResult
InvoiceOperationGetRequest: TypeAlias = InvoiceOperationGet
InvoiceOperationGetResponse: TypeAlias = InvoiceOperationRegosOffsettedArrayResult
InvoiceOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
InvoiceOperationMoveOperationsResponse: TypeAlias = UpdateResult
InvoiceOperationSetPriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
InvoiceOperationSetPriceByPriceTypeResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['InvoiceOperation', 'InvoiceOperationAdd', 'InvoiceOperationDelete', 'InvoiceOperationEdit', 'InvoiceOperationGet', 'InvoiceOperationRegosOffsettedArrayResult', 'InvoiceRoamingOperation', 'InvoiceRoamingOperationArrayRegosObjectResult', 'InvoiceRoamingOperationGet']


__all__ = [
    'InvoiceOperation',
    'InvoiceOperationAdd',
    'InvoiceOperationDelete',
    'InvoiceOperationEdit',
    'InvoiceOperationGet',
    'InvoiceOperationRegosOffsettedArrayResult',
    'InvoiceRoamingOperation',
    'InvoiceRoamingOperationArrayRegosObjectResult',
    'InvoiceRoamingOperationGet',
    'InvoiceOperationGetRequest',
    'InvoiceOperationGetResponse',
    'InvoiceOperationAddRequest',
    'InvoiceOperationAddResponse',
    'InvoiceOperationEditRequest',
    'InvoiceOperationEditResponse',
    'InvoiceOperationDeleteRequest',
    'InvoiceOperationDeleteResponse',
    'InvoiceOperationSetPriceByPriceTypeRequest',
    'InvoiceOperationSetPriceByPriceTypeResponse',
    'InvoiceOperationMoveOperationsRequest',
    'InvoiceOperationMoveOperationsResponse',
    'InvoiceOperationGetOperationsFromRoamingRequest',
    'InvoiceOperationGetOperationsFromRoamingResponse'
]

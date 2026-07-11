"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PurchaseOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    current_price: _Decimal | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    additional_expenses_amount: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PurchaseOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class PurchaseOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PurchaseOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    additional_expenses_amount: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class PurchaseOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class PurchaseOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PurchaseOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class SetCostByLastPurchase(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DiscountOperationAdd, DiscountOperationDelete, DiscountOperationGet, DiscountOperationRegosArrayResult, DocsOperationsCopy, DocsOperationsMovement, Error, ObjectRegosObjectResult, SetPriceByPriceType_Model, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


PurchaseOperationAddDiscountRequest: TypeAlias = DiscountOperationAdd
PurchaseOperationAddDiscountResponse: TypeAlias = UpdateResult
PurchaseOperationAddRequest: TypeAlias = list[PurchaseOperationAdd]
PurchaseOperationAddResponse: TypeAlias = UpdateResult
PurchaseOperationCopyOperationsFromDocInvoiceRequest: TypeAlias = DocsOperationsCopy
PurchaseOperationCopyOperationsFromDocInvoiceResponse: TypeAlias = ObjectRegosObjectResult
PurchaseOperationCopyOperationsFromDocOrderToPartnerRequest: TypeAlias = DocsOperationsCopy
PurchaseOperationCopyOperationsFromDocOrderToPartnerResponse: TypeAlias = ObjectRegosObjectResult
PurchaseOperationCopyOperationsFromDocWholeSaleRequest: TypeAlias = DocsOperationsCopy
PurchaseOperationCopyOperationsFromDocWholeSaleResponse: TypeAlias = ObjectRegosObjectResult
PurchaseOperationDeleteDiscountRequest: TypeAlias = DiscountOperationDelete
PurchaseOperationDeleteDiscountResponse: TypeAlias = UpdateResult
PurchaseOperationDeleteRequest: TypeAlias = list[PurchaseOperationDelete]
PurchaseOperationDeleteResponse: TypeAlias = UpdateResult
PurchaseOperationEditRequest: TypeAlias = list[PurchaseOperationEdit]
PurchaseOperationEditResponse: TypeAlias = UpdateResult
PurchaseOperationGetDiscountRequest: TypeAlias = DiscountOperationGet
PurchaseOperationGetDiscountResponse: TypeAlias = DiscountOperationRegosArrayResult
PurchaseOperationGetRequest: TypeAlias = PurchaseOperationGet
PurchaseOperationGetResponse: TypeAlias = PurchaseOperationRegosOffsettedArrayResult
PurchaseOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
PurchaseOperationMoveOperationsResponse: TypeAlias = UpdateResult
PurchaseOperationSetCostByLastPurchaseRequest: TypeAlias = SetCostByLastPurchase
PurchaseOperationSetCostByLastPurchaseResponse: TypeAlias = UpdateResult
PurchaseOperationSetPriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
PurchaseOperationSetPriceByPriceTypeResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['PurchaseOperation', 'PurchaseOperationAdd', 'PurchaseOperationDelete', 'PurchaseOperationEdit', 'PurchaseOperationGet', 'PurchaseOperationRegosOffsettedArrayResult', 'SetCostByLastPurchase']


__all__ = [
    'PurchaseOperation',
    'PurchaseOperationAdd',
    'PurchaseOperationDelete',
    'PurchaseOperationEdit',
    'PurchaseOperationGet',
    'PurchaseOperationRegosOffsettedArrayResult',
    'SetCostByLastPurchase',
    'PurchaseOperationGetRequest',
    'PurchaseOperationGetResponse',
    'PurchaseOperationAddRequest',
    'PurchaseOperationAddResponse',
    'PurchaseOperationEditRequest',
    'PurchaseOperationEditResponse',
    'PurchaseOperationDeleteRequest',
    'PurchaseOperationDeleteResponse',
    'PurchaseOperationSetCostByLastPurchaseRequest',
    'PurchaseOperationSetCostByLastPurchaseResponse',
    'PurchaseOperationSetPriceByPriceTypeRequest',
    'PurchaseOperationSetPriceByPriceTypeResponse',
    'PurchaseOperationGetDiscountRequest',
    'PurchaseOperationGetDiscountResponse',
    'PurchaseOperationAddDiscountRequest',
    'PurchaseOperationAddDiscountResponse',
    'PurchaseOperationDeleteDiscountRequest',
    'PurchaseOperationDeleteDiscountResponse',
    'PurchaseOperationMoveOperationsRequest',
    'PurchaseOperationMoveOperationsResponse',
    'PurchaseOperationCopyOperationsFromDocWholeSaleRequest',
    'PurchaseOperationCopyOperationsFromDocWholeSaleResponse',
    'PurchaseOperationCopyOperationsFromDocOrderToPartnerRequest',
    'PurchaseOperationCopyOperationsFromDocOrderToPartnerResponse',
    'PurchaseOperationCopyOperationsFromDocInvoiceRequest',
    'PurchaseOperationCopyOperationsFromDocInvoiceResponse'
]

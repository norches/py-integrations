"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class WholeSaleOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class WholeSaleOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class WholeSaleOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class WholeSaleOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class WholeSaleOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class WholeSaleOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[WholeSaleOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DiscountOperationAdd, DiscountOperationDelete, DiscountOperationGet, DiscountOperationRegosArrayResult, DocsOperationsCopy, DocsOperationsMovement, Error, SetPriceByPriceType_Model, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


WholeSaleOperationAddDiscountRequest: TypeAlias = DiscountOperationAdd
WholeSaleOperationAddDiscountResponse: TypeAlias = UpdateResult
WholeSaleOperationAddRequest: TypeAlias = list[WholeSaleOperationAdd]
WholeSaleOperationAddResponse: TypeAlias = UpdateResult
WholeSaleOperationCopyOperationsFromDocOrderFromPartnerRequest: TypeAlias = DocsOperationsCopy
WholeSaleOperationCopyOperationsFromDocOrderFromPartnerResponse: TypeAlias = UpdateResult
WholeSaleOperationCopyOperationsFromDocPurchaseRequest: TypeAlias = DocsOperationsCopy
WholeSaleOperationCopyOperationsFromDocPurchaseResponse: TypeAlias = UpdateResult
WholeSaleOperationDeleteDiscountRequest: TypeAlias = DiscountOperationDelete
WholeSaleOperationDeleteDiscountResponse: TypeAlias = UpdateResult
WholeSaleOperationDeleteRequest: TypeAlias = list[WholeSaleOperationDelete]
WholeSaleOperationDeleteResponse: TypeAlias = UpdateResult
WholeSaleOperationEditRequest: TypeAlias = list[WholeSaleOperationEdit]
WholeSaleOperationEditResponse: TypeAlias = UpdateResult
WholeSaleOperationGetDiscountRequest: TypeAlias = DiscountOperationGet
WholeSaleOperationGetDiscountResponse: TypeAlias = DiscountOperationRegosArrayResult
WholeSaleOperationGetRequest: TypeAlias = WholeSaleOperationGet
WholeSaleOperationGetResponse: TypeAlias = WholeSaleOperationRegosOffsettedArrayResult
WholeSaleOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
WholeSaleOperationMoveOperationsResponse: TypeAlias = UpdateResult
WholeSaleOperationSetPriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
WholeSaleOperationSetPriceByPriceTypeResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['WholeSaleOperation', 'WholeSaleOperationAdd', 'WholeSaleOperationDelete', 'WholeSaleOperationEdit', 'WholeSaleOperationGet', 'WholeSaleOperationRegosOffsettedArrayResult']


__all__ = [
    'WholeSaleOperation',
    'WholeSaleOperationAdd',
    'WholeSaleOperationDelete',
    'WholeSaleOperationEdit',
    'WholeSaleOperationGet',
    'WholeSaleOperationRegosOffsettedArrayResult',
    'WholeSaleOperationGetRequest',
    'WholeSaleOperationGetResponse',
    'WholeSaleOperationAddRequest',
    'WholeSaleOperationAddResponse',
    'WholeSaleOperationEditRequest',
    'WholeSaleOperationEditResponse',
    'WholeSaleOperationDeleteRequest',
    'WholeSaleOperationDeleteResponse',
    'WholeSaleOperationGetDiscountRequest',
    'WholeSaleOperationGetDiscountResponse',
    'WholeSaleOperationAddDiscountRequest',
    'WholeSaleOperationAddDiscountResponse',
    'WholeSaleOperationDeleteDiscountRequest',
    'WholeSaleOperationDeleteDiscountResponse',
    'WholeSaleOperationMoveOperationsRequest',
    'WholeSaleOperationMoveOperationsResponse',
    'WholeSaleOperationCopyOperationsFromDocPurchaseRequest',
    'WholeSaleOperationCopyOperationsFromDocPurchaseResponse',
    'WholeSaleOperationCopyOperationsFromDocOrderFromPartnerRequest',
    'WholeSaleOperationCopyOperationsFromDocOrderFromPartnerResponse',
    'WholeSaleOperationSetPriceByPriceTypeRequest',
    'WholeSaleOperationSetPriceByPriceTypeResponse'
]

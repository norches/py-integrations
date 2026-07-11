"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class WholeSaleReturnOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class WholeSaleReturnOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class WholeSaleReturnOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class WholeSaleReturnOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class WholeSaleReturnOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class WholeSaleReturnOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[WholeSaleReturnOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DiscountOperationAdd, DiscountOperationDelete, DiscountOperationGet, DiscountOperationRegosArrayResult, DocsOperationsMovement, Error, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


WholeSaleReturnOperationAddDiscountRequest: TypeAlias = DiscountOperationAdd
WholeSaleReturnOperationAddDiscountResponse: TypeAlias = UpdateResult
WholeSaleReturnOperationAddRequest: TypeAlias = list[WholeSaleReturnOperationAdd]
WholeSaleReturnOperationAddResponse: TypeAlias = UpdateResult
WholeSaleReturnOperationDeleteDiscountRequest: TypeAlias = DiscountOperationDelete
WholeSaleReturnOperationDeleteDiscountResponse: TypeAlias = UpdateResult
WholeSaleReturnOperationDeleteRequest: TypeAlias = list[WholeSaleReturnOperationDelete]
WholeSaleReturnOperationDeleteResponse: TypeAlias = UpdateResult
WholeSaleReturnOperationEditRequest: TypeAlias = list[WholeSaleReturnOperationEdit]
WholeSaleReturnOperationEditResponse: TypeAlias = UpdateResult
WholeSaleReturnOperationGetDiscountRequest: TypeAlias = DiscountOperationGet
WholeSaleReturnOperationGetDiscountResponse: TypeAlias = DiscountOperationRegosArrayResult
WholeSaleReturnOperationGetRequest: TypeAlias = WholeSaleReturnOperationGet
WholeSaleReturnOperationGetResponse: TypeAlias = WholeSaleReturnOperationRegosOffsettedArrayResult
WholeSaleReturnOperationMoveOprerationsRequest: TypeAlias = DocsOperationsMovement
WholeSaleReturnOperationMoveOprerationsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['WholeSaleReturnOperation', 'WholeSaleReturnOperationAdd', 'WholeSaleReturnOperationDelete', 'WholeSaleReturnOperationEdit', 'WholeSaleReturnOperationGet', 'WholeSaleReturnOperationRegosOffsettedArrayResult']


__all__ = [
    'WholeSaleReturnOperation',
    'WholeSaleReturnOperationAdd',
    'WholeSaleReturnOperationDelete',
    'WholeSaleReturnOperationEdit',
    'WholeSaleReturnOperationGet',
    'WholeSaleReturnOperationRegosOffsettedArrayResult',
    'WholeSaleReturnOperationGetRequest',
    'WholeSaleReturnOperationGetResponse',
    'WholeSaleReturnOperationAddRequest',
    'WholeSaleReturnOperationAddResponse',
    'WholeSaleReturnOperationEditRequest',
    'WholeSaleReturnOperationEditResponse',
    'WholeSaleReturnOperationDeleteRequest',
    'WholeSaleReturnOperationDeleteResponse',
    'WholeSaleReturnOperationGetDiscountRequest',
    'WholeSaleReturnOperationGetDiscountResponse',
    'WholeSaleReturnOperationAddDiscountRequest',
    'WholeSaleReturnOperationAddDiscountResponse',
    'WholeSaleReturnOperationDeleteDiscountRequest',
    'WholeSaleReturnOperationDeleteDiscountResponse',
    'WholeSaleReturnOperationMoveOprerationsRequest',
    'WholeSaleReturnOperationMoveOprerationsResponse'
]

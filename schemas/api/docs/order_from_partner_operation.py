"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class OrderFromPartnerOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    current_quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class OrderFromPartnerOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class OrderFromPartnerOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class OrderFromPartnerOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class OrderFromPartnerOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class OrderFromPartnerOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[OrderFromPartnerOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DiscountOperationAdd, DiscountOperationDelete, DiscountOperationGet, DiscountOperationRegosArrayResult, DocsOperationsMovement, Error, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


OrderFromPartnerOperationAddDiscountRequest: TypeAlias = DiscountOperationAdd
OrderFromPartnerOperationAddDiscountResponse: TypeAlias = UpdateResult
OrderFromPartnerOperationAddRequest: TypeAlias = list[OrderFromPartnerOperationAdd]
OrderFromPartnerOperationAddResponse: TypeAlias = UpdateResult
OrderFromPartnerOperationDeleteDiscountRequest: TypeAlias = DiscountOperationDelete
OrderFromPartnerOperationDeleteDiscountResponse: TypeAlias = UpdateResult
OrderFromPartnerOperationDeleteRequest: TypeAlias = list[OrderFromPartnerOperationDelete]
OrderFromPartnerOperationDeleteResponse: TypeAlias = UpdateResult
OrderFromPartnerOperationEditRequest: TypeAlias = list[OrderFromPartnerOperationEdit]
OrderFromPartnerOperationEditResponse: TypeAlias = UpdateResult
OrderFromPartnerOperationGetDiscountRequest: TypeAlias = DiscountOperationGet
OrderFromPartnerOperationGetDiscountResponse: TypeAlias = DiscountOperationRegosArrayResult
OrderFromPartnerOperationGetRequest: TypeAlias = OrderFromPartnerOperationGet
OrderFromPartnerOperationGetResponse: TypeAlias = OrderFromPartnerOperationRegosOffsettedArrayResult
OrderFromPartnerOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
OrderFromPartnerOperationMoveOperationsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['OrderFromPartnerOperation', 'OrderFromPartnerOperationAdd', 'OrderFromPartnerOperationDelete', 'OrderFromPartnerOperationEdit', 'OrderFromPartnerOperationGet', 'OrderFromPartnerOperationRegosOffsettedArrayResult']


__all__ = [
    'OrderFromPartnerOperation',
    'OrderFromPartnerOperationAdd',
    'OrderFromPartnerOperationDelete',
    'OrderFromPartnerOperationEdit',
    'OrderFromPartnerOperationGet',
    'OrderFromPartnerOperationRegosOffsettedArrayResult',
    'OrderFromPartnerOperationGetRequest',
    'OrderFromPartnerOperationGetResponse',
    'OrderFromPartnerOperationAddRequest',
    'OrderFromPartnerOperationAddResponse',
    'OrderFromPartnerOperationEditRequest',
    'OrderFromPartnerOperationEditResponse',
    'OrderFromPartnerOperationDeleteRequest',
    'OrderFromPartnerOperationDeleteResponse',
    'OrderFromPartnerOperationMoveOperationsRequest',
    'OrderFromPartnerOperationMoveOperationsResponse',
    'OrderFromPartnerOperationGetDiscountRequest',
    'OrderFromPartnerOperationGetDiscountResponse',
    'OrderFromPartnerOperationAddDiscountRequest',
    'OrderFromPartnerOperationAddDiscountResponse',
    'OrderFromPartnerOperationDeleteDiscountRequest',
    'OrderFromPartnerOperationDeleteDiscountResponse'
]

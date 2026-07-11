"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ReturnsToPartnerOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ReturnsToPartnerOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class ReturnsToPartnerOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ReturnsToPartnerOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class ReturnsToPartnerOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ReturnsToPartnerOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ReturnsToPartnerOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class SetCostByLastReturnToPartner(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DiscountOperationAdd, DiscountOperationDelete, DiscountOperationGet, DiscountOperationRegosArrayResult, DocsOperationsMovement, Error, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


ReturnsToPartnerOperationAddDiscountRequest: TypeAlias = DiscountOperationAdd
ReturnsToPartnerOperationAddDiscountResponse: TypeAlias = UpdateResult
ReturnsToPartnerOperationAddRequest: TypeAlias = list[ReturnsToPartnerOperationAdd]
ReturnsToPartnerOperationAddResponse: TypeAlias = UpdateResult
ReturnsToPartnerOperationDeleteDiscountRequest: TypeAlias = DiscountOperationDelete
ReturnsToPartnerOperationDeleteDiscountResponse: TypeAlias = UpdateResult
ReturnsToPartnerOperationDeleteRequest: TypeAlias = list[ReturnsToPartnerOperationDelete]
ReturnsToPartnerOperationDeleteResponse: TypeAlias = UpdateResult
ReturnsToPartnerOperationEditRequest: TypeAlias = list[ReturnsToPartnerOperationEdit]
ReturnsToPartnerOperationEditResponse: TypeAlias = UpdateResult
ReturnsToPartnerOperationGetDiscountRequest: TypeAlias = DiscountOperationGet
ReturnsToPartnerOperationGetDiscountResponse: TypeAlias = DiscountOperationRegosArrayResult
ReturnsToPartnerOperationGetRequest: TypeAlias = ReturnsToPartnerOperationGet
ReturnsToPartnerOperationGetResponse: TypeAlias = ReturnsToPartnerOperationRegosOffsettedArrayResult
ReturnsToPartnerOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
ReturnsToPartnerOperationMoveOperationsResponse: TypeAlias = UpdateResult
ReturnsToPartnerOperationSetCostByLastPurchaseRequest: TypeAlias = SetCostByLastReturnToPartner
ReturnsToPartnerOperationSetCostByLastPurchaseResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['ReturnsToPartnerOperation', 'ReturnsToPartnerOperationAdd', 'ReturnsToPartnerOperationDelete', 'ReturnsToPartnerOperationEdit', 'ReturnsToPartnerOperationGet', 'ReturnsToPartnerOperationRegosOffsettedArrayResult', 'SetCostByLastReturnToPartner']


__all__ = [
    'ReturnsToPartnerOperation',
    'ReturnsToPartnerOperationAdd',
    'ReturnsToPartnerOperationDelete',
    'ReturnsToPartnerOperationEdit',
    'ReturnsToPartnerOperationGet',
    'ReturnsToPartnerOperationRegosOffsettedArrayResult',
    'SetCostByLastReturnToPartner',
    'ReturnsToPartnerOperationGetRequest',
    'ReturnsToPartnerOperationGetResponse',
    'ReturnsToPartnerOperationAddRequest',
    'ReturnsToPartnerOperationAddResponse',
    'ReturnsToPartnerOperationEditRequest',
    'ReturnsToPartnerOperationEditResponse',
    'ReturnsToPartnerOperationDeleteRequest',
    'ReturnsToPartnerOperationDeleteResponse',
    'ReturnsToPartnerOperationSetCostByLastPurchaseRequest',
    'ReturnsToPartnerOperationSetCostByLastPurchaseResponse',
    'ReturnsToPartnerOperationGetDiscountRequest',
    'ReturnsToPartnerOperationGetDiscountResponse',
    'ReturnsToPartnerOperationAddDiscountRequest',
    'ReturnsToPartnerOperationAddDiscountResponse',
    'ReturnsToPartnerOperationDeleteDiscountRequest',
    'ReturnsToPartnerOperationDeleteDiscountResponse',
    'ReturnsToPartnerOperationMoveOperationsRequest',
    'ReturnsToPartnerOperationMoveOperationsResponse'
]

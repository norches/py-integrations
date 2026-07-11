"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class CommercialOfferOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CommercialOfferOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)


class CommercialOfferOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class CommercialOfferOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)


class CommercialOfferOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class CommercialOfferOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CommercialOfferOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


CommercialOfferOperationAddRequest: TypeAlias = list[CommercialOfferOperationAdd]
CommercialOfferOperationAddResponse: TypeAlias = UpdateResult
CommercialOfferOperationDeleteRequest: TypeAlias = list[CommercialOfferOperationDelete]
CommercialOfferOperationDeleteResponse: TypeAlias = UpdateResult
CommercialOfferOperationEditRequest: TypeAlias = list[CommercialOfferOperationEdit]
CommercialOfferOperationEditResponse: TypeAlias = UpdateResult
CommercialOfferOperationGetRequest: TypeAlias = CommercialOfferOperationGet
CommercialOfferOperationGetResponse: TypeAlias = CommercialOfferOperationRegosOffsettedArrayResult


_MODEL_NAMES = ['CommercialOfferOperation', 'CommercialOfferOperationAdd', 'CommercialOfferOperationDelete', 'CommercialOfferOperationEdit', 'CommercialOfferOperationGet', 'CommercialOfferOperationRegosOffsettedArrayResult']


__all__ = [
    'CommercialOfferOperation',
    'CommercialOfferOperationAdd',
    'CommercialOfferOperationDelete',
    'CommercialOfferOperationEdit',
    'CommercialOfferOperationGet',
    'CommercialOfferOperationRegosOffsettedArrayResult',
    'CommercialOfferOperationGetRequest',
    'CommercialOfferOperationGetResponse',
    'CommercialOfferOperationAddRequest',
    'CommercialOfferOperationAddResponse',
    'CommercialOfferOperationEditRequest',
    'CommercialOfferOperationEditResponse',
    'CommercialOfferOperationDeleteRequest',
    'CommercialOfferOperationDeleteResponse'
]

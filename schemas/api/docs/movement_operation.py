"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class MovementOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class MovementOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class MovementOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class MovementOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class MovementOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class MovementOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[MovementOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsMovement, Error, SetPriceByPriceType_Model, UpdateResult
from schemas.api.references.item import Item


MovementOperationAddRequest: TypeAlias = list[MovementOperationAdd]
MovementOperationAddResponse: TypeAlias = UpdateResult
MovementOperationDeleteRequest: TypeAlias = list[MovementOperationDelete]
MovementOperationDeleteResponse: TypeAlias = UpdateResult
MovementOperationEditRequest: TypeAlias = list[MovementOperationEdit]
MovementOperationEditResponse: TypeAlias = UpdateResult
MovementOperationGetRequest: TypeAlias = MovementOperationGet
MovementOperationGetResponse: TypeAlias = MovementOperationRegosOffsettedArrayResult
MovementOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
MovementOperationMoveOperationsResponse: TypeAlias = UpdateResult
MovementOperationSetPriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
MovementOperationSetPriceByPriceTypeResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['MovementOperation', 'MovementOperationAdd', 'MovementOperationDelete', 'MovementOperationEdit', 'MovementOperationGet', 'MovementOperationRegosOffsettedArrayResult']


__all__ = [
    'MovementOperation',
    'MovementOperationAdd',
    'MovementOperationDelete',
    'MovementOperationEdit',
    'MovementOperationGet',
    'MovementOperationRegosOffsettedArrayResult',
    'MovementOperationGetRequest',
    'MovementOperationGetResponse',
    'MovementOperationAddRequest',
    'MovementOperationAddResponse',
    'MovementOperationEditRequest',
    'MovementOperationEditResponse',
    'MovementOperationDeleteRequest',
    'MovementOperationDeleteResponse',
    'MovementOperationMoveOperationsRequest',
    'MovementOperationMoveOperationsResponse',
    'MovementOperationSetPriceByPriceTypeRequest',
    'MovementOperationSetPriceByPriceTypeResponse'
]

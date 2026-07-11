"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class InventoryOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    datetime: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    actual_quantity: _Decimal | None = PydField(default=None)
    registered_quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class InventoryOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    actual_quantity: _Decimal | None = PydField(default=None)
    datetime: int | None = PydField(default=None)
    update_actual_quantity: bool | None = PydField(default=None)


class InventoryOperationAddBulk(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    department_ids: list[int] | None = PydField(default=None)
    actual_quantity: _Decimal | None = PydField(default=None)
    update_actual_quantity: bool | None = PydField(default=None)


class InventoryOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class InventoryOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    actual_quantity: _Decimal | None = PydField(default=None)
    update_actual_quantity: bool | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)


class InventoryOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    only_deviation: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class InventoryOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[InventoryOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsMovement, Error, SetPriceByPriceType_Model, UpdateResult
from schemas.api.references.item import Item


InventoryOperationAddBulkRequest: TypeAlias = InventoryOperationAddBulk
InventoryOperationAddBulkResponse: TypeAlias = UpdateResult
InventoryOperationAddRequest: TypeAlias = list[InventoryOperationAdd]
InventoryOperationAddResponse: TypeAlias = UpdateResult
InventoryOperationDeleteRequest: TypeAlias = list[InventoryOperationDelete]
InventoryOperationDeleteResponse: TypeAlias = UpdateResult
InventoryOperationEditRequest: TypeAlias = list[InventoryOperationEdit]
InventoryOperationEditResponse: TypeAlias = UpdateResult
InventoryOperationGetRequest: TypeAlias = InventoryOperationGet
InventoryOperationGetResponse: TypeAlias = InventoryOperationRegosOffsettedArrayResult
InventoryOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
InventoryOperationMoveOperationsResponse: TypeAlias = UpdateResult
InventoryOperationSetPriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
InventoryOperationSetPriceByPriceTypeResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['InventoryOperation', 'InventoryOperationAdd', 'InventoryOperationAddBulk', 'InventoryOperationDelete', 'InventoryOperationEdit', 'InventoryOperationGet', 'InventoryOperationRegosOffsettedArrayResult']


__all__ = [
    'InventoryOperation',
    'InventoryOperationAdd',
    'InventoryOperationAddBulk',
    'InventoryOperationDelete',
    'InventoryOperationEdit',
    'InventoryOperationGet',
    'InventoryOperationRegosOffsettedArrayResult',
    'InventoryOperationGetRequest',
    'InventoryOperationGetResponse',
    'InventoryOperationAddRequest',
    'InventoryOperationAddResponse',
    'InventoryOperationAddBulkRequest',
    'InventoryOperationAddBulkResponse',
    'InventoryOperationEditRequest',
    'InventoryOperationEditResponse',
    'InventoryOperationDeleteRequest',
    'InventoryOperationDeleteResponse',
    'InventoryOperationMoveOperationsRequest',
    'InventoryOperationMoveOperationsResponse',
    'InventoryOperationSetPriceByPriceTypeRequest',
    'InventoryOperationSetPriceByPriceTypeResponse'
]

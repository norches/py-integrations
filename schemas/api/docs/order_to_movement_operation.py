"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class OrderToMovementOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class OrderToMovementOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class OrderToMovementOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class OrderToMovementOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class OrderToMovementOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class OrderToMovementOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[OrderToMovementOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsMovement, Error, UpdateResult
from schemas.api.references.item import Item


OrderToMovementOperationAddRequest: TypeAlias = list[OrderToMovementOperationAdd]
OrderToMovementOperationAddResponse: TypeAlias = UpdateResult
OrderToMovementOperationDeleteRequest: TypeAlias = list[OrderToMovementOperationDelete]
OrderToMovementOperationDeleteResponse: TypeAlias = UpdateResult
OrderToMovementOperationEditRequest: TypeAlias = list[OrderToMovementOperationEdit]
OrderToMovementOperationEditResponse: TypeAlias = UpdateResult
OrderToMovementOperationGetRequest: TypeAlias = OrderToMovementOperationGet
OrderToMovementOperationGetResponse: TypeAlias = OrderToMovementOperationRegosOffsettedArrayResult
OrderToMovementOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
OrderToMovementOperationMoveOperationsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['OrderToMovementOperation', 'OrderToMovementOperationAdd', 'OrderToMovementOperationDelete', 'OrderToMovementOperationEdit', 'OrderToMovementOperationGet', 'OrderToMovementOperationRegosOffsettedArrayResult']


__all__ = [
    'OrderToMovementOperation',
    'OrderToMovementOperationAdd',
    'OrderToMovementOperationDelete',
    'OrderToMovementOperationEdit',
    'OrderToMovementOperationGet',
    'OrderToMovementOperationRegosOffsettedArrayResult',
    'OrderToMovementOperationGetRequest',
    'OrderToMovementOperationGetResponse',
    'OrderToMovementOperationAddRequest',
    'OrderToMovementOperationAddResponse',
    'OrderToMovementOperationEditRequest',
    'OrderToMovementOperationEditResponse',
    'OrderToMovementOperationDeleteRequest',
    'OrderToMovementOperationDeleteResponse',
    'OrderToMovementOperationMoveOperationsRequest',
    'OrderToMovementOperationMoveOperationsResponse'
]

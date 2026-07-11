"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class InOutOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class InOutOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class InOutOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class InOutOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class InOutOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class InOutOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[InOutOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsCopy, DocsOperationsMovement, Error, UpdateResult
from schemas.api.references.item import Item


InOutOperationAddRequest: TypeAlias = list[InOutOperationAdd]
InOutOperationAddResponse: TypeAlias = UpdateResult
InOutOperationCopyOperationsFromDocInventoryRequest: TypeAlias = DocsOperationsCopy
InOutOperationCopyOperationsFromDocInventoryResponse: TypeAlias = UpdateResult
InOutOperationDeleteRequest: TypeAlias = list[InOutOperationDelete]
InOutOperationDeleteResponse: TypeAlias = UpdateResult
InOutOperationEditRequest: TypeAlias = list[InOutOperationEdit]
InOutOperationEditResponse: TypeAlias = UpdateResult
InOutOperationGetRequest: TypeAlias = InOutOperationGet
InOutOperationGetResponse: TypeAlias = InOutOperationRegosOffsettedArrayResult
InOutOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
InOutOperationMoveOperationsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['InOutOperation', 'InOutOperationAdd', 'InOutOperationDelete', 'InOutOperationEdit', 'InOutOperationGet', 'InOutOperationRegosOffsettedArrayResult']


__all__ = [
    'InOutOperation',
    'InOutOperationAdd',
    'InOutOperationDelete',
    'InOutOperationEdit',
    'InOutOperationGet',
    'InOutOperationRegosOffsettedArrayResult',
    'InOutOperationGetRequest',
    'InOutOperationGetResponse',
    'InOutOperationAddRequest',
    'InOutOperationAddResponse',
    'InOutOperationEditRequest',
    'InOutOperationEditResponse',
    'InOutOperationDeleteRequest',
    'InOutOperationDeleteResponse',
    'InOutOperationMoveOperationsRequest',
    'InOutOperationMoveOperationsResponse',
    'InOutOperationCopyOperationsFromDocInventoryRequest',
    'InOutOperationCopyOperationsFromDocInventoryResponse'
]

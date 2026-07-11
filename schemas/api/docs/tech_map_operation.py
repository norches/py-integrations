"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class TechMapOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    part_cost: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TechMapOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    data: list[TechMapOperationAddData] | None = PydField(default=None)


class TechMapOperationAddData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    part_cost: _Decimal | None = PydField(default=None)


class TechMapOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class TechMapOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    part_cost: _Decimal | None = PydField(default=None)


class TechMapOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class TechMapOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[TechMapOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsMovement, Error, UpdateResult
from schemas.api.references.item import Item


TechMapOperationAddRequest: TypeAlias = TechMapOperationAdd
TechMapOperationAddResponse: TypeAlias = UpdateResult
TechMapOperationDeleteRequest: TypeAlias = list[TechMapOperationDelete]
TechMapOperationDeleteResponse: TypeAlias = UpdateResult
TechMapOperationEditRequest: TypeAlias = list[TechMapOperationEdit]
TechMapOperationEditResponse: TypeAlias = UpdateResult
TechMapOperationGetRequest: TypeAlias = TechMapOperationGet
TechMapOperationGetResponse: TypeAlias = TechMapOperationRegosOffsettedArrayResult
TechMapOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
TechMapOperationMoveOperationsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['TechMapOperation', 'TechMapOperationAdd', 'TechMapOperationAddData', 'TechMapOperationDelete', 'TechMapOperationEdit', 'TechMapOperationGet', 'TechMapOperationRegosOffsettedArrayResult']


__all__ = [
    'TechMapOperation',
    'TechMapOperationAdd',
    'TechMapOperationAddData',
    'TechMapOperationDelete',
    'TechMapOperationEdit',
    'TechMapOperationGet',
    'TechMapOperationRegosOffsettedArrayResult',
    'TechMapOperationGetRequest',
    'TechMapOperationGetResponse',
    'TechMapOperationAddRequest',
    'TechMapOperationAddResponse',
    'TechMapOperationEditRequest',
    'TechMapOperationEditResponse',
    'TechMapOperationDeleteRequest',
    'TechMapOperationDeleteResponse',
    'TechMapOperationMoveOperationsRequest',
    'TechMapOperationMoveOperationsResponse'
]

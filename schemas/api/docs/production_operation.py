"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ProductionOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    doc_tech_map: DocTechMap | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ProductionOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    data: list[ProductionOperationAddData] | None = PydField(default=None)


class ProductionOperationAddData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)


class ProductionOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class ProductionOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)


class ProductionOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    tech_map_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ProductionOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ProductionOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ProductionOperationReplaceOprTechMap(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsMovement, Error, UpdateResult
from schemas.api.docs.doc_tech_map import DocTechMap
from schemas.api.references.item import Item


ProductionOperationAddRequest: TypeAlias = ProductionOperationAdd
ProductionOperationAddResponse: TypeAlias = UpdateResult
ProductionOperationDeleteRequest: TypeAlias = ProductionOperationDelete
ProductionOperationDeleteResponse: TypeAlias = UpdateResult
ProductionOperationEditRequest: TypeAlias = list[ProductionOperationEdit]
ProductionOperationEditResponse: TypeAlias = UpdateResult
ProductionOperationGetRequest: TypeAlias = ProductionOperationGet
ProductionOperationGetResponse: TypeAlias = ProductionOperationRegosOffsettedArrayResult
ProductionOperationMoveOperationsRequest: TypeAlias = DocsOperationsMovement
ProductionOperationMoveOperationsResponse: TypeAlias = UpdateResult
ProductionOperationReplaceOprTechMapRequest: TypeAlias = ProductionOperationReplaceOprTechMap
ProductionOperationReplaceOprTechMapResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['ProductionOperation', 'ProductionOperationAdd', 'ProductionOperationAddData', 'ProductionOperationDelete', 'ProductionOperationEdit', 'ProductionOperationGet', 'ProductionOperationRegosOffsettedArrayResult', 'ProductionOperationReplaceOprTechMap']


__all__ = [
    'ProductionOperation',
    'ProductionOperationAdd',
    'ProductionOperationAddData',
    'ProductionOperationDelete',
    'ProductionOperationEdit',
    'ProductionOperationGet',
    'ProductionOperationRegosOffsettedArrayResult',
    'ProductionOperationReplaceOprTechMap',
    'ProductionOperationGetRequest',
    'ProductionOperationGetResponse',
    'ProductionOperationAddRequest',
    'ProductionOperationAddResponse',
    'ProductionOperationEditRequest',
    'ProductionOperationEditResponse',
    'ProductionOperationReplaceOprTechMapRequest',
    'ProductionOperationReplaceOprTechMapResponse',
    'ProductionOperationDeleteRequest',
    'ProductionOperationDeleteResponse',
    'ProductionOperationMoveOperationsRequest',
    'ProductionOperationMoveOperationsResponse'
]

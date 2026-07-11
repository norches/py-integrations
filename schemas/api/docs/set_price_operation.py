"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class SetPriceOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    base_value: _Decimal | None = PydField(default=None)
    new_value: _Decimal | None = PydField(default=None)
    current_value: _Decimal | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class SetPriceOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    base_value: _Decimal | None = PydField(default=None)
    new_value: _Decimal | None = PydField(default=None)


class SetPriceOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class SetPriceOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    base_value: _Decimal | None = PydField(default=None)
    new_value: _Decimal | None = PydField(default=None)


class SetPriceOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class SetPriceOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[SetPriceOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import DocsOperationsCopy, Error, ObjectRegosObjectResult, SetPriceByPriceType_Model, UpdateResult
from schemas.api.references.item import Item


SetPriceOperationAddRequest: TypeAlias = list[SetPriceOperationAdd]
SetPriceOperationAddResponse: TypeAlias = UpdateResult
SetPriceOperationCopyOperationsFromDocPurchaseRequest: TypeAlias = DocsOperationsCopy
SetPriceOperationCopyOperationsFromDocPurchaseResponse: TypeAlias = ObjectRegosObjectResult
SetPriceOperationDeleteRequest: TypeAlias = list[SetPriceOperationDelete]
SetPriceOperationDeleteResponse: TypeAlias = UpdateResult
SetPriceOperationEditRequest: TypeAlias = list[SetPriceOperationEdit]
SetPriceOperationEditResponse: TypeAlias = UpdateResult
SetPriceOperationGetRequest: TypeAlias = SetPriceOperationGet
SetPriceOperationGetResponse: TypeAlias = SetPriceOperationRegosOffsettedArrayResult
SetPriceOperationSetBasePriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
SetPriceOperationSetBasePriceByPriceTypeResponse: TypeAlias = UpdateResult
SetPriceOperationSetNewPriceByPriceTypeRequest: TypeAlias = SetPriceByPriceType_Model
SetPriceOperationSetNewPriceByPriceTypeResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['SetPriceOperation', 'SetPriceOperationAdd', 'SetPriceOperationDelete', 'SetPriceOperationEdit', 'SetPriceOperationGet', 'SetPriceOperationRegosOffsettedArrayResult']


__all__ = [
    'SetPriceOperation',
    'SetPriceOperationAdd',
    'SetPriceOperationDelete',
    'SetPriceOperationEdit',
    'SetPriceOperationGet',
    'SetPriceOperationRegosOffsettedArrayResult',
    'SetPriceOperationGetRequest',
    'SetPriceOperationGetResponse',
    'SetPriceOperationAddRequest',
    'SetPriceOperationAddResponse',
    'SetPriceOperationEditRequest',
    'SetPriceOperationEditResponse',
    'SetPriceOperationDeleteRequest',
    'SetPriceOperationDeleteResponse',
    'SetPriceOperationCopyOperationsFromDocPurchaseRequest',
    'SetPriceOperationCopyOperationsFromDocPurchaseResponse',
    'SetPriceOperationSetBasePriceByPriceTypeRequest',
    'SetPriceOperationSetBasePriceByPriceTypeResponse',
    'SetPriceOperationSetNewPriceByPriceTypeRequest',
    'SetPriceOperationSetNewPriceByPriceTypeResponse'
]

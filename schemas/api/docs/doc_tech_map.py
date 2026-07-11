"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocTechMap(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    type: DocTechMapType | None = PydField(default=None)
    code: str | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    autocalculate_part_cost: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocTechMapAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    type: DocTechMapType | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    autocalculate_part_cost: bool | None = PydField(default=None)


class DocTechMapColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocTechMapColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocTechMapColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DocTechMapEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    autocalculate_part_cost: bool | None = PydField(default=None)


class DocTechMapGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    type: DocTechMapType | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocTechMapColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocTechMapId(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocTechMapRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocTechMap] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocTechMapType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.firm import Firm
from schemas.api.references.item import Item


DocTechMapAddRequest: TypeAlias = DocTechMapAdd
DocTechMapAddResponse: TypeAlias = InsertResult
DocTechMapDeleteRequest: TypeAlias = DocTechMapId
DocTechMapDeleteResponse: TypeAlias = UpdateResult
DocTechMapEditRequest: TypeAlias = DocTechMapEdit
DocTechMapEditResponse: TypeAlias = UpdateResult
DocTechMapGetRequest: TypeAlias = DocTechMapGet
DocTechMapGetResponse: TypeAlias = DocTechMapRegosOffsettedArrayResult
DocTechMapLockRequest: TypeAlias = DocTechMapId
DocTechMapLockResponse: TypeAlias = UpdateResult
DocTechMapPerformCancelRequest: TypeAlias = DocTechMapId
DocTechMapPerformCancelResponse: TypeAlias = UpdateResult
DocTechMapPerformRequest: TypeAlias = DocTechMapId
DocTechMapPerformResponse: TypeAlias = UpdateResult
DocTechMapUnlockRequest: TypeAlias = DocTechMapId
DocTechMapUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocTechMap', 'DocTechMapAdd', 'DocTechMapColumn', 'DocTechMapEdit', 'DocTechMapGet', 'DocTechMapId', 'DocTechMapRegosOffsettedArrayResult']


__all__ = [
    'DocTechMap',
    'DocTechMapAdd',
    'DocTechMapColumn',
    'DocTechMapColumns',
    'DocTechMapEdit',
    'DocTechMapGet',
    'DocTechMapId',
    'DocTechMapRegosOffsettedArrayResult',
    'DocTechMapType',
    'DocTechMapGetRequest',
    'DocTechMapGetResponse',
    'DocTechMapAddRequest',
    'DocTechMapAddResponse',
    'DocTechMapEditRequest',
    'DocTechMapEditResponse',
    'DocTechMapDeleteRequest',
    'DocTechMapDeleteResponse',
    'DocTechMapLockRequest',
    'DocTechMapLockResponse',
    'DocTechMapUnlockRequest',
    'DocTechMapUnlockResponse',
    'DocTechMapPerformRequest',
    'DocTechMapPerformResponse',
    'DocTechMapPerformCancelRequest',
    'DocTechMapPerformCancelResponse'
]

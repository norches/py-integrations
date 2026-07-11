"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocProduction(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    type: DocTechMapType | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocProductionRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocProduction] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocProduction_Add(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: DocTechMapType | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocProduction_Column(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocProduction_Columns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocProduction_Columns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10


class DocProduction_Edit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocProduction_Get(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    type: DocTechMapType | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocProduction_Column] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.docs.doc_tech_map import DocTechMapType
from schemas.api.rbac.user import User
from schemas.api.references.stock import Stock


DocProductionAddRequest: TypeAlias = DocProduction_Add
DocProductionAddResponse: TypeAlias = InsertResult
DocProductionDeleteRequest: TypeAlias = Base_ID
DocProductionDeleteResponse: TypeAlias = UpdateResult
DocProductionEditRequest: TypeAlias = DocProduction_Edit
DocProductionEditResponse: TypeAlias = UpdateResult
DocProductionGetRequest: TypeAlias = DocProduction_Get
DocProductionGetResponse: TypeAlias = DocProductionRegosOffsettedArrayResult
DocProductionLockRequest: TypeAlias = Base_ID
DocProductionLockResponse: TypeAlias = UpdateResult
DocProductionPerformCancelRequest: TypeAlias = Base_ID
DocProductionPerformCancelResponse: TypeAlias = UpdateResult
DocProductionPerformRequest: TypeAlias = Base_ID
DocProductionPerformResponse: TypeAlias = UpdateResult
DocProductionUnlockRequest: TypeAlias = Base_ID
DocProductionUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocProduction', 'DocProductionRegosOffsettedArrayResult', 'DocProduction_Add', 'DocProduction_Column', 'DocProduction_Edit', 'DocProduction_Get']


__all__ = [
    'DocProduction',
    'DocProductionRegosOffsettedArrayResult',
    'DocProduction_Add',
    'DocProduction_Column',
    'DocProduction_Columns',
    'DocProduction_Edit',
    'DocProduction_Get',
    'DocProductionGetRequest',
    'DocProductionGetResponse',
    'DocProductionAddRequest',
    'DocProductionAddResponse',
    'DocProductionEditRequest',
    'DocProductionEditResponse',
    'DocProductionDeleteRequest',
    'DocProductionDeleteResponse',
    'DocProductionLockRequest',
    'DocProductionLockResponse',
    'DocProductionUnlockRequest',
    'DocProductionUnlockResponse',
    'DocProductionPerformRequest',
    'DocProductionPerformResponse',
    'DocProductionPerformCancelRequest',
    'DocProductionPerformCancelResponse'
]

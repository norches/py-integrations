"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocInOut(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    inout_type: InOutType | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    auto: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocInOutAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    inout_type: InOutType | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocInOutColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocInOutColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocInOutColumns(IntEnum):
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


class DocInOutDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInOutDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInOutEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    inout_type: InOutType | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocInOutGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    inout_type: InOutType | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    auto: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocInOutColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocInOutLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocInOutPerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInOutRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocInOut] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class InOutType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.stock import Stock


DocInOutAddRequest: TypeAlias = DocInOutAdd
DocInOutAddResponse: TypeAlias = InsertResult
DocInOutDeleteMarkRequest: TypeAlias = DocInOutDeleteMark
DocInOutDeleteMarkResponse: TypeAlias = UpdateResult
DocInOutDeleteRequest: TypeAlias = DocInOutDelete
DocInOutDeleteResponse: TypeAlias = UpdateResult
DocInOutEditRequest: TypeAlias = DocInOutEdit
DocInOutEditResponse: TypeAlias = UpdateResult
DocInOutGetRequest: TypeAlias = DocInOutGet
DocInOutGetResponse: TypeAlias = DocInOutRegosOffsettedArrayResult
DocInOutLockRequest: TypeAlias = DocInOutLockAndUnlock
DocInOutLockResponse: TypeAlias = UpdateResult
DocInOutPerformCancelRequest: TypeAlias = DocInOutPerformAndCancel
DocInOutPerformCancelResponse: TypeAlias = UpdateResult
DocInOutPerformRequest: TypeAlias = DocInOutPerformAndCancel
DocInOutPerformResponse: TypeAlias = UpdateResult
DocInOutUnlockRequest: TypeAlias = DocInOutLockAndUnlock
DocInOutUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocInOut', 'DocInOutAdd', 'DocInOutColumn', 'DocInOutDelete', 'DocInOutDeleteMark', 'DocInOutEdit', 'DocInOutGet', 'DocInOutLockAndUnlock', 'DocInOutPerformAndCancel', 'DocInOutRegosOffsettedArrayResult']


__all__ = [
    'DocInOut',
    'DocInOutAdd',
    'DocInOutColumn',
    'DocInOutColumns',
    'DocInOutDelete',
    'DocInOutDeleteMark',
    'DocInOutEdit',
    'DocInOutGet',
    'DocInOutLockAndUnlock',
    'DocInOutPerformAndCancel',
    'DocInOutRegosOffsettedArrayResult',
    'InOutType',
    'DocInOutGetRequest',
    'DocInOutGetResponse',
    'DocInOutAddRequest',
    'DocInOutAddResponse',
    'DocInOutEditRequest',
    'DocInOutEditResponse',
    'DocInOutDeleteMarkRequest',
    'DocInOutDeleteMarkResponse',
    'DocInOutDeleteRequest',
    'DocInOutDeleteResponse',
    'DocInOutLockRequest',
    'DocInOutLockResponse',
    'DocInOutUnlockRequest',
    'DocInOutUnlockResponse',
    'DocInOutPerformRequest',
    'DocInOutPerformResponse',
    'DocInOutPerformCancelRequest',
    'DocInOutPerformCancelResponse'
]

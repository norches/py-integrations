"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocMovement(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    stock_sender: Stock | None = PydField(default=None)
    stock_receiver: Stock | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocMovementAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    stock_sender_id: int | None = PydField(default=None)
    stock_receiver_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocMovementColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocMovementColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocMovementColumns(IntEnum):
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


class DocMovementDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocMovementDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocMovementEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock_sender_id: int | None = PydField(default=None)
    stock_receiver_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocMovementGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    stock_sender_ids: list[int] | None = PydField(default=None)
    stock_receiver_ids: list[int] | None = PydField(default=None)
    firm_sender_ids: list[int] | None = PydField(default=None)
    firm_receiver_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocMovementColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocMovementLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocMovementPerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocMovementRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocMovement] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.stock import Stock


DocMovementAddRequest: TypeAlias = DocMovementAdd
DocMovementAddResponse: TypeAlias = InsertResult
DocMovementDeleteMarkRequest: TypeAlias = DocMovementDeleteMark
DocMovementDeleteMarkResponse: TypeAlias = UpdateResult
DocMovementDeleteRequest: TypeAlias = DocMovementDelete
DocMovementDeleteResponse: TypeAlias = UpdateResult
DocMovementEditRequest: TypeAlias = DocMovementEdit
DocMovementEditResponse: TypeAlias = UpdateResult
DocMovementGetRequest: TypeAlias = DocMovementGet
DocMovementGetResponse: TypeAlias = DocMovementRegosOffsettedArrayResult
DocMovementLockRequest: TypeAlias = DocMovementLockAndUnlock
DocMovementLockResponse: TypeAlias = UpdateResult
DocMovementPerformCancelRequest: TypeAlias = DocMovementPerformAndCancel
DocMovementPerformCancelResponse: TypeAlias = UpdateResult
DocMovementPerformRequest: TypeAlias = DocMovementPerformAndCancel
DocMovementPerformResponse: TypeAlias = UpdateResult
DocMovementUnlockRequest: TypeAlias = DocMovementLockAndUnlock
DocMovementUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocMovement', 'DocMovementAdd', 'DocMovementColumn', 'DocMovementDelete', 'DocMovementDeleteMark', 'DocMovementEdit', 'DocMovementGet', 'DocMovementLockAndUnlock', 'DocMovementPerformAndCancel', 'DocMovementRegosOffsettedArrayResult']


__all__ = [
    'DocMovement',
    'DocMovementAdd',
    'DocMovementColumn',
    'DocMovementColumns',
    'DocMovementDelete',
    'DocMovementDeleteMark',
    'DocMovementEdit',
    'DocMovementGet',
    'DocMovementLockAndUnlock',
    'DocMovementPerformAndCancel',
    'DocMovementRegosOffsettedArrayResult',
    'DocMovementGetRequest',
    'DocMovementGetResponse',
    'DocMovementAddRequest',
    'DocMovementAddResponse',
    'DocMovementEditRequest',
    'DocMovementEditResponse',
    'DocMovementDeleteMarkRequest',
    'DocMovementDeleteMarkResponse',
    'DocMovementDeleteRequest',
    'DocMovementDeleteResponse',
    'DocMovementLockRequest',
    'DocMovementLockResponse',
    'DocMovementUnlockRequest',
    'DocMovementUnlockResponse',
    'DocMovementPerformRequest',
    'DocMovementPerformResponse',
    'DocMovementPerformCancelRequest',
    'DocMovementPerformCancelResponse'
]

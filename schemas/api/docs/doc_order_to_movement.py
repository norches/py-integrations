"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocOrderToMovement(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    stock_receiver: Stock | None = PydField(default=None)
    status: DocumentStatus | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocOrderToMovementAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    stock_receiver_id: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocOrderToMovementColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocOrderToMovementColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocOrderToMovementColumns(IntEnum):
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


class DocOrderToMovementDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderToMovementDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderToMovementEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock_receiver_id: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocOrderToMovementGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    status_ids: list[int] | None = PydField(default=None)
    stock_receiver_ids: list[int] | None = PydField(default=None)
    firm_receiver_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    sort_orders: list[DocOrderToMovementColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocOrderToMovementLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocOrderToMovementRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocOrderToMovement] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.docs.document_status import DocumentStatus
from schemas.api.rbac.user import User
from schemas.api.references.stock import Stock


DocOrderToMovementAddRequest: TypeAlias = DocOrderToMovementAdd
DocOrderToMovementAddResponse: TypeAlias = InsertResult
DocOrderToMovementDeleteMarkRequest: TypeAlias = DocOrderToMovementDeleteMark
DocOrderToMovementDeleteMarkResponse: TypeAlias = UpdateResult
DocOrderToMovementDeleteRequest: TypeAlias = DocOrderToMovementDelete
DocOrderToMovementDeleteResponse: TypeAlias = UpdateResult
DocOrderToMovementEditRequest: TypeAlias = DocOrderToMovementEdit
DocOrderToMovementEditResponse: TypeAlias = UpdateResult
DocOrderToMovementGetRequest: TypeAlias = DocOrderToMovementGet
DocOrderToMovementGetResponse: TypeAlias = DocOrderToMovementRegosOffsettedArrayResult
DocOrderToMovementLockRequest: TypeAlias = DocOrderToMovementLockAndUnlock
DocOrderToMovementLockResponse: TypeAlias = UpdateResult
DocOrderToMovementUnlockRequest: TypeAlias = DocOrderToMovementLockAndUnlock
DocOrderToMovementUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocOrderToMovement', 'DocOrderToMovementAdd', 'DocOrderToMovementColumn', 'DocOrderToMovementDelete', 'DocOrderToMovementDeleteMark', 'DocOrderToMovementEdit', 'DocOrderToMovementGet', 'DocOrderToMovementLockAndUnlock', 'DocOrderToMovementRegosOffsettedArrayResult']


__all__ = [
    'DocOrderToMovement',
    'DocOrderToMovementAdd',
    'DocOrderToMovementColumn',
    'DocOrderToMovementColumns',
    'DocOrderToMovementDelete',
    'DocOrderToMovementDeleteMark',
    'DocOrderToMovementEdit',
    'DocOrderToMovementGet',
    'DocOrderToMovementLockAndUnlock',
    'DocOrderToMovementRegosOffsettedArrayResult',
    'DocOrderToMovementGetRequest',
    'DocOrderToMovementGetResponse',
    'DocOrderToMovementAddRequest',
    'DocOrderToMovementAddResponse',
    'DocOrderToMovementEditRequest',
    'DocOrderToMovementEditResponse',
    'DocOrderToMovementDeleteMarkRequest',
    'DocOrderToMovementDeleteMarkResponse',
    'DocOrderToMovementDeleteRequest',
    'DocOrderToMovementDeleteResponse',
    'DocOrderToMovementLockRequest',
    'DocOrderToMovementLockResponse',
    'DocOrderToMovementUnlockRequest',
    'DocOrderToMovementUnlockResponse'
]

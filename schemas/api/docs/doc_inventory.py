"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocInventory(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    open_date: int | None = PydField(default=None)
    close_date: int | None = PydField(default=None)
    compare_type: DocInventoryCompareType | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    closed: bool | None = PydField(default=None)
    full: bool | None = PydField(default=None)
    create_docinout: bool | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocInventoryAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    open_date: int | None = PydField(default=None)
    compare_type: DocInventoryCompareType | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    full: bool | None = PydField(default=None)
    create_docinout: bool | None = PydField(default=None)
    external_id: str | None = PydField(default=None)


class DocInventoryCloseAndOpen(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInventoryColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocInventoryColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocInventoryColumns(IntEnum):
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
    VALUE_11 = 11


class DocInventoryCompareType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class DocInventoryDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInventoryDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInventoryEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    open_date: int | None = PydField(default=None)
    compare_type: DocInventoryCompareType | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    full: bool | None = PydField(default=None)
    create_docinout: bool | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocInventoryGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    compare_type: DocInventoryCompareType | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    closed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocInventoryColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocInventoryLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocInventoryRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocInventory] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.price_type import PriceType
from schemas.api.references.stock import Stock


DocInventoryAddRequest: TypeAlias = DocInventoryAdd
DocInventoryAddResponse: TypeAlias = InsertResult
DocInventoryCloseRequest: TypeAlias = DocInventoryCloseAndOpen
DocInventoryCloseResponse: TypeAlias = UpdateResult
DocInventoryDeleteMarkRequest: TypeAlias = DocInventoryDeleteMark
DocInventoryDeleteMarkResponse: TypeAlias = UpdateResult
DocInventoryDeleteRequest: TypeAlias = DocInventoryDelete
DocInventoryDeleteResponse: TypeAlias = UpdateResult
DocInventoryEditRequest: TypeAlias = DocInventoryEdit
DocInventoryEditResponse: TypeAlias = UpdateResult
DocInventoryGetRequest: TypeAlias = DocInventoryGet
DocInventoryGetResponse: TypeAlias = DocInventoryRegosOffsettedArrayResult
DocInventoryLockRequest: TypeAlias = DocInventoryLockAndUnlock
DocInventoryLockResponse: TypeAlias = UpdateResult
DocInventoryOpenRequest: TypeAlias = DocInventoryCloseAndOpen
DocInventoryOpenResponse: TypeAlias = UpdateResult
DocInventoryUnlockRequest: TypeAlias = DocInventoryLockAndUnlock
DocInventoryUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocInventory', 'DocInventoryAdd', 'DocInventoryCloseAndOpen', 'DocInventoryColumn', 'DocInventoryDelete', 'DocInventoryDeleteMark', 'DocInventoryEdit', 'DocInventoryGet', 'DocInventoryLockAndUnlock', 'DocInventoryRegosOffsettedArrayResult']


__all__ = [
    'DocInventory',
    'DocInventoryAdd',
    'DocInventoryCloseAndOpen',
    'DocInventoryColumn',
    'DocInventoryColumns',
    'DocInventoryCompareType',
    'DocInventoryDelete',
    'DocInventoryDeleteMark',
    'DocInventoryEdit',
    'DocInventoryGet',
    'DocInventoryLockAndUnlock',
    'DocInventoryRegosOffsettedArrayResult',
    'DocInventoryGetRequest',
    'DocInventoryGetResponse',
    'DocInventoryAddRequest',
    'DocInventoryAddResponse',
    'DocInventoryEditRequest',
    'DocInventoryEditResponse',
    'DocInventoryDeleteMarkRequest',
    'DocInventoryDeleteMarkResponse',
    'DocInventoryDeleteRequest',
    'DocInventoryDeleteResponse',
    'DocInventoryLockRequest',
    'DocInventoryLockResponse',
    'DocInventoryUnlockRequest',
    'DocInventoryUnlockResponse',
    'DocInventoryCloseRequest',
    'DocInventoryCloseResponse',
    'DocInventoryOpenRequest',
    'DocInventoryOpenResponse'
]

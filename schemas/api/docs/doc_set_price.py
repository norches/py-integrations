"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocSetPrice(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    description: str | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocSetPriceAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    price_type_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DocSetPriceColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocSetPriceColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocSetPriceColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DocSetPriceDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocSetPriceDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocSetPriceEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DocSetPriceGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    price_type_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    sort_orders: list[DocSetPriceColumn] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocSetPriceLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocSetPricePerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocSetPriceRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocSetPrice] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.price_type import PriceType


DocSetPriceAddRequest: TypeAlias = DocSetPriceAdd
DocSetPriceAddResponse: TypeAlias = InsertResult
DocSetPriceDeleteMarkRequest: TypeAlias = DocSetPriceDeleteMark
DocSetPriceDeleteMarkResponse: TypeAlias = UpdateResult
DocSetPriceDeleteRequest: TypeAlias = DocSetPriceDelete
DocSetPriceDeleteResponse: TypeAlias = UpdateResult
DocSetPriceEditRequest: TypeAlias = DocSetPriceEdit
DocSetPriceEditResponse: TypeAlias = UpdateResult
DocSetPriceGetRequest: TypeAlias = DocSetPriceGet
DocSetPriceGetResponse: TypeAlias = DocSetPriceRegosOffsettedArrayResult
DocSetPriceLockRequest: TypeAlias = DocSetPriceLockAndUnlock
DocSetPriceLockResponse: TypeAlias = UpdateResult
DocSetPricePerformCancelRequest: TypeAlias = DocSetPricePerformAndCancel
DocSetPricePerformCancelResponse: TypeAlias = UpdateResult
DocSetPricePerformRequest: TypeAlias = DocSetPricePerformAndCancel
DocSetPricePerformResponse: TypeAlias = UpdateResult
DocSetPriceUnlockRequest: TypeAlias = DocSetPriceLockAndUnlock
DocSetPriceUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocSetPrice', 'DocSetPriceAdd', 'DocSetPriceColumn', 'DocSetPriceDelete', 'DocSetPriceDeleteMark', 'DocSetPriceEdit', 'DocSetPriceGet', 'DocSetPriceLockAndUnlock', 'DocSetPricePerformAndCancel', 'DocSetPriceRegosOffsettedArrayResult']


__all__ = [
    'DocSetPrice',
    'DocSetPriceAdd',
    'DocSetPriceColumn',
    'DocSetPriceColumns',
    'DocSetPriceDelete',
    'DocSetPriceDeleteMark',
    'DocSetPriceEdit',
    'DocSetPriceGet',
    'DocSetPriceLockAndUnlock',
    'DocSetPricePerformAndCancel',
    'DocSetPriceRegosOffsettedArrayResult',
    'DocSetPriceGetRequest',
    'DocSetPriceGetResponse',
    'DocSetPriceAddRequest',
    'DocSetPriceAddResponse',
    'DocSetPriceEditRequest',
    'DocSetPriceEditResponse',
    'DocSetPriceDeleteMarkRequest',
    'DocSetPriceDeleteMarkResponse',
    'DocSetPriceDeleteRequest',
    'DocSetPriceDeleteResponse',
    'DocSetPriceLockRequest',
    'DocSetPriceLockResponse',
    'DocSetPriceUnlockRequest',
    'DocSetPriceUnlockResponse',
    'DocSetPricePerformRequest',
    'DocSetPricePerformResponse',
    'DocSetPricePerformCancelRequest',
    'DocSetPricePerformCancelResponse'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocAccountMovement(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    account_sender: Account | None = PydField(default=None)
    amount_sended: _Decimal | None = PydField(default=None)
    account_receiver: Account | None = PydField(default=None)
    amount_received: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocAccountMovementAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    account_sender_id: int | None = PydField(default=None)
    account_receiver_id: int | None = PydField(default=None)
    amount_sended: _Decimal | None = PydField(default=None)
    amount_received: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocAccountMovementColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocAccountMovementColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocAccountMovementColumns(IntEnum):
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
    VALUE_12 = 12


class DocAccountMovementDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocAccountMovementDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocAccountMovementEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    amount_sended: _Decimal | None = PydField(default=None)
    amount_received: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class DocAccountMovementGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    sort_orders: list[DocAccountMovementColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocAccountMovementPerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocAccountMovementRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocAccountMovement] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.rbac.user import User
from schemas.api.references.account import Account
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit
from schemas.api.references.firm import Firm


DocAccountMovementAddRequest: TypeAlias = DocAccountMovementAdd
DocAccountMovementAddResponse: TypeAlias = InsertResult
DocAccountMovementDeleteMarkRequest: TypeAlias = DocAccountMovementDeleteMark
DocAccountMovementDeleteMarkResponse: TypeAlias = UpdateResult
DocAccountMovementDeleteRequest: TypeAlias = DocAccountMovementDelete
DocAccountMovementDeleteResponse: TypeAlias = UpdateResult
DocAccountMovementEditRequest: TypeAlias = DocAccountMovementEdit
DocAccountMovementEditResponse: TypeAlias = UpdateResult
DocAccountMovementGetRequest: TypeAlias = DocAccountMovementGet
DocAccountMovementGetResponse: TypeAlias = DocAccountMovementRegosOffsettedArrayResult
DocAccountMovementPerformCancelRequest: TypeAlias = DocAccountMovementPerformAndCancel
DocAccountMovementPerformCancelResponse: TypeAlias = UpdateResult
DocAccountMovementPerformRequest: TypeAlias = DocAccountMovementPerformAndCancel
DocAccountMovementPerformResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocAccountMovement', 'DocAccountMovementAdd', 'DocAccountMovementColumn', 'DocAccountMovementDelete', 'DocAccountMovementDeleteMark', 'DocAccountMovementEdit', 'DocAccountMovementGet', 'DocAccountMovementPerformAndCancel', 'DocAccountMovementRegosOffsettedArrayResult']


__all__ = [
    'DocAccountMovement',
    'DocAccountMovementAdd',
    'DocAccountMovementColumn',
    'DocAccountMovementColumns',
    'DocAccountMovementDelete',
    'DocAccountMovementDeleteMark',
    'DocAccountMovementEdit',
    'DocAccountMovementGet',
    'DocAccountMovementPerformAndCancel',
    'DocAccountMovementRegosOffsettedArrayResult',
    'DocAccountMovementGetRequest',
    'DocAccountMovementGetResponse',
    'DocAccountMovementAddRequest',
    'DocAccountMovementAddResponse',
    'DocAccountMovementEditRequest',
    'DocAccountMovementEditResponse',
    'DocAccountMovementDeleteMarkRequest',
    'DocAccountMovementDeleteMarkResponse',
    'DocAccountMovementDeleteRequest',
    'DocAccountMovementDeleteResponse',
    'DocAccountMovementPerformRequest',
    'DocAccountMovementPerformResponse',
    'DocAccountMovementPerformCancelRequest',
    'DocAccountMovementPerformCancelResponse'
]

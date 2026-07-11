"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocPayment(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    type: PaymentType | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    document_type_id: int | None = PydField(default=None)
    contract: DocContractShort | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    category: AccountOperationCategory | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    description: str | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocPaymentAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    type_id: int | None = PydField(default=None)
    document: int | None = PydField(default=None)
    document_type_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    category_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class DocPaymentColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocPaymentColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocPaymentColumns(IntEnum):
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
    VALUE_13 = 13
    VALUE_14 = 14


class DocPaymentDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocPaymentDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocPaymentEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    type_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    category_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class DocPaymentGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    payment_direction: PaymentDirection | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    category_ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    document_type_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    sort_orders: list[DocPaymentColumn] | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocPaymentPerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocPaymentRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocPayment] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class PaymentDirection(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.rbac.user import User
from schemas.api.references.account_operation_category import AccountOperationCategory
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit
from schemas.api.references.firm import Firm
from schemas.api.references.partner import Partner
from schemas.api.references.payment_type import PaymentType


DocPaymentAddRequest: TypeAlias = DocPaymentAdd
DocPaymentAddResponse: TypeAlias = InsertResult
DocPaymentDeleteMarkRequest: TypeAlias = DocPaymentDeleteMark
DocPaymentDeleteMarkResponse: TypeAlias = UpdateResult
DocPaymentDeleteRequest: TypeAlias = DocPaymentDelete
DocPaymentDeleteResponse: TypeAlias = UpdateResult
DocPaymentEditRequest: TypeAlias = DocPaymentEdit
DocPaymentEditResponse: TypeAlias = UpdateResult
DocPaymentGetRequest: TypeAlias = DocPaymentGet
DocPaymentGetResponse: TypeAlias = DocPaymentRegosOffsettedArrayResult
DocPaymentPerformCancelRequest: TypeAlias = DocPaymentPerformAndCancel
DocPaymentPerformCancelResponse: TypeAlias = UpdateResult
DocPaymentPerformRequest: TypeAlias = DocPaymentPerformAndCancel
DocPaymentPerformResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocPayment', 'DocPaymentAdd', 'DocPaymentColumn', 'DocPaymentDelete', 'DocPaymentDeleteMark', 'DocPaymentEdit', 'DocPaymentGet', 'DocPaymentPerformAndCancel', 'DocPaymentRegosOffsettedArrayResult']


__all__ = [
    'DocPayment',
    'DocPaymentAdd',
    'DocPaymentColumn',
    'DocPaymentColumns',
    'DocPaymentDelete',
    'DocPaymentDeleteMark',
    'DocPaymentEdit',
    'DocPaymentGet',
    'DocPaymentPerformAndCancel',
    'DocPaymentRegosOffsettedArrayResult',
    'PaymentDirection',
    'DocPaymentGetRequest',
    'DocPaymentGetResponse',
    'DocPaymentAddRequest',
    'DocPaymentAddResponse',
    'DocPaymentEditRequest',
    'DocPaymentEditResponse',
    'DocPaymentDeleteMarkRequest',
    'DocPaymentDeleteMarkResponse',
    'DocPaymentDeleteRequest',
    'DocPaymentDeleteResponse',
    'DocPaymentPerformRequest',
    'DocPaymentPerformResponse',
    'DocPaymentPerformCancelRequest',
    'DocPaymentPerformCancelResponse'
]

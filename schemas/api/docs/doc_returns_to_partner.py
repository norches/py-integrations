"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocReturnsToPartner(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    contract: DocContractShort | None = PydField(default=None)
    description: str | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocReturnsToPartnerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocReturnsToPartnerColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocReturnsToPartnerColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocReturnsToPartnerColumns(IntEnum):
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


class DocReturnsToPartnerDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocReturnsToPartnerDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocReturnsToPartnerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocReturnsToPartnerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocReturnsToPartnerColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocReturnsToPartnerLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocReturnsToPartnerPerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocReturnsToPartnerRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocReturnsToPartner] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.partner import Partner
from schemas.api.references.stock import Stock


DocReturnsToPartnerAddRequest: TypeAlias = DocReturnsToPartnerAdd
DocReturnsToPartnerAddResponse: TypeAlias = InsertResult
DocReturnsToPartnerDeleteMarkRequest: TypeAlias = DocReturnsToPartnerDeleteMark
DocReturnsToPartnerDeleteMarkResponse: TypeAlias = UpdateResult
DocReturnsToPartnerDeleteRequest: TypeAlias = DocReturnsToPartnerDelete
DocReturnsToPartnerDeleteResponse: TypeAlias = UpdateResult
DocReturnsToPartnerEditRequest: TypeAlias = DocReturnsToPartnerEdit
DocReturnsToPartnerEditResponse: TypeAlias = UpdateResult
DocReturnsToPartnerGetRequest: TypeAlias = DocReturnsToPartnerGet
DocReturnsToPartnerGetResponse: TypeAlias = DocReturnsToPartnerRegosOffsettedArrayResult
DocReturnsToPartnerLockRequest: TypeAlias = DocReturnsToPartnerLockAndUnlock
DocReturnsToPartnerLockResponse: TypeAlias = UpdateResult
DocReturnsToPartnerPerformCancelRequest: TypeAlias = DocReturnsToPartnerPerformAndCancel
DocReturnsToPartnerPerformCancelResponse: TypeAlias = UpdateResult
DocReturnsToPartnerPerformRequest: TypeAlias = DocReturnsToPartnerPerformAndCancel
DocReturnsToPartnerPerformResponse: TypeAlias = UpdateResult
DocReturnsToPartnerUnlockRequest: TypeAlias = DocReturnsToPartnerLockAndUnlock
DocReturnsToPartnerUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocReturnsToPartner', 'DocReturnsToPartnerAdd', 'DocReturnsToPartnerColumn', 'DocReturnsToPartnerDelete', 'DocReturnsToPartnerDeleteMark', 'DocReturnsToPartnerEdit', 'DocReturnsToPartnerGet', 'DocReturnsToPartnerLockAndUnlock', 'DocReturnsToPartnerPerformAndCancel', 'DocReturnsToPartnerRegosOffsettedArrayResult']


__all__ = [
    'DocReturnsToPartner',
    'DocReturnsToPartnerAdd',
    'DocReturnsToPartnerColumn',
    'DocReturnsToPartnerColumns',
    'DocReturnsToPartnerDelete',
    'DocReturnsToPartnerDeleteMark',
    'DocReturnsToPartnerEdit',
    'DocReturnsToPartnerGet',
    'DocReturnsToPartnerLockAndUnlock',
    'DocReturnsToPartnerPerformAndCancel',
    'DocReturnsToPartnerRegosOffsettedArrayResult',
    'DocReturnsToPartnerGetRequest',
    'DocReturnsToPartnerGetResponse',
    'DocReturnsToPartnerAddRequest',
    'DocReturnsToPartnerAddResponse',
    'DocReturnsToPartnerEditRequest',
    'DocReturnsToPartnerEditResponse',
    'DocReturnsToPartnerDeleteMarkRequest',
    'DocReturnsToPartnerDeleteMarkResponse',
    'DocReturnsToPartnerDeleteRequest',
    'DocReturnsToPartnerDeleteResponse',
    'DocReturnsToPartnerLockRequest',
    'DocReturnsToPartnerLockResponse',
    'DocReturnsToPartnerUnlockRequest',
    'DocReturnsToPartnerUnlockResponse',
    'DocReturnsToPartnerPerformRequest',
    'DocReturnsToPartnerPerformResponse',
    'DocReturnsToPartnerPerformCancelRequest',
    'DocReturnsToPartnerPerformCancelResponse'
]

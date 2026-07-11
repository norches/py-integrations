"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocOrderFromPartner(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    contract: DocContractShort | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    status: DocumentStatus | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    booked: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DocOrderFromPartnerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    booked: bool | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocOrderFromPartnerColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocOrderFromPartnerColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocOrderFromPartnerColumns(IntEnum):
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


class DocOrderFromPartnerDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderFromPartnerDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderFromPartnerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    booked: bool | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocOrderFromPartnerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    status_ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    sort_orders: list[DocOrderFromPartnerColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocOrderFromPartnerLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocOrderFromPartnerRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocOrderFromPartner] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.docs.document_status import DocumentStatus
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.partner import Partner
from schemas.api.references.stock import Stock


DocOrderFromPartnerAddRequest: TypeAlias = DocOrderFromPartnerAdd
DocOrderFromPartnerAddResponse: TypeAlias = InsertResult
DocOrderFromPartnerDeleteMarkRequest: TypeAlias = DocOrderFromPartnerDeleteMark
DocOrderFromPartnerDeleteMarkResponse: TypeAlias = UpdateResult
DocOrderFromPartnerDeleteRequest: TypeAlias = DocOrderFromPartnerDelete
DocOrderFromPartnerDeleteResponse: TypeAlias = UpdateResult
DocOrderFromPartnerEditRequest: TypeAlias = DocOrderFromPartnerEdit
DocOrderFromPartnerEditResponse: TypeAlias = UpdateResult
DocOrderFromPartnerGetRequest: TypeAlias = DocOrderFromPartnerGet
DocOrderFromPartnerGetResponse: TypeAlias = DocOrderFromPartnerRegosOffsettedArrayResult
DocOrderFromPartnerLockRequest: TypeAlias = DocOrderFromPartnerLockAndUnlock
DocOrderFromPartnerLockResponse: TypeAlias = UpdateResult
DocOrderFromPartnerUnlockRequest: TypeAlias = DocOrderFromPartnerLockAndUnlock
DocOrderFromPartnerUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocOrderFromPartner', 'DocOrderFromPartnerAdd', 'DocOrderFromPartnerColumn', 'DocOrderFromPartnerDelete', 'DocOrderFromPartnerDeleteMark', 'DocOrderFromPartnerEdit', 'DocOrderFromPartnerGet', 'DocOrderFromPartnerLockAndUnlock', 'DocOrderFromPartnerRegosOffsettedArrayResult']


__all__ = [
    'DocOrderFromPartner',
    'DocOrderFromPartnerAdd',
    'DocOrderFromPartnerColumn',
    'DocOrderFromPartnerColumns',
    'DocOrderFromPartnerDelete',
    'DocOrderFromPartnerDeleteMark',
    'DocOrderFromPartnerEdit',
    'DocOrderFromPartnerGet',
    'DocOrderFromPartnerLockAndUnlock',
    'DocOrderFromPartnerRegosOffsettedArrayResult',
    'DocOrderFromPartnerGetRequest',
    'DocOrderFromPartnerGetResponse',
    'DocOrderFromPartnerAddRequest',
    'DocOrderFromPartnerAddResponse',
    'DocOrderFromPartnerEditRequest',
    'DocOrderFromPartnerEditResponse',
    'DocOrderFromPartnerDeleteMarkRequest',
    'DocOrderFromPartnerDeleteMarkResponse',
    'DocOrderFromPartnerDeleteRequest',
    'DocOrderFromPartnerDeleteResponse',
    'DocOrderFromPartnerLockRequest',
    'DocOrderFromPartnerLockResponse',
    'DocOrderFromPartnerUnlockRequest',
    'DocOrderFromPartnerUnlockResponse'
]

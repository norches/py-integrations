"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocOrderToPartner(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    contract: DocContractShort | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    status: DocumentStatus | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    description: str | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocOrderToPartnerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DocOrderToPartnerColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocOrderToPartnerColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocOrderToPartnerColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class DocOrderToPartnerDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderToPartnerDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderToPartnerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DocOrderToPartnerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    status_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    sort_orders: list[DocOrderToPartnerColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocOrderToPartnerLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocOrderToPartnerRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocOrderToPartner] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.docs.document_status import DocumentStatus
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.partner import Partner


DocOrderToPartnerAddRequest: TypeAlias = DocOrderToPartnerAdd
DocOrderToPartnerAddResponse: TypeAlias = InsertResult
DocOrderToPartnerDeleteMarkRequest: TypeAlias = DocOrderToPartnerDeleteMark
DocOrderToPartnerDeleteMarkResponse: TypeAlias = UpdateResult
DocOrderToPartnerDeleteRequest: TypeAlias = DocOrderToPartnerDelete
DocOrderToPartnerDeleteResponse: TypeAlias = UpdateResult
DocOrderToPartnerEditRequest: TypeAlias = DocOrderToPartnerEdit
DocOrderToPartnerEditResponse: TypeAlias = UpdateResult
DocOrderToPartnerGetRequest: TypeAlias = DocOrderToPartnerGet
DocOrderToPartnerGetResponse: TypeAlias = DocOrderToPartnerRegosOffsettedArrayResult
DocOrderToPartnerLockRequest: TypeAlias = DocOrderToPartnerLockAndUnlock
DocOrderToPartnerLockResponse: TypeAlias = UpdateResult
DocOrderToPartnerUnlockRequest: TypeAlias = DocOrderToPartnerLockAndUnlock
DocOrderToPartnerUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocOrderToPartner', 'DocOrderToPartnerAdd', 'DocOrderToPartnerColumn', 'DocOrderToPartnerDelete', 'DocOrderToPartnerDeleteMark', 'DocOrderToPartnerEdit', 'DocOrderToPartnerGet', 'DocOrderToPartnerLockAndUnlock', 'DocOrderToPartnerRegosOffsettedArrayResult']


__all__ = [
    'DocOrderToPartner',
    'DocOrderToPartnerAdd',
    'DocOrderToPartnerColumn',
    'DocOrderToPartnerColumns',
    'DocOrderToPartnerDelete',
    'DocOrderToPartnerDeleteMark',
    'DocOrderToPartnerEdit',
    'DocOrderToPartnerGet',
    'DocOrderToPartnerLockAndUnlock',
    'DocOrderToPartnerRegosOffsettedArrayResult',
    'DocOrderToPartnerGetRequest',
    'DocOrderToPartnerGetResponse',
    'DocOrderToPartnerAddRequest',
    'DocOrderToPartnerAddResponse',
    'DocOrderToPartnerEditRequest',
    'DocOrderToPartnerEditResponse',
    'DocOrderToPartnerDeleteMarkRequest',
    'DocOrderToPartnerDeleteMarkResponse',
    'DocOrderToPartnerDeleteRequest',
    'DocOrderToPartnerDeleteResponse',
    'DocOrderToPartnerLockRequest',
    'DocOrderToPartnerLockResponse',
    'DocOrderToPartnerUnlockRequest',
    'DocOrderToPartnerUnlockResponse'
]

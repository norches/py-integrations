"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocWholeSale(RegosModel):
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
    seller: User | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocWholeSaleAdd(RegosModel):
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
    price_type_id: int | None = PydField(default=None)
    seller_id: int | None = PydField(default=None)


class DocWholeSaleColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocWholeSaleColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocWholeSaleColumns(IntEnum):
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
    VALUE_15 = 15


class DocWholeSaleDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocWholeSaleDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocWholeSaleEdit(RegosModel):
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
    seller_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)


class DocWholeSaleGet(RegosModel):
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
    sort_orders: list[DocWholeSaleColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocWholeSaleLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocWholeSalePerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocWholeSaleRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocWholeSale] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.partner import Partner
from schemas.api.references.price_type import PriceType
from schemas.api.references.stock import Stock


DocWholeSaleAddRequest: TypeAlias = DocWholeSaleAdd
DocWholeSaleAddResponse: TypeAlias = InsertResult
DocWholeSaleDeleteMarkRequest: TypeAlias = DocWholeSaleDeleteMark
DocWholeSaleDeleteMarkResponse: TypeAlias = UpdateResult
DocWholeSaleDeleteRequest: TypeAlias = DocWholeSaleDelete
DocWholeSaleDeleteResponse: TypeAlias = UpdateResult
DocWholeSaleEditRequest: TypeAlias = DocWholeSaleEdit
DocWholeSaleEditResponse: TypeAlias = UpdateResult
DocWholeSaleGetRequest: TypeAlias = DocWholeSaleGet
DocWholeSaleGetResponse: TypeAlias = DocWholeSaleRegosOffsettedArrayResult
DocWholeSaleLockRequest: TypeAlias = DocWholeSaleLockAndUnlock
DocWholeSaleLockResponse: TypeAlias = UpdateResult
DocWholeSalePerformCancelRequest: TypeAlias = DocWholeSalePerformAndCancel
DocWholeSalePerformCancelResponse: TypeAlias = UpdateResult
DocWholeSalePerformRequest: TypeAlias = DocWholeSalePerformAndCancel
DocWholeSalePerformResponse: TypeAlias = UpdateResult
DocWholeSaleUnlockRequest: TypeAlias = DocWholeSaleLockAndUnlock
DocWholeSaleUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocWholeSale', 'DocWholeSaleAdd', 'DocWholeSaleColumn', 'DocWholeSaleDelete', 'DocWholeSaleDeleteMark', 'DocWholeSaleEdit', 'DocWholeSaleGet', 'DocWholeSaleLockAndUnlock', 'DocWholeSalePerformAndCancel', 'DocWholeSaleRegosOffsettedArrayResult']


__all__ = [
    'DocWholeSale',
    'DocWholeSaleAdd',
    'DocWholeSaleColumn',
    'DocWholeSaleColumns',
    'DocWholeSaleDelete',
    'DocWholeSaleDeleteMark',
    'DocWholeSaleEdit',
    'DocWholeSaleGet',
    'DocWholeSaleLockAndUnlock',
    'DocWholeSalePerformAndCancel',
    'DocWholeSaleRegosOffsettedArrayResult',
    'DocWholeSaleGetRequest',
    'DocWholeSaleGetResponse',
    'DocWholeSaleAddRequest',
    'DocWholeSaleAddResponse',
    'DocWholeSaleEditRequest',
    'DocWholeSaleEditResponse',
    'DocWholeSaleDeleteMarkRequest',
    'DocWholeSaleDeleteMarkResponse',
    'DocWholeSaleDeleteRequest',
    'DocWholeSaleDeleteResponse',
    'DocWholeSaleLockRequest',
    'DocWholeSaleLockResponse',
    'DocWholeSaleUnlockRequest',
    'DocWholeSaleUnlockResponse',
    'DocWholeSalePerformRequest',
    'DocWholeSalePerformResponse',
    'DocWholeSalePerformCancelRequest',
    'DocWholeSalePerformCancelResponse'
]

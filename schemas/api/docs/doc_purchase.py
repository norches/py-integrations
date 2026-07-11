"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocPurchase(RegosModel):
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
    exchange_rate: _Decimal | None = PydField(default=None)
    additional_expenses_amount: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocPurchaseAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)


class DocPurchaseColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocPurchaseSortOrderColumnsEnum | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocPurchaseEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
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
    fields: list[FieldValueEdit] | None = PydField(default=None)


class DocPurchaseGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocPurchaseColumn] | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocPurchaseRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocPurchase] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocPurchaseSortOrderColumnsEnum(IntEnum):
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


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseLockAndUnlock, Base_ID, ColumnSortOrderDirection, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.common.filter import Filter
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit
from schemas.api.references.partner import Partner
from schemas.api.references.price_type import PriceType
from schemas.api.references.stock import Stock


DocPurchaseAddRequest: TypeAlias = DocPurchaseAdd
DocPurchaseAddResponse: TypeAlias = InsertResult
DocPurchaseDeleteMarkRequest: TypeAlias = Base_ID
DocPurchaseDeleteMarkResponse: TypeAlias = UpdateResult
DocPurchaseDeleteRequest: TypeAlias = Base_ID
DocPurchaseDeleteResponse: TypeAlias = UpdateResult
DocPurchaseEditRequest: TypeAlias = DocPurchaseEdit
DocPurchaseEditResponse: TypeAlias = UpdateResult
DocPurchaseGetRequest: TypeAlias = DocPurchaseGet
DocPurchaseGetResponse: TypeAlias = DocPurchaseRegosOffsettedArrayResult
DocPurchaseLockRequest: TypeAlias = BaseLockAndUnlock
DocPurchaseLockResponse: TypeAlias = UpdateResult
DocPurchasePerformCancelRequest: TypeAlias = Base_ID
DocPurchasePerformCancelResponse: TypeAlias = UpdateResult
DocPurchasePerformRequest: TypeAlias = Base_ID
DocPurchasePerformResponse: TypeAlias = UpdateResult
DocPurchaseUnlockRequest: TypeAlias = BaseLockAndUnlock
DocPurchaseUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocPurchase', 'DocPurchaseAdd', 'DocPurchaseColumn', 'DocPurchaseEdit', 'DocPurchaseGet', 'DocPurchaseRegosOffsettedArrayResult']


__all__ = [
    'DocPurchase',
    'DocPurchaseAdd',
    'DocPurchaseColumn',
    'DocPurchaseEdit',
    'DocPurchaseGet',
    'DocPurchaseRegosOffsettedArrayResult',
    'DocPurchaseSortOrderColumnsEnum',
    'DocPurchaseGetRequest',
    'DocPurchaseGetResponse',
    'DocPurchaseAddRequest',
    'DocPurchaseAddResponse',
    'DocPurchaseEditRequest',
    'DocPurchaseEditResponse',
    'DocPurchaseDeleteMarkRequest',
    'DocPurchaseDeleteMarkResponse',
    'DocPurchaseDeleteRequest',
    'DocPurchaseDeleteResponse',
    'DocPurchaseLockRequest',
    'DocPurchaseLockResponse',
    'DocPurchaseUnlockRequest',
    'DocPurchaseUnlockResponse',
    'DocPurchasePerformRequest',
    'DocPurchasePerformResponse',
    'DocPurchasePerformCancelRequest',
    'DocPurchasePerformCancelResponse'
]

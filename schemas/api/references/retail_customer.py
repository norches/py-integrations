"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailCustomer(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    first_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    main_phone: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    refer_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    region: Region | None = PydField(default=None)
    group: RetailCustomerGroup | None = PydField(default=None)
    full_name: str | None = PydField(default=None)
    last_purchase: int | None = PydField(default=None)
    debt: _Decimal | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailCustomerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    first_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    main_phone: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    refer_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    region_id: int | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class RetailCustomerDebtAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    uuid: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    paid: _Decimal | None = PydField(default=None)


class RetailCustomerDebtPayment(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    payment_uuid: str | None = PydField(default=None)
    debt_uuid: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailCustomerDebtPaymentAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    debt_uuid: str | None = PydField(default=None)
    payment_uuid: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)


class RetailCustomerDebtPaymentRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCustomerDebtPayment] | Error | None = PydField(default=None)


class RetailCustomerDebtPaymentsdGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)


class RetailCustomerDebtRecord(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    uuid: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    payments_amount: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailCustomerDebtRecordGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    uuids: list[str] | None = PydField(default=None)
    is_debts: bool | None = PydField(default=None)


class RetailCustomerDebtRecordRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCustomerDebtRecord] | Error | None = PydField(default=None)


class RetailCustomerDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class RetailCustomerDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class RetailCustomerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    first_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    main_phone: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    refer_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    region_id: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class RetailCustomerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    region_ids: list[int] | None = PydField(default=None)
    refer_ids: list[int] | None = PydField(default=None)
    gender: SexEnum | None = PydField(default=None)
    sort_orders: list[RetailCustomer_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    main_phone: str | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailCustomerItemPurchases(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    item: Item | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    amount2: _Decimal | None = PydField(default=None)


class RetailCustomerItemPurchasesArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCustomerItemPurchases] | Error | None = PydField(default=None)


class RetailCustomerPurchaseInfo(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    favoritePurchases: list[RetailCustomerItemPurchases] | None = PydField(default=None)
    avgChequeAmount: _Decimal | None = PydField(default=None)
    chequeQuantity: int | None = PydField(default=None)
    lastPurchaseDate: int | None = PydField(default=None)
    saleChequeQuantity: int | None = PydField(default=None)
    returnChequeQuantity: int | None = PydField(default=None)


class RetailCustomerPurchaseInfoRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: RetailCustomerPurchaseInfo | Error | None = PydField(default=None)


class RetailCustomerPurchaseInfoRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)


class RetailCustomerPurchaseRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)


class RetailCustomerRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCustomer] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailCustomer_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: RetailCustomer_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class RetailCustomer_SortOrderColumn(IntEnum):
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


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, DecimalRegosObjectResult, Error, InsertResult, Int64RegosObjectResult, SexEnum, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit
from schemas.api.references.item import Item
from schemas.api.references.region import Region
from schemas.api.references.retail_customer_group import RetailCustomerGroup


RetailCustomerAddDebtPaymentRequest: TypeAlias = RetailCustomerDebtPaymentAdd
RetailCustomerAddDebtPaymentResponse: TypeAlias = InsertResult
RetailCustomerAddDebtRequest: TypeAlias = RetailCustomerDebtAdd
RetailCustomerAddDebtResponse: TypeAlias = InsertResult
RetailCustomerAddRequest: TypeAlias = RetailCustomerAdd
RetailCustomerAddResponse: TypeAlias = InsertResult
RetailCustomerDeleteMarkRequest: TypeAlias = RetailCustomerDeleteMark
RetailCustomerDeleteMarkResponse: TypeAlias = UpdateResult
RetailCustomerDeleteRequest: TypeAlias = RetailCustomerDelete
RetailCustomerDeleteResponse: TypeAlias = UpdateResult
RetailCustomerEditRequest: TypeAlias = RetailCustomerEdit
RetailCustomerEditResponse: TypeAlias = UpdateResult
RetailCustomerGetAvgChequeAmountRequest: TypeAlias = RetailCustomerPurchaseRequest
RetailCustomerGetAvgChequeAmountResponse: TypeAlias = DecimalRegosObjectResult
RetailCustomerGetChequeCountRequest: TypeAlias = RetailCustomerPurchaseRequest
RetailCustomerGetChequeCountResponse: TypeAlias = Int64RegosObjectResult
RetailCustomerGetDebtsPaymentHistoryRequest: TypeAlias = RetailCustomerDebtPaymentsdGet
RetailCustomerGetDebtsPaymentHistoryResponse: TypeAlias = RetailCustomerDebtPaymentRegosArrayResult
RetailCustomerGetDebtsRequest: TypeAlias = RetailCustomerDebtRecordGet
RetailCustomerGetDebtsResponse: TypeAlias = RetailCustomerDebtRecordRegosArrayResult
RetailCustomerGetFavoritePurchasesRequest: TypeAlias = RetailCustomerPurchaseRequest
RetailCustomerGetFavoritePurchasesResponse: TypeAlias = RetailCustomerItemPurchasesArrayRegosObjectResult
RetailCustomerGetLastPurchaseDateRequest: TypeAlias = RetailCustomerPurchaseRequest
RetailCustomerGetLastPurchaseDateResponse: TypeAlias = Int64RegosObjectResult
RetailCustomerGetPurchaseInfoRequest: TypeAlias = RetailCustomerPurchaseInfoRequest
RetailCustomerGetPurchaseInfoResponse: TypeAlias = RetailCustomerPurchaseInfoRegosObjectResult
RetailCustomerGetRequest: TypeAlias = RetailCustomerGet
RetailCustomerGetResponse: TypeAlias = RetailCustomerRegosOffsettedArrayResult


_MODEL_NAMES = ['RetailCustomer', 'RetailCustomerAdd', 'RetailCustomerDebtAdd', 'RetailCustomerDebtPayment', 'RetailCustomerDebtPaymentAdd', 'RetailCustomerDebtPaymentRegosArrayResult', 'RetailCustomerDebtPaymentsdGet', 'RetailCustomerDebtRecord', 'RetailCustomerDebtRecordGet', 'RetailCustomerDebtRecordRegosArrayResult', 'RetailCustomerDelete', 'RetailCustomerDeleteMark', 'RetailCustomerEdit', 'RetailCustomerGet', 'RetailCustomerItemPurchases', 'RetailCustomerItemPurchasesArrayRegosObjectResult', 'RetailCustomerPurchaseInfo', 'RetailCustomerPurchaseInfoRegosObjectResult', 'RetailCustomerPurchaseInfoRequest', 'RetailCustomerPurchaseRequest', 'RetailCustomerRegosOffsettedArrayResult', 'RetailCustomer_SortOrder']


__all__ = [
    'RetailCustomer',
    'RetailCustomerAdd',
    'RetailCustomerDebtAdd',
    'RetailCustomerDebtPayment',
    'RetailCustomerDebtPaymentAdd',
    'RetailCustomerDebtPaymentRegosArrayResult',
    'RetailCustomerDebtPaymentsdGet',
    'RetailCustomerDebtRecord',
    'RetailCustomerDebtRecordGet',
    'RetailCustomerDebtRecordRegosArrayResult',
    'RetailCustomerDelete',
    'RetailCustomerDeleteMark',
    'RetailCustomerEdit',
    'RetailCustomerGet',
    'RetailCustomerItemPurchases',
    'RetailCustomerItemPurchasesArrayRegosObjectResult',
    'RetailCustomerPurchaseInfo',
    'RetailCustomerPurchaseInfoRegosObjectResult',
    'RetailCustomerPurchaseInfoRequest',
    'RetailCustomerPurchaseRequest',
    'RetailCustomerRegosOffsettedArrayResult',
    'RetailCustomer_SortOrder',
    'RetailCustomer_SortOrderColumn',
    'RetailCustomerGetRequest',
    'RetailCustomerGetResponse',
    'RetailCustomerAddRequest',
    'RetailCustomerAddResponse',
    'RetailCustomerEditRequest',
    'RetailCustomerEditResponse',
    'RetailCustomerDeleteMarkRequest',
    'RetailCustomerDeleteMarkResponse',
    'RetailCustomerDeleteRequest',
    'RetailCustomerDeleteResponse',
    'RetailCustomerGetFavoritePurchasesRequest',
    'RetailCustomerGetFavoritePurchasesResponse',
    'RetailCustomerGetAvgChequeAmountRequest',
    'RetailCustomerGetAvgChequeAmountResponse',
    'RetailCustomerGetLastPurchaseDateRequest',
    'RetailCustomerGetLastPurchaseDateResponse',
    'RetailCustomerGetChequeCountRequest',
    'RetailCustomerGetChequeCountResponse',
    'RetailCustomerGetPurchaseInfoRequest',
    'RetailCustomerGetPurchaseInfoResponse',
    'RetailCustomerGetDebtsRequest',
    'RetailCustomerGetDebtsResponse',
    'RetailCustomerGetDebtsPaymentHistoryRequest',
    'RetailCustomerGetDebtsPaymentHistoryResponse',
    'RetailCustomerAddDebtRequest',
    'RetailCustomerAddDebtResponse',
    'RetailCustomerAddDebtPaymentRequest',
    'RetailCustomerAddDebtPaymentResponse'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocCheque(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    status: DocChequeStatusEnum | None = PydField(default=None)
    session: str | None = PydField(default=None)
    cashier: User | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    seller: User | None = PydField(default=None)
    return_reason: RetailReturnReason | None = PydField(default=None)
    card: RetailCard | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    agregate_status: AgregateStatusEnum | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocChequeColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocChequeColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocChequeColumns(IntEnum):
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


class DocChequeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuids: list[str] | None = PydField(default=None)
    cashier_ids: list[int] | None = PydField(default=None)
    seller_ids: list[int] | None = PydField(default=None)
    card_ids: list[int] | None = PydField(default=None)
    customer_ids: list[int] | None = PydField(default=None)
    session_uuid: str | None = PydField(default=None)
    status: DocChequeStatusEnum | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    is_fiscal: bool | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    sort_orders: list[DocChequeColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocChequeOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    has_storno: bool | None = PydField(default=None)
    storno_uuid: str | None = PydField(default=None)
    document: str | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    order: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocChequeOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    doc_sale_uuid: str | None = PydField(default=None)
    uuids: list[str] | None = PydField(default=None)


class DocChequeOperationRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocChequeOperation] | Error | None = PydField(default=None)


class DocChequeRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocCheque] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocChequeShort(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    sale_status: DocChequeStatusEnum | None = PydField(default=None)
    session_uuid: str | None = PydField(default=None)
    session_code: str | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    stock_name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    firm_name: str | None = PydField(default=None)
    customer_id: int | None = PydField(default=None)
    customer_name: str | None = PydField(default=None)
    card_id: int | None = PydField(default=None)
    card_barcode: str | None = PydField(default=None)


class DocChequeShortGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuids: list[str] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    search: str | None = PydField(default=None)
    session_uuids: list[str] | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    customer_ids: list[int] | None = PydField(default=None)
    sort_orders: list[DocChequeShortSortOrder] | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    sale_status: DocChequeStatusEnum | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocChequeShortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DocChequeShortRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocChequeShort] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocChequeShortSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocChequeShortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocChequeStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import AgregateStatusEnum, ColumnSortOrderDirection, Error
from schemas.api.rbac.user import User
from schemas.api.references.item import Item
from schemas.api.references.retail_card import RetailCard
from schemas.api.references.retail_return_reason import RetailReturnReason


DocChequeGetFavoritePeriodRequest: TypeAlias = DocChequeGet
DocChequeGetFavoritePeriodResponse: TypeAlias = DocChequeRegosOffsettedArrayResult
DocChequeGetRequest: TypeAlias = DocChequeGet
DocChequeGetResponse: TypeAlias = DocChequeRegosOffsettedArrayResult
DocChequeGetShortRequest: TypeAlias = DocChequeShortGet
DocChequeGetShortResponse: TypeAlias = DocChequeShortRegosOffsettedArrayResult


_MODEL_NAMES = ['DocCheque', 'DocChequeColumn', 'DocChequeGet', 'DocChequeOperation', 'DocChequeOperationGet', 'DocChequeOperationRegosArrayResult', 'DocChequeRegosOffsettedArrayResult', 'DocChequeShort', 'DocChequeShortGet', 'DocChequeShortRegosOffsettedArrayResult', 'DocChequeShortSortOrder']


__all__ = [
    'DocCheque',
    'DocChequeColumn',
    'DocChequeColumns',
    'DocChequeGet',
    'DocChequeOperation',
    'DocChequeOperationGet',
    'DocChequeOperationRegosArrayResult',
    'DocChequeRegosOffsettedArrayResult',
    'DocChequeShort',
    'DocChequeShortGet',
    'DocChequeShortOrderColumn',
    'DocChequeShortRegosOffsettedArrayResult',
    'DocChequeShortSortOrder',
    'DocChequeStatusEnum',
    'DocChequeGetRequest',
    'DocChequeGetResponse',
    'DocChequeGetShortRequest',
    'DocChequeGetShortResponse',
    'DocChequeGetFavoritePeriodRequest',
    'DocChequeGetFavoritePeriodResponse'
]

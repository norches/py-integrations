"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocOpeningBalance(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    debit: _Decimal | None = PydField(default=None)
    credit: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocOpeningBalanceAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    debit: _Decimal | None = PydField(default=None)
    credit: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)


class DocOpeningBalanceColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocOpeningBalanceColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocOpeningBalanceColumns(IntEnum):
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


class DocOpeningBalanceDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOpeningBalanceDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOpeningBalanceEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    debit: _Decimal | None = PydField(default=None)
    credit: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)


class DocOpeningBalanceGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    sort_orders: list[DocOpeningBalanceColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocOpeningBalancePerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOpeningBalanceRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocOpeningBalance] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.currency import Currency
from schemas.api.references.firm import Firm
from schemas.api.references.partner import Partner


DocOpeningBalanceAddRequest: TypeAlias = DocOpeningBalanceAdd
DocOpeningBalanceAddResponse: TypeAlias = InsertResult
DocOpeningBalanceDeleteMarkRequest: TypeAlias = DocOpeningBalanceDeleteMark
DocOpeningBalanceDeleteMarkResponse: TypeAlias = UpdateResult
DocOpeningBalanceDeleteRequest: TypeAlias = DocOpeningBalanceDelete
DocOpeningBalanceDeleteResponse: TypeAlias = UpdateResult
DocOpeningBalanceEditRequest: TypeAlias = DocOpeningBalanceEdit
DocOpeningBalanceEditResponse: TypeAlias = UpdateResult
DocOpeningBalanceGetRequest: TypeAlias = DocOpeningBalanceGet
DocOpeningBalanceGetResponse: TypeAlias = DocOpeningBalanceRegosOffsettedArrayResult
DocOpeningBalancePerformCancelRequest: TypeAlias = DocOpeningBalancePerformAndCancel
DocOpeningBalancePerformCancelResponse: TypeAlias = UpdateResult
DocOpeningBalancePerformRequest: TypeAlias = DocOpeningBalancePerformAndCancel
DocOpeningBalancePerformResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocOpeningBalance', 'DocOpeningBalanceAdd', 'DocOpeningBalanceColumn', 'DocOpeningBalanceDelete', 'DocOpeningBalanceDeleteMark', 'DocOpeningBalanceEdit', 'DocOpeningBalanceGet', 'DocOpeningBalancePerformAndCancel', 'DocOpeningBalanceRegosOffsettedArrayResult']


__all__ = [
    'DocOpeningBalance',
    'DocOpeningBalanceAdd',
    'DocOpeningBalanceColumn',
    'DocOpeningBalanceColumns',
    'DocOpeningBalanceDelete',
    'DocOpeningBalanceDeleteMark',
    'DocOpeningBalanceEdit',
    'DocOpeningBalanceGet',
    'DocOpeningBalancePerformAndCancel',
    'DocOpeningBalanceRegosOffsettedArrayResult',
    'DocOpeningBalanceGetRequest',
    'DocOpeningBalanceGetResponse',
    'DocOpeningBalanceAddRequest',
    'DocOpeningBalanceAddResponse',
    'DocOpeningBalanceEditRequest',
    'DocOpeningBalanceEditResponse',
    'DocOpeningBalanceDeleteMarkRequest',
    'DocOpeningBalanceDeleteMarkResponse',
    'DocOpeningBalanceDeleteRequest',
    'DocOpeningBalanceDeleteResponse',
    'DocOpeningBalancePerformRequest',
    'DocOpeningBalancePerformResponse',
    'DocOpeningBalancePerformCancelRequest',
    'DocOpeningBalancePerformCancelResponse'
]

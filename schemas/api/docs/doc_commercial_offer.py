"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocCommercialOffer(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    description: str | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocCommercialOfferAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)


class DocCommercialOfferColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocCommercialOfferColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocCommercialOfferColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class DocCommercialOfferDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocCommercialOfferDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocCommercialOfferEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)


class DocCommercialOfferGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    currency_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    sort_orders: list[DocCommercialOfferColumn] | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    search: str | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocCommercialOfferLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocCommercialOfferRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocCommercialOffer] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.partner import Partner


DocCommercialOfferAddRequest: TypeAlias = DocCommercialOfferAdd
DocCommercialOfferAddResponse: TypeAlias = InsertResult
DocCommercialOfferDeleteMarkRequest: TypeAlias = DocCommercialOfferDeleteMark
DocCommercialOfferDeleteMarkResponse: TypeAlias = UpdateResult
DocCommercialOfferDeleteRequest: TypeAlias = DocCommercialOfferDelete
DocCommercialOfferDeleteResponse: TypeAlias = UpdateResult
DocCommercialOfferEditRequest: TypeAlias = DocCommercialOfferEdit
DocCommercialOfferEditResponse: TypeAlias = UpdateResult
DocCommercialOfferGetRequest: TypeAlias = DocCommercialOfferGet
DocCommercialOfferGetResponse: TypeAlias = DocCommercialOfferRegosOffsettedArrayResult
DocCommercialOfferLockRequest: TypeAlias = DocCommercialOfferLockAndUnlock
DocCommercialOfferLockResponse: TypeAlias = UpdateResult
DocCommercialOfferUnlockRequest: TypeAlias = DocCommercialOfferLockAndUnlock
DocCommercialOfferUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocCommercialOffer', 'DocCommercialOfferAdd', 'DocCommercialOfferColumn', 'DocCommercialOfferDelete', 'DocCommercialOfferDeleteMark', 'DocCommercialOfferEdit', 'DocCommercialOfferGet', 'DocCommercialOfferLockAndUnlock', 'DocCommercialOfferRegosOffsettedArrayResult']


__all__ = [
    'DocCommercialOffer',
    'DocCommercialOfferAdd',
    'DocCommercialOfferColumn',
    'DocCommercialOfferColumns',
    'DocCommercialOfferDelete',
    'DocCommercialOfferDeleteMark',
    'DocCommercialOfferEdit',
    'DocCommercialOfferGet',
    'DocCommercialOfferLockAndUnlock',
    'DocCommercialOfferRegosOffsettedArrayResult',
    'DocCommercialOfferGetRequest',
    'DocCommercialOfferGetResponse',
    'DocCommercialOfferAddRequest',
    'DocCommercialOfferAddResponse',
    'DocCommercialOfferEditRequest',
    'DocCommercialOfferEditResponse',
    'DocCommercialOfferDeleteMarkRequest',
    'DocCommercialOfferDeleteMarkResponse',
    'DocCommercialOfferDeleteRequest',
    'DocCommercialOfferDeleteResponse',
    'DocCommercialOfferLockRequest',
    'DocCommercialOfferLockResponse',
    'DocCommercialOfferUnlockRequest',
    'DocCommercialOfferUnlockResponse'
]

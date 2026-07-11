"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PartnerBalance(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    document_code: str | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    start_amount: _Decimal | None = PydField(default=None)
    debit: _Decimal | None = PydField(default=None)
    credit: _Decimal | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    document_type: DocumentType | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    currency_amount: _Decimal | None = PydField(default=None)


class PartnerBalanceBase(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    document_code: str | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    start_amount: _Decimal | None = PydField(default=None)
    debit: _Decimal | None = PydField(default=None)
    credit: _Decimal | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    document_type: DocumentType | None = PydField(default=None)


class PartnerBalanceBaseGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class PartnerBalanceBaseRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PartnerBalanceBase] | Error | None = PydField(default=None)


class PartnerBalanceGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)


class PartnerBalanceRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PartnerBalance] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.docs.document_type import DocumentType
from schemas.api.references.currency import Currency
from schemas.api.references.firm import Firm


PartnerBalanceGetInBaseCurrencyRequest: TypeAlias = PartnerBalanceBaseGet
PartnerBalanceGetInBaseCurrencyResponse: TypeAlias = PartnerBalanceBaseRegosArrayResult
PartnerBalanceGetRequest: TypeAlias = PartnerBalanceGet
PartnerBalanceGetResponse: TypeAlias = PartnerBalanceRegosArrayResult


_MODEL_NAMES = ['PartnerBalance', 'PartnerBalanceBase', 'PartnerBalanceBaseGet', 'PartnerBalanceBaseRegosArrayResult', 'PartnerBalanceGet', 'PartnerBalanceRegosArrayResult']


__all__ = [
    'PartnerBalance',
    'PartnerBalanceBase',
    'PartnerBalanceBaseGet',
    'PartnerBalanceBaseRegosArrayResult',
    'PartnerBalanceGet',
    'PartnerBalanceRegosArrayResult',
    'PartnerBalanceGetRequest',
    'PartnerBalanceGetResponse',
    'PartnerBalanceGetInBaseCurrencyRequest',
    'PartnerBalanceGetInBaseCurrencyResponse'
]

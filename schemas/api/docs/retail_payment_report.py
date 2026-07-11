"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailPaymentReport(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    payment_type: PaymentType | None = PydField(default=None)
    data: list[RetailPaymentReportData] | None = PydField(default=None)
    payment_amount: _Decimal | None = PydField(default=None)


class RetailPaymentReportData(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    value: _Decimal | None = PydField(default=None)
    date: str | None = PydField(default=None)


class RetailPaymentReportGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: str | None = PydField(default=None)
    end_date: str | None = PydField(default=None)
    period_interval: RetailPaymentReport_PeriodInterval | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)


class RetailPaymentReportRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailPaymentReport] | Error | None = PydField(default=None)


class RetailPaymentReport_PeriodInterval(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.references.payment_type import PaymentType


RetailPaymentReportGetRequest: TypeAlias = RetailPaymentReportGet
RetailPaymentReportGetResponse: TypeAlias = RetailPaymentReportRegosArrayResult


_MODEL_NAMES = ['RetailPaymentReport', 'RetailPaymentReportData', 'RetailPaymentReportGet', 'RetailPaymentReportRegosArrayResult']


__all__ = [
    'RetailPaymentReport',
    'RetailPaymentReportData',
    'RetailPaymentReportGet',
    'RetailPaymentReportRegosArrayResult',
    'RetailPaymentReport_PeriodInterval',
    'RetailPaymentReportGetRequest',
    'RetailPaymentReportGetResponse'
]

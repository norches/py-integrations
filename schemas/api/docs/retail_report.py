"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailReportCount(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    sale_count: int | None = PydField(default=None)
    return_count: int | None = PydField(default=None)
    debt_amount: _Decimal | None = PydField(default=None)
    debt_paid_amount: _Decimal | None = PydField(default=None)
    gross_profit: _Decimal | None = PydField(default=None)


class RetailReportCountGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)


class RetailReportCountRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailReportCount] | Error | None = PydField(default=None)


class RetailReportOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    item: Item | None = PydField(default=None)
    sale_quantity: _Decimal | None = PydField(default=None)
    sale_amount: _Decimal | None = PydField(default=None)
    return_quantity: _Decimal | None = PydField(default=None)
    return_amount: _Decimal | None = PydField(default=None)


class RetailReportOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailReportOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailReportOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailReportPayment(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    payment_type_name: str | None = PydField(default=None)
    sale_amount: _Decimal | None = PydField(default=None)
    return_amount: _Decimal | None = PydField(default=None)


class RetailReportPaymentGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)


class RetailReportPaymentRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailReportPayment] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.references.item import Item


RetailReportCountsRequest: TypeAlias = RetailReportCountGet
RetailReportCountsResponse: TypeAlias = RetailReportCountRegosArrayResult
RetailReportOperationsRequest: TypeAlias = RetailReportOperationGet
RetailReportOperationsResponse: TypeAlias = RetailReportOperationRegosOffsettedArrayResult
RetailReportPaymentsRequest: TypeAlias = RetailReportPaymentGet
RetailReportPaymentsResponse: TypeAlias = RetailReportPaymentRegosArrayResult


_MODEL_NAMES = ['RetailReportCount', 'RetailReportCountGet', 'RetailReportCountRegosArrayResult', 'RetailReportOperation', 'RetailReportOperationGet', 'RetailReportOperationRegosOffsettedArrayResult', 'RetailReportPayment', 'RetailReportPaymentGet', 'RetailReportPaymentRegosArrayResult']


__all__ = [
    'RetailReportCount',
    'RetailReportCountGet',
    'RetailReportCountRegosArrayResult',
    'RetailReportOperation',
    'RetailReportOperationGet',
    'RetailReportOperationRegosOffsettedArrayResult',
    'RetailReportPayment',
    'RetailReportPaymentGet',
    'RetailReportPaymentRegosArrayResult',
    'RetailReportCountsRequest',
    'RetailReportCountsResponse',
    'RetailReportPaymentsRequest',
    'RetailReportPaymentsResponse',
    'RetailReportOperationsRequest',
    'RetailReportOperationsResponse'
]

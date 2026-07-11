"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocPaymentAggregation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    type: PaymentType | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocPaymentAggregationColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocPaymentAggregationColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocPaymentAggregationColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DocPaymentAggregationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    sort_orders: list[DocPaymentAggregationColumn] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocPaymentAggregationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocPaymentAggregation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error
from schemas.api.references.firm import Firm
from schemas.api.references.payment_type import PaymentType


DocPaymentAggregationGetRequest: TypeAlias = DocPaymentAggregationGet
DocPaymentAggregationGetResponse: TypeAlias = DocPaymentAggregationRegosOffsettedArrayResult


_MODEL_NAMES = ['DocPaymentAggregation', 'DocPaymentAggregationColumn', 'DocPaymentAggregationGet', 'DocPaymentAggregationRegosOffsettedArrayResult']


__all__ = [
    'DocPaymentAggregation',
    'DocPaymentAggregationColumn',
    'DocPaymentAggregationColumns',
    'DocPaymentAggregationGet',
    'DocPaymentAggregationRegosOffsettedArrayResult',
    'DocPaymentAggregationGetRequest',
    'DocPaymentAggregationGetResponse'
]

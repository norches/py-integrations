"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocStockAggregation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    amount2: _Decimal | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocStockAggregationColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocStockAggregationColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocStockAggregationColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DocStockAggregationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    sort_orders: list[DocStockAggregationColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocStockAggregationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocStockAggregation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error
from schemas.api.references.stock import Stock


DocStockAggregationGetRequest: TypeAlias = DocStockAggregationGet
DocStockAggregationGetResponse: TypeAlias = DocStockAggregationRegosOffsettedArrayResult


_MODEL_NAMES = ['DocStockAggregation', 'DocStockAggregationColumn', 'DocStockAggregationGet', 'DocStockAggregationRegosOffsettedArrayResult']


__all__ = [
    'DocStockAggregation',
    'DocStockAggregationColumn',
    'DocStockAggregationColumns',
    'DocStockAggregationGet',
    'DocStockAggregationRegosOffsettedArrayResult',
    'DocStockAggregationGetRequest',
    'DocStockAggregationGetResponse'
]

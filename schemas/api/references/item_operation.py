"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ItemOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    date: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    document_type: DocumentType | None = PydField(default=None)
    document_type_name: str | None = PydField(default=None)
    document_code: str | None = PydField(default=None)
    doc_type_name: str | None = PydField(default=None)
    doc_code: str | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    additional_expenses_amount: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    positive: bool | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)


class ItemOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    sort_orders: list[ItemOprOrder] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ItemOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, VatCalculationTypeEnum
from schemas.api.docs.document_type import DocumentType
from schemas.api.references.item import ItemOprOrder
from schemas.api.references.stock import Stock


ItemOperationGetRequest: TypeAlias = ItemOperationGet
ItemOperationGetResponse: TypeAlias = ItemOperationRegosOffsettedArrayResult


_MODEL_NAMES = ['ItemOperation', 'ItemOperationGet', 'ItemOperationRegosOffsettedArrayResult']


__all__ = [
    'ItemOperation',
    'ItemOperationGet',
    'ItemOperationRegosOffsettedArrayResult',
    'ItemOperationGetRequest',
    'ItemOperationGetResponse'
]

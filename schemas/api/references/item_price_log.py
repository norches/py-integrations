"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ItemPriceLog(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    document_date: int | None = PydField(default=None)
    document_type_id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    document_type_name: str | None = PydField(default=None)
    document_type_name_var: str | None = PydField(default=None)
    document_code: str | None = PydField(default=None)
    doc_date: int | None = PydField(default=None)
    doc_type_name: str | None = PydField(default=None)
    doc_type_name_var: str | None = PydField(default=None)
    doc_code: str | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ItemPriceLogGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_ids: list[int] | None = PydField(default=None)
    price_type_ids: list[int] | None = PydField(default=None)


class ItemPriceLogRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemPriceLog] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.references.price_type import PriceType


ItemPriceLogGetRequest: TypeAlias = ItemPriceLogGet
ItemPriceLogGetResponse: TypeAlias = ItemPriceLogRegosArrayResult


_MODEL_NAMES = ['ItemPriceLog', 'ItemPriceLogGet', 'ItemPriceLogRegosArrayResult']


__all__ = [
    'ItemPriceLog',
    'ItemPriceLogGet',
    'ItemPriceLogRegosArrayResult',
    'ItemPriceLogGetRequest',
    'ItemPriceLogGetResponse'
]

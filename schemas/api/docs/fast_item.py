"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RegosOnlineFastItem(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    code: int | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    image_url: str | None = PydField(default=None)


class RegosOnlineFastItemAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)


class RegosOnlineFastItemArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RegosOnlineFastItem] | Error | None = PydField(default=None)


class RegosOnlineFastItemGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    group_ids: list[int] | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, Error, InsertResult, SingleObjectResult


FastItemAddRequest: TypeAlias = RegosOnlineFastItemAdd
FastItemAddResponse: TypeAlias = InsertResult
FastItemDeleteRequest: TypeAlias = Base_ID
FastItemDeleteResponse: TypeAlias = SingleObjectResult
FastItemGetRequest: TypeAlias = RegosOnlineFastItemGet
FastItemGetResponse: TypeAlias = RegosOnlineFastItemArrayRegosObjectResult


_MODEL_NAMES = ['RegosOnlineFastItem', 'RegosOnlineFastItemAdd', 'RegosOnlineFastItemArrayRegosObjectResult', 'RegosOnlineFastItemGet']


__all__ = [
    'RegosOnlineFastItem',
    'RegosOnlineFastItemAdd',
    'RegosOnlineFastItemArrayRegosObjectResult',
    'RegosOnlineFastItemGet',
    'FastItemGetRequest',
    'FastItemGetResponse',
    'FastItemAddRequest',
    'FastItemAddResponse',
    'FastItemDeleteRequest',
    'FastItemDeleteResponse'
]

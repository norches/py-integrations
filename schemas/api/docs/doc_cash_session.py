"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocCashSession(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    start_user: User | None = PydField(default=None)
    start_amount: _Decimal | None = PydField(default=None)
    close_date: int | None = PydField(default=None)
    close_user: User | None = PydField(default=None)
    closed: bool | None = PydField(default=None)
    close_amount: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocCashSessionColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocCashSessionColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocCashSessionColumns(IntEnum):
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


class DocCashSessionGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuids: list[str] | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    is_agregated: bool | None = PydField(default=None)
    is_close: bool | None = PydField(default=None)
    open_user_id: int | None = PydField(default=None)
    close_user_id: int | None = PydField(default=None)
    sort_orders: list[DocCashSessionColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocCashSessionRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocCashSession] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error
from schemas.api.rbac.user import User


DocCashSessionGetRequest: TypeAlias = DocCashSessionGet
DocCashSessionGetResponse: TypeAlias = DocCashSessionRegosOffsettedArrayResult


_MODEL_NAMES = ['DocCashSession', 'DocCashSessionColumn', 'DocCashSessionGet', 'DocCashSessionRegosOffsettedArrayResult']


__all__ = [
    'DocCashSession',
    'DocCashSessionColumn',
    'DocCashSessionColumns',
    'DocCashSessionGet',
    'DocCashSessionRegosOffsettedArrayResult',
    'DocCashSessionGetRequest',
    'DocCashSessionGetResponse'
]

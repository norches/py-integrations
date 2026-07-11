"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserOperatingCash(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user: User | None = PydField(default=None)
    operating_cash: OperatingCash | None = PydField(default=None)


class UserOperatingCashGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    price_type_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    is_virtual: bool | None = PydField(default=None)
    sort_orders: list[UserOperatingCash_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class UserOperatingCashRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserOperatingCash] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class UserOperatingCashRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class UserOperatingCashSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)


class UserOperatingCash_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: UserOperatingCash_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class UserOperatingCash_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.operating_cash import OperatingCash


UserOperatingCashGetRequest: TypeAlias = UserOperatingCashGet
UserOperatingCashGetResponse: TypeAlias = UserOperatingCashRegosOffsettedArrayResult
UserOperatingCashRemoveRequest: TypeAlias = UserOperatingCashRemove
UserOperatingCashRemoveResponse: TypeAlias = UpdateResult
UserOperatingCashSetRequest: TypeAlias = UserOperatingCashSet
UserOperatingCashSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['UserOperatingCash', 'UserOperatingCashGet', 'UserOperatingCashRegosOffsettedArrayResult', 'UserOperatingCashRemove', 'UserOperatingCashSet', 'UserOperatingCash_SortOrder']


__all__ = [
    'UserOperatingCash',
    'UserOperatingCashGet',
    'UserOperatingCashRegosOffsettedArrayResult',
    'UserOperatingCashRemove',
    'UserOperatingCashSet',
    'UserOperatingCash_SortOrder',
    'UserOperatingCash_SortOrderColumn',
    'UserOperatingCashGetRequest',
    'UserOperatingCashGetResponse',
    'UserOperatingCashSetRequest',
    'UserOperatingCashSetResponse',
    'UserOperatingCashRemoveRequest',
    'UserOperatingCashRemoveResponse'
]

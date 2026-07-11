"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Account(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class AccountAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)


class AccountDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class AccountEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)


class AccountGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_ids: list[int] | None = PydField(default=None)
    sort_orders: list[AccountSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class AccountRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Account] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class AccountSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: AccountSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class AccountSortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.currency import Currency


AccountAddRequest: TypeAlias = AccountAdd
AccountAddResponse: TypeAlias = InsertResult
AccountDeleteRequest: TypeAlias = AccountDelete
AccountDeleteResponse: TypeAlias = UpdateResult
AccountEditRequest: TypeAlias = AccountEdit
AccountEditResponse: TypeAlias = UpdateResult
AccountGetRequest: TypeAlias = AccountGet
AccountGetResponse: TypeAlias = AccountRegosOffsettedArrayResult


_MODEL_NAMES = ['Account', 'AccountAdd', 'AccountDelete', 'AccountEdit', 'AccountGet', 'AccountRegosOffsettedArrayResult', 'AccountSortOrder']


__all__ = [
    'Account',
    'AccountAdd',
    'AccountDelete',
    'AccountEdit',
    'AccountGet',
    'AccountRegosOffsettedArrayResult',
    'AccountSortOrder',
    'AccountSortOrderColumn',
    'AccountGetRequest',
    'AccountGetResponse',
    'AccountAddRequest',
    'AccountAddResponse',
    'AccountEditRequest',
    'AccountEditResponse',
    'AccountDeleteRequest',
    'AccountDeleteResponse'
]

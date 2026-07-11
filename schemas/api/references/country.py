"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Country(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    alfa2: str | None = PydField(default=None)
    alfa3: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CountryAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    alfa2: str | None = PydField(default=None)
    alfa3: str | None = PydField(default=None)


class CountryDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class CountryEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    alfa2: str | None = PydField(default=None)
    alfa3: str | None = PydField(default=None)


class CountryGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    code: list[str] | None = PydField(default=None)
    sort_orders: list[CountrySortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class CountryRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Country] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class CountrySortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: CountrySortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class CountrySortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


CountryAddRequest: TypeAlias = CountryAdd
CountryAddResponse: TypeAlias = InsertResult
CountryDeleteRequest: TypeAlias = CountryDelete
CountryDeleteResponse: TypeAlias = UpdateResult
CountryEditRequest: TypeAlias = CountryEdit
CountryEditResponse: TypeAlias = UpdateResult
CountryGetRequest: TypeAlias = CountryGet
CountryGetResponse: TypeAlias = CountryRegosOffsettedArrayResult


_MODEL_NAMES = ['Country', 'CountryAdd', 'CountryDelete', 'CountryEdit', 'CountryGet', 'CountryRegosOffsettedArrayResult', 'CountrySortOrder']


__all__ = [
    'Country',
    'CountryAdd',
    'CountryDelete',
    'CountryEdit',
    'CountryGet',
    'CountryRegosOffsettedArrayResult',
    'CountrySortOrder',
    'CountrySortOrderColumn',
    'CountryGetRequest',
    'CountryGetResponse',
    'CountryAddRequest',
    'CountryAddResponse',
    'CountryEditRequest',
    'CountryEditResponse',
    'CountryDeleteRequest',
    'CountryDeleteResponse'
]

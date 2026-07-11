"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Dashboard(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    period: DashboardPeriodEnum | None = PydField(default=None)
    name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    is_fixed: bool | None = PydField(default=None)
    is_default: bool | None = PydField(default=None)
    is_creator: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DashboardAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)


class DashboardEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    is_fixed: bool | None = PydField(default=None)


class DashboardGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[DashboardSortOrder] | None = PydField(default=None)


class DashboardPeriodEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DashboardRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Dashboard] | Error | None = PydField(default=None)


class DashboardSetFilters(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    period: DashboardPeriodEnum | None = PydField(default=None)


class DashboardSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DashboardSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DashboardSortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, ColumnSortOrderDirection, Error, InsertResult, SingleObjectResult, UpdateResult


DashboardAddRequest: TypeAlias = DashboardAdd
DashboardAddResponse: TypeAlias = InsertResult
DashboardDeleteRequest: TypeAlias = Base_ID
DashboardDeleteResponse: TypeAlias = UpdateResult
DashboardEditRequest: TypeAlias = DashboardEdit
DashboardEditResponse: TypeAlias = UpdateResult
DashboardGetRequest: TypeAlias = DashboardGet
DashboardGetResponse: TypeAlias = DashboardRegosArrayResult
DashboardSetFiltersRequest: TypeAlias = DashboardSetFilters
DashboardSetFiltersResponse: TypeAlias = SingleObjectResult


_MODEL_NAMES = ['Dashboard', 'DashboardAdd', 'DashboardEdit', 'DashboardGet', 'DashboardRegosArrayResult', 'DashboardSetFilters', 'DashboardSortOrder']


__all__ = [
    'Dashboard',
    'DashboardAdd',
    'DashboardEdit',
    'DashboardGet',
    'DashboardPeriodEnum',
    'DashboardRegosArrayResult',
    'DashboardSetFilters',
    'DashboardSortOrder',
    'DashboardSortOrderColumn',
    'DashboardGetRequest',
    'DashboardGetResponse',
    'DashboardAddRequest',
    'DashboardAddResponse',
    'DashboardEditRequest',
    'DashboardEditResponse',
    'DashboardDeleteRequest',
    'DashboardDeleteResponse',
    'DashboardSetFiltersRequest',
    'DashboardSetFiltersResponse'
]

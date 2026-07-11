"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Widget(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    widget_type: WidgetType | None = PydField(default=None)
    dashboard_id: int | None = PydField(default=None)
    row: int | None = PydField(default=None)
    column: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class WidgetAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    dashboard_id: int | None = PydField(default=None)
    widget_type: WidgetTypesEnum | None = PydField(default=None)
    name: str | None = PydField(default=None)
    row: int | None = PydField(default=None)
    column: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)


class WidgetEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class WidgetGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    dashboard_id: int | None = PydField(default=None)


class WidgetRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Widget] | Error | None = PydField(default=None)


class WidgetSetFilters(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)


class WidgetSetPosition(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    row: int | None = PydField(default=None)
    column: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, Error, SingleObjectResult, UpdateResult
from schemas.api.widgets.widget_type import WidgetType, WidgetTypesEnum


WidgetAddRequest: TypeAlias = list[WidgetAdd]
WidgetAddResponse: TypeAlias = UpdateResult
WidgetDeleteRequest: TypeAlias = list[Base_ID]
WidgetDeleteResponse: TypeAlias = UpdateResult
WidgetEditRequest: TypeAlias = WidgetEdit
WidgetEditResponse: TypeAlias = UpdateResult
WidgetGetRequest: TypeAlias = WidgetGet
WidgetGetResponse: TypeAlias = WidgetRegosArrayResult
WidgetSetFiltersRequest: TypeAlias = WidgetSetFilters
WidgetSetFiltersResponse: TypeAlias = SingleObjectResult
WidgetSetPositionRequest: TypeAlias = list[WidgetSetPosition]
WidgetSetPositionResponse: TypeAlias = SingleObjectResult


_MODEL_NAMES = ['Widget', 'WidgetAdd', 'WidgetEdit', 'WidgetGet', 'WidgetRegosArrayResult', 'WidgetSetFilters', 'WidgetSetPosition']


__all__ = [
    'Widget',
    'WidgetAdd',
    'WidgetEdit',
    'WidgetGet',
    'WidgetRegosArrayResult',
    'WidgetSetFilters',
    'WidgetSetPosition',
    'WidgetGetRequest',
    'WidgetGetResponse',
    'WidgetAddRequest',
    'WidgetAddResponse',
    'WidgetEditRequest',
    'WidgetEditResponse',
    'WidgetDeleteRequest',
    'WidgetDeleteResponse',
    'WidgetSetFiltersRequest',
    'WidgetSetFiltersResponse',
    'WidgetSetPositionRequest',
    'WidgetSetPositionResponse'
]

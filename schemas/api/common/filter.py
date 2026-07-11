"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Filter(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    field: str | None = PydField(default=None)
    operator: FilterOperatorEnum | None = PydField(default=None)
    value: str | None = PydField(default=None)


class FilterFieldInfo(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    field: str | None = PydField(default=None)
    datatype: str | None = PydField(default=None)


class FilterFieldInfoRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[FilterFieldInfo] | Error | None = PydField(default=None)


class FilterGetFields(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: FieldEntityTypeEnum | None = PydField(default=None)


class FilterOperatorEnum(IntEnum):
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


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.references.field import FieldEntityTypeEnum


FilterGetFieldsRequest: TypeAlias = FilterGetFields
FilterGetFieldsResponse: TypeAlias = FilterFieldInfoRegosArrayResult


_MODEL_NAMES = ['Filter', 'FilterFieldInfo', 'FilterFieldInfoRegosArrayResult', 'FilterGetFields']


__all__ = [
    'Filter',
    'FilterFieldInfo',
    'FilterFieldInfoRegosArrayResult',
    'FilterGetFields',
    'FilterOperatorEnum',
    'FilterGetFieldsRequest',
    'FilterGetFieldsResponse'
]

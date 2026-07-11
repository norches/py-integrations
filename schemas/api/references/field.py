"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Field(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    entity_type: FieldEntityTypeEnum | None = PydField(default=None)
    data_type: str | None = PydField(default=None)
    metadata: str | None = PydField(default=None)
    is_custom: bool | None = PydField(default=None)
    required: bool | None = PydField(default=None)


class FieldAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    entity_type: FieldEntityTypeEnum | None = PydField(default=None)
    data_type: str | None = PydField(default=None)
    metadata: str | None = PydField(default=None)
    required: bool | None = PydField(default=None)


class FieldEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    required: bool | None = PydField(default=None)
    metadata: str | None = PydField(default=None)


class FieldEntityTypeEnum(IntEnum):
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
    VALUE_12 = 12


class FieldGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    keys: list[str] | None = PydField(default=None)
    entity_type: FieldEntityTypeEnum | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)
    required: bool | None = PydField(default=None)


class FieldRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Field] | Error | None = PydField(default=None)


class FieldValue(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    key: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    data_type: str | None = PydField(default=None)
    metadata: str | None = PydField(default=None)
    is_custom: bool | None = PydField(default=None)
    required: bool | None = PydField(default=None)
    value: str | None = PydField(default=None)


class FieldValueAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)


class FieldValueEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseSortColumn, Base_ID, Error, InsertResult, UpdateResult


FieldAddRequest: TypeAlias = FieldAdd
FieldAddResponse: TypeAlias = InsertResult
FieldDeleteRequest: TypeAlias = Base_ID
FieldDeleteResponse: TypeAlias = UpdateResult
FieldEditRequest: TypeAlias = FieldEdit
FieldEditResponse: TypeAlias = UpdateResult
FieldGetRequest: TypeAlias = FieldGet
FieldGetResponse: TypeAlias = FieldRegosArrayResult


_MODEL_NAMES = ['Field', 'FieldAdd', 'FieldEdit', 'FieldGet', 'FieldRegosArrayResult', 'FieldValue', 'FieldValueAdd', 'FieldValueEdit']


__all__ = [
    'Field',
    'FieldAdd',
    'FieldEdit',
    'FieldEntityTypeEnum',
    'FieldGet',
    'FieldRegosArrayResult',
    'FieldValue',
    'FieldValueAdd',
    'FieldValueEdit',
    'FieldGetRequest',
    'FieldGetResponse',
    'FieldAddRequest',
    'FieldAddResponse',
    'FieldEditRequest',
    'FieldEditResponse',
    'FieldDeleteRequest',
    'FieldDeleteResponse'
]

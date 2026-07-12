"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import Enum, IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Filter(RegosModel):
    "Служит для дополнительной фильтрации выборок по основным(список полей определяется для каждой сущности отдельно) и по дополнительным полям, созданным для сущности"
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    Field: str | None = PydField(default=None, description="Имя поля сущности (например first_name, region_id, date_of_birth)")
    Operator: FilterOperatorEnum | None = PydField(default=None, description="Оператор фильтрации")
    Value: str | None = PydField(default=None, description="Значение фильтра в текстовом представлении. Для In/NotIn передаётся список значений через запятую. Также поддерживается\nмаска ${field} в качестве значения, где field — название поля, доступного для фильтрации; обязательное условие: тип\nданных поля field должен совпадать с типом данных ${field}. Для Exists/NotExists не обязательно и игнорируется")


class FilterFieldInfo(RegosModel):
    "Поле, доступное для фильтрации."
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    field: str | None = PydField(default=None)
    datatype: str | None = PydField(default=None)


class FilterFieldInfoRegosArrayResult(RegosModel):
    "OpenAPI-only typed equivalent of SingleArrayResult."
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None, description="Признак успешности выполнения запроса.")
    result: list[FilterFieldInfo] | Error | None = PydField(default=None, description="Массив результата.")


class FilterGetFields(RegosModel):
    "Модель запроса для получения списка полей фильтрации сущности."
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: FieldEntityTypeEnum | None = PydField(default=None, description="Сущность, для которой нужно вернуть список полей фильтрации")


class FilterOperatorEnum(str, Enum):
    "Перечисление типов операторов фильтрации"
    Default = "Default"
    Equal = "Equal"
    NotEqual = "NotEqual"
    Greater = "Greater"
    Less = "Less"
    GreaterOrEqual = "GreaterOrEqual"
    LessOrEqual = "LessOrEqual"
    Like = "Like"
    Exists = "Exists"
    NotExists = "NotExists"
    In = "In"
    NotIn = "NotIn"


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

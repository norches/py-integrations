"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Producer(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ProducerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)


class ProducerDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ProducerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class ProducerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    sort_orders: list[ProducerSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ProducerRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Producer] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ProducerSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: ProducerSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class ProducerSortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult


ProducerAddRequest: TypeAlias = ProducerAdd
ProducerAddResponse: TypeAlias = InsertResult
ProducerDeleteRequest: TypeAlias = ProducerDelete
ProducerDeleteResponse: TypeAlias = UpdateResult
ProducerEditRequest: TypeAlias = ProducerEdit
ProducerEditResponse: TypeAlias = UpdateResult
ProducerGetRequest: TypeAlias = ProducerGet
ProducerGetResponse: TypeAlias = ProducerRegosOffsettedArrayResult


_MODEL_NAMES = ['Producer', 'ProducerAdd', 'ProducerDelete', 'ProducerEdit', 'ProducerGet', 'ProducerRegosOffsettedArrayResult', 'ProducerSortOrder']


__all__ = [
    'Producer',
    'ProducerAdd',
    'ProducerDelete',
    'ProducerEdit',
    'ProducerGet',
    'ProducerRegosOffsettedArrayResult',
    'ProducerSortOrder',
    'ProducerSortOrderColumn',
    'ProducerGetRequest',
    'ProducerGetResponse',
    'ProducerAddRequest',
    'ProducerAddResponse',
    'ProducerEditRequest',
    'ProducerEditResponse',
    'ProducerDeleteRequest',
    'ProducerDeleteResponse'
]

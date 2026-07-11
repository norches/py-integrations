"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class AccessApp(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class Redefinition(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    app: AccessApp | None = PydField(default=None)
    language: Language | None = PydField(default=None)
    table: Table | None = PydField(default=None)
    data_id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    hidden: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RedefinitionRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Redefinition] | Error | None = PydField(default=None)


class Redefinition_Add(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    app_id: int | None = PydField(default=None)
    lang_id: int | None = PydField(default=None)
    table_id: int | None = PydField(default=None)
    data_id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    hidden: bool | None = PydField(default=None)


class Redefinition_Delete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class Redefinition_Edit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    app_id: int | None = PydField(default=None)
    lang_id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    hidden: bool | None = PydField(default=None)


class Redefinition_Get(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    table_ids: list[int] | None = PydField(default=None)
    data_id: int | None = PydField(default=None)
    app_id: int | None = PydField(default=None)
    lang_id: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    hidden: bool | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, Table, UpdateResult
from schemas.api.rbac.language import Language


RedefinitionAddRequest: TypeAlias = Redefinition_Add
RedefinitionAddResponse: TypeAlias = InsertResult
RedefinitionDeleteRequest: TypeAlias = Redefinition_Delete
RedefinitionDeleteResponse: TypeAlias = UpdateResult
RedefinitionEditRequest: TypeAlias = Redefinition_Edit
RedefinitionEditResponse: TypeAlias = UpdateResult
RedefinitionGetRequest: TypeAlias = Redefinition_Get
RedefinitionGetResponse: TypeAlias = RedefinitionRegosArrayResult


_MODEL_NAMES = ['AccessApp', 'Redefinition', 'RedefinitionRegosArrayResult', 'Redefinition_Add', 'Redefinition_Delete', 'Redefinition_Edit', 'Redefinition_Get']


__all__ = [
    'AccessApp',
    'Redefinition',
    'RedefinitionRegosArrayResult',
    'Redefinition_Add',
    'Redefinition_Delete',
    'Redefinition_Edit',
    'Redefinition_Get',
    'RedefinitionGetRequest',
    'RedefinitionGetResponse',
    'RedefinitionAddRequest',
    'RedefinitionAddResponse',
    'RedefinitionEditRequest',
    'RedefinitionEditResponse',
    'RedefinitionDeleteRequest',
    'RedefinitionDeleteResponse'
]

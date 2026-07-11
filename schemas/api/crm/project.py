"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Project(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    logo_file_id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    created_date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ProjectAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    logo_file_id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)


class ProjectDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ProjectEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    logo_file_id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)


class ProjectGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    responsible_user_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)


class ProjectRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Project] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ProjectSetAccess(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)
    replace_mode: bool | None = PydField(default=None)


class ProjectSetResponsible(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseSortColumn, Error, InsertResult, UpdateResult


ProjectAddRequest: TypeAlias = ProjectAdd
ProjectAddResponse: TypeAlias = InsertResult
ProjectDeleteRequest: TypeAlias = ProjectDelete
ProjectDeleteResponse: TypeAlias = UpdateResult
ProjectEditRequest: TypeAlias = ProjectEdit
ProjectEditResponse: TypeAlias = UpdateResult
ProjectGetRequest: TypeAlias = ProjectGet
ProjectGetResponse: TypeAlias = ProjectRegosOffsettedArrayResult
ProjectSetAccessRequest: TypeAlias = ProjectSetAccess
ProjectSetAccessResponse: TypeAlias = UpdateResult
ProjectSetResponsibleRequest: TypeAlias = ProjectSetResponsible
ProjectSetResponsibleResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Project', 'ProjectAdd', 'ProjectDelete', 'ProjectEdit', 'ProjectGet', 'ProjectRegosOffsettedArrayResult', 'ProjectSetAccess', 'ProjectSetResponsible']


__all__ = [
    'Project',
    'ProjectAdd',
    'ProjectDelete',
    'ProjectEdit',
    'ProjectGet',
    'ProjectRegosOffsettedArrayResult',
    'ProjectSetAccess',
    'ProjectSetResponsible',
    'ProjectGetRequest',
    'ProjectGetResponse',
    'ProjectAddRequest',
    'ProjectAddResponse',
    'ProjectEditRequest',
    'ProjectEditResponse',
    'ProjectDeleteRequest',
    'ProjectDeleteResponse',
    'ProjectSetAccessRequest',
    'ProjectSetAccessResponse',
    'ProjectSetResponsibleRequest',
    'ProjectSetResponsibleResponse'
]

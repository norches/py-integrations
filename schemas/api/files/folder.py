"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class CommonFolderAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)


class CommonFolderDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class CommonFolderEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)


class CommonFolderGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)


class CommonFolderRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CommonFolder] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseSortColumn, CommonFileAccessLevelEnum, CommonFolder, Error, InsertResult, UpdateResult


FolderAddRequest: TypeAlias = CommonFolderAdd
FolderAddResponse: TypeAlias = InsertResult
FolderDeleteRequest: TypeAlias = CommonFolderDelete
FolderDeleteResponse: TypeAlias = UpdateResult
FolderEditRequest: TypeAlias = CommonFolderEdit
FolderEditResponse: TypeAlias = UpdateResult
FolderGetRequest: TypeAlias = CommonFolderGet
FolderGetResponse: TypeAlias = CommonFolderRegosOffsettedArrayResult


_MODEL_NAMES = ['CommonFolderAdd', 'CommonFolderDelete', 'CommonFolderEdit', 'CommonFolderGet', 'CommonFolderRegosOffsettedArrayResult']


__all__ = [
    'CommonFolderAdd',
    'CommonFolderDelete',
    'CommonFolderEdit',
    'CommonFolderGet',
    'CommonFolderRegosOffsettedArrayResult',
    'FolderGetRequest',
    'FolderGetResponse',
    'FolderAddRequest',
    'FolderAddResponse',
    'FolderEditRequest',
    'FolderEditResponse',
    'FolderDeleteRequest',
    'FolderDeleteResponse'
]

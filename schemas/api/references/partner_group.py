"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PartnerGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    child_count: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PartnerGroupAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class PartnerGroupArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PartnerGroup] | Error | None = PydField(default=None)


class PartnerGroupDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PartnerGroupEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class PartnerGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


PartnerGroupAddRequest: TypeAlias = PartnerGroupAdd
PartnerGroupAddResponse: TypeAlias = InsertResult
PartnerGroupDeleteRequest: TypeAlias = PartnerGroupDelete
PartnerGroupDeleteResponse: TypeAlias = UpdateResult
PartnerGroupEditRequest: TypeAlias = PartnerGroupEdit
PartnerGroupEditResponse: TypeAlias = UpdateResult
PartnerGroupGetRequest: TypeAlias = PartnerGroupGet
PartnerGroupGetResponse: TypeAlias = PartnerGroupArrayRegosObjectResult


_MODEL_NAMES = ['PartnerGroup', 'PartnerGroupAdd', 'PartnerGroupArrayRegosObjectResult', 'PartnerGroupDelete', 'PartnerGroupEdit', 'PartnerGroupGet']


__all__ = [
    'PartnerGroup',
    'PartnerGroupAdd',
    'PartnerGroupArrayRegosObjectResult',
    'PartnerGroupDelete',
    'PartnerGroupEdit',
    'PartnerGroupGet',
    'PartnerGroupGetRequest',
    'PartnerGroupGetResponse',
    'PartnerGroupAddRequest',
    'PartnerGroupAddResponse',
    'PartnerGroupEditRequest',
    'PartnerGroupEditResponse',
    'PartnerGroupDeleteRequest',
    'PartnerGroupDeleteResponse'
]

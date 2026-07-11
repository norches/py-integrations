"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailCustomerGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    child_count: int | None = PydField(default=None)


class RetailCustomerGroupAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class RetailCustomerGroupArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCustomerGroup] | Error | None = PydField(default=None)


class RetailCustomerGroupDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class RetailCustomerGroupEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class RetailCustomerGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


RetailCustomerGroupAddRequest: TypeAlias = RetailCustomerGroupAdd
RetailCustomerGroupAddResponse: TypeAlias = InsertResult
RetailCustomerGroupDeleteRequest: TypeAlias = RetailCustomerGroupDelete
RetailCustomerGroupDeleteResponse: TypeAlias = UpdateResult
RetailCustomerGroupEditRequest: TypeAlias = RetailCustomerGroupEdit
RetailCustomerGroupEditResponse: TypeAlias = UpdateResult
RetailCustomerGroupGetRequest: TypeAlias = RetailCustomerGroupGet
RetailCustomerGroupGetResponse: TypeAlias = RetailCustomerGroupArrayRegosObjectResult


_MODEL_NAMES = ['RetailCustomerGroup', 'RetailCustomerGroupAdd', 'RetailCustomerGroupArrayRegosObjectResult', 'RetailCustomerGroupDelete', 'RetailCustomerGroupEdit', 'RetailCustomerGroupGet']


__all__ = [
    'RetailCustomerGroup',
    'RetailCustomerGroupAdd',
    'RetailCustomerGroupArrayRegosObjectResult',
    'RetailCustomerGroupDelete',
    'RetailCustomerGroupEdit',
    'RetailCustomerGroupGet',
    'RetailCustomerGroupGetRequest',
    'RetailCustomerGroupGetResponse',
    'RetailCustomerGroupAddRequest',
    'RetailCustomerGroupAddResponse',
    'RetailCustomerGroupEditRequest',
    'RetailCustomerGroupEditResponse',
    'RetailCustomerGroupDeleteRequest',
    'RetailCustomerGroupDeleteResponse'
]

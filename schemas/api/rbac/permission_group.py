"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PermissionGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    order: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PermissionGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class PermissionGroupRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PermissionGroup] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error


PermissionGroupGetRequest: TypeAlias = PermissionGroupGet
PermissionGroupGetResponse: TypeAlias = PermissionGroupRegosArrayResult


_MODEL_NAMES = ['PermissionGroup', 'PermissionGroupGet', 'PermissionGroupRegosArrayResult']


__all__ = [
    'PermissionGroup',
    'PermissionGroupGet',
    'PermissionGroupRegosArrayResult',
    'PermissionGroupGetRequest',
    'PermissionGroupGetResponse'
]

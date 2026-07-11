"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class IntegrationGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    image_url: str | None = PydField(default=None)


class IntegrationGroupGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class IntegrationGroupRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[IntegrationGroup] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error


IntegrationGroupGetRequest: TypeAlias = IntegrationGroupGet
IntegrationGroupGetResponse: TypeAlias = IntegrationGroupRegosArrayResult


_MODEL_NAMES = ['IntegrationGroup', 'IntegrationGroupGet', 'IntegrationGroupRegosArrayResult']


__all__ = [
    'IntegrationGroup',
    'IntegrationGroupGet',
    'IntegrationGroupRegosArrayResult',
    'IntegrationGroupGetRequest',
    'IntegrationGroupGetResponse'
]

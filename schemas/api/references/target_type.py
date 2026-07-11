"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class TargetType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_key: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TargetTypeRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[TargetType] | Error | None = PydField(default=None)


class TargetTypesEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error


TargetTypeGetResponse: TypeAlias = TargetTypeRegosArrayResult


_MODEL_NAMES = ['TargetType', 'TargetTypeRegosArrayResult']


__all__ = [
    'TargetType',
    'TargetTypeRegosArrayResult',
    'TargetTypesEnum',
    'TargetTypeGetResponse'
]

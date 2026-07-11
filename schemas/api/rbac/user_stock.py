"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserStock(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)


class UserStockGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)


class UserStockRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserStock] | Error | None = PydField(default=None)


class UserStockRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserStockSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.references.stock import Stock


UserStockGetRequest: TypeAlias = UserStockGet
UserStockGetResponse: TypeAlias = UserStockRegosArrayResult
UserStockRemoveRequest: TypeAlias = UserStockRemove
UserStockRemoveResponse: TypeAlias = UpdateResult
UserStockSetRequest: TypeAlias = UserStockSet
UserStockSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['UserStock', 'UserStockGet', 'UserStockRegosArrayResult', 'UserStockRemove', 'UserStockSet']


__all__ = [
    'UserStock',
    'UserStockGet',
    'UserStockRegosArrayResult',
    'UserStockRemove',
    'UserStockSet',
    'UserStockGetRequest',
    'UserStockGetResponse',
    'UserStockSetRequest',
    'UserStockSetResponse',
    'UserStockRemoveRequest',
    'UserStockRemoveResponse'
]

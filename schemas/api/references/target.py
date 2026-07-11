"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Target(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    target_type: TargetType | None = PydField(default=None)
    owner: TargetOwnerEnum | None = PydField(default=None)
    period_type: TargetPeriodTypeEnum | None = PydField(default=None)
    period: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    repeateable: bool | None = PydField(default=None)
    finished: bool | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    user: User | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TargetAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    type: TargetTypesEnum | None = PydField(default=None)
    owner: TargetOwnerEnum | None = PydField(default=None)
    period_type: TargetPeriodTypeEnum | None = PydField(default=None)
    period: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    repeateable: bool | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class TargetGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    user_ids: list[int] | None = PydField(default=None)
    finished: bool | None = PydField(default=None)
    owner: TargetOwnerEnum | None = PydField(default=None)


class TargetHistory(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    target: Target | None = PydField(default=None)
    data: list[TargetHistoryItem] | None = PydField(default=None)


class TargetHistoryItem(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    progress: _Decimal | None = PydField(default=None)
    percent: int | None = PydField(default=None)


class TargetHistoryRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: TargetHistory | Error | None = PydField(default=None)


class TargetOwnerEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class TargetPeriodTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TargetRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Target] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.firm import Firm
from schemas.api.references.stock import Stock
from schemas.api.references.target_type import TargetType, TargetTypesEnum


TargetAddRequest: TypeAlias = TargetAdd
TargetAddResponse: TypeAlias = InsertResult
TargetDeleteRequest: TypeAlias = Base_ID
TargetDeleteResponse: TypeAlias = UpdateResult
TargetFinishRequest: TypeAlias = Base_ID
TargetFinishResponse: TypeAlias = UpdateResult
TargetGetHistoryRequest: TypeAlias = Base_ID
TargetGetHistoryResponse: TypeAlias = TargetHistoryRegosObjectResult
TargetGetRequest: TypeAlias = TargetGet
TargetGetResponse: TypeAlias = TargetRegosArrayResult


_MODEL_NAMES = ['Target', 'TargetAdd', 'TargetGet', 'TargetHistory', 'TargetHistoryItem', 'TargetHistoryRegosObjectResult', 'TargetRegosArrayResult']


__all__ = [
    'Target',
    'TargetAdd',
    'TargetGet',
    'TargetHistory',
    'TargetHistoryItem',
    'TargetHistoryRegosObjectResult',
    'TargetOwnerEnum',
    'TargetPeriodTypeEnum',
    'TargetRegosArrayResult',
    'TargetGetRequest',
    'TargetGetResponse',
    'TargetAddRequest',
    'TargetAddResponse',
    'TargetFinishRequest',
    'TargetFinishResponse',
    'TargetDeleteRequest',
    'TargetDeleteResponse',
    'TargetGetHistoryRequest',
    'TargetGetHistoryResponse'
]

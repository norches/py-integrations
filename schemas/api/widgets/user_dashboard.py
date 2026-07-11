"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class UserDashboard(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    dashboard: Dashboard | None = PydField(default=None)


class UserDashboardGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    dashboard_ids: list[int] | None = PydField(default=None)


class UserDashboardRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserDashboard] | Error | None = PydField(default=None)


class UserDashboardRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    dashboard_id: int | None = PydField(default=None)


class UserDashboardSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    dashboard_id: int | None = PydField(default=None)


class UserDashboardSetDefault(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    dashboard_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.widgets.dashboard import Dashboard


UserDashboardGetRequest: TypeAlias = UserDashboardGet
UserDashboardGetResponse: TypeAlias = UserDashboardRegosArrayResult
UserDashboardRemoveRequest: TypeAlias = UserDashboardRemove
UserDashboardRemoveResponse: TypeAlias = UpdateResult
UserDashboardSetDefaultRequest: TypeAlias = UserDashboardSetDefault
UserDashboardSetDefaultResponse: TypeAlias = UpdateResult
UserDashboardSetRequest: TypeAlias = UserDashboardSet
UserDashboardSetResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['UserDashboard', 'UserDashboardGet', 'UserDashboardRegosArrayResult', 'UserDashboardRemove', 'UserDashboardSet', 'UserDashboardSetDefault']


__all__ = [
    'UserDashboard',
    'UserDashboardGet',
    'UserDashboardRegosArrayResult',
    'UserDashboardRemove',
    'UserDashboardSet',
    'UserDashboardSetDefault',
    'UserDashboardGetRequest',
    'UserDashboardGetResponse',
    'UserDashboardSetRequest',
    'UserDashboardSetResponse',
    'UserDashboardRemoveRequest',
    'UserDashboardRemoveResponse',
    'UserDashboardSetDefaultRequest',
    'UserDashboardSetDefaultResponse'
]

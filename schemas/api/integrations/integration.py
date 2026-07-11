"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class IntegrationConnect(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)


class IntegrationConnected(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    is_public: bool | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    alias: str | None = PydField(default=None)
    owner: IntegrationOwnerEnum | None = PydField(default=None)
    handler: IntegrationHandlerEnum | None = PydField(default=None)
    handlers: list[IntegrationHandlerEnum] | None = PydField(default=None)
    scheduled: bool | None = PydField(default=None)
    schedule: IntegrationSchedule | None = PydField(default=None)
    check_enabled: bool | None = PydField(default=None)
    is_active: bool | None = PydField(default=None)
    user: User | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    endpoint: str | None = PydField(default=None)
    webhooks: list[str] | None = PydField(default=None)
    image_url: str | None = PydField(default=None)
    docs_url: str | None = PydField(default=None)
    version: str | None = PydField(default=None)
    has_web_ui: bool | None = PydField(default=None)
    proxy_enabled: bool | None = PydField(default=None)
    web_ui_url: str | None = PydField(default=None)
    has_iap: bool | None = PydField(default=None)
    state: RegosIntegrationIntegrationStateEnum | None = PydField(default=None)


class IntegrationConnectedGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    is_public: bool | None = PydField(default=None)
    keys: list[str] | None = PydField(default=None)
    connected_integration_ids: list[str] | None = PydField(default=None)
    include_schedule: bool | None = PydField(default=None)
    include_name: bool | None = PydField(default=None)
    handler: IntegrationHandlerEnum | None = PydField(default=None)
    handlers: list[IntegrationHandlerEnum] | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class IntegrationConnectedRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[IntegrationConnected] | Error | None = PydField(default=None)


class IntegrationDisconnect(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)


class IntegrationHandlerEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class IntegrationLocalAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    endpoint: str | None = PydField(default=None)
    webhooks: list[str] | None = PydField(default=None)


class IntegrationLocalDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)


class IntegrationLocalEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    endpoint: str | None = PydField(default=None)
    webhooks: list[str] | None = PydField(default=None)


class IntegrationOwnerEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class IntegrationReconnect(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)


class IntegrationSchedule(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    scheduler_uuid: str | None = PydField(default=None)
    period_type: IntegrationSchedulePeriodTypeEnum | None = PydField(default=None)
    period_value: int | None = PydField(default=None)
    last_execute: _DateTime | None = PydField(default=None)


class IntegrationSchedulePeriodTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class IntegrationUnConnected(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    key: str | None = PydField(default=None)
    is_public: bool | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    scheduled: bool | None = PydField(default=None)
    check_enabled: bool | None = PydField(default=None)
    handler: IntegrationHandlerEnum | None = PydField(default=None)
    handlers: list[IntegrationHandlerEnum] | None = PydField(default=None)
    image_url: str | None = PydField(default=None)
    docs_url: str | None = PydField(default=None)
    webhooks: list[str] | None = PydField(default=None)
    version: str | None = PydField(default=None)
    has_web_ui: bool | None = PydField(default=None)
    proxy_enabled: bool | None = PydField(default=None)
    has_iap: bool | None = PydField(default=None)


class IntegrationUnConnectedGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    keys: list[str] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    handlers: list[IntegrationHandlerEnum] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class IntegrationUnConnectedRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[IntegrationUnConnected] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, SingleObjectResult
from schemas.api.integrations.connected_integration import RegosIntegrationIntegrationStateEnum
from schemas.api.rbac.user import User


IntegrationAddRequest: TypeAlias = IntegrationLocalAdd
IntegrationAddResponse: TypeAlias = SingleObjectResult
IntegrationConnectRequest: TypeAlias = IntegrationConnect
IntegrationConnectResponse: TypeAlias = SingleObjectResult
IntegrationDeleteRequest: TypeAlias = IntegrationLocalDelete
IntegrationDeleteResponse: TypeAlias = SingleObjectResult
IntegrationEditRequest: TypeAlias = IntegrationLocalEdit
IntegrationEditResponse: TypeAlias = SingleObjectResult
IntegrationGetRequest: TypeAlias = IntegrationUnConnectedGet
IntegrationGetResponse: TypeAlias = IntegrationUnConnectedRegosOffsettedArrayResult


_MODEL_NAMES = ['IntegrationConnect', 'IntegrationConnected', 'IntegrationConnectedGet', 'IntegrationConnectedRegosArrayResult', 'IntegrationDisconnect', 'IntegrationLocalAdd', 'IntegrationLocalDelete', 'IntegrationLocalEdit', 'IntegrationReconnect', 'IntegrationSchedule', 'IntegrationUnConnected', 'IntegrationUnConnectedGet', 'IntegrationUnConnectedRegosOffsettedArrayResult']


__all__ = [
    'IntegrationConnect',
    'IntegrationConnected',
    'IntegrationConnectedGet',
    'IntegrationConnectedRegosArrayResult',
    'IntegrationDisconnect',
    'IntegrationHandlerEnum',
    'IntegrationLocalAdd',
    'IntegrationLocalDelete',
    'IntegrationLocalEdit',
    'IntegrationOwnerEnum',
    'IntegrationReconnect',
    'IntegrationSchedule',
    'IntegrationSchedulePeriodTypeEnum',
    'IntegrationUnConnected',
    'IntegrationUnConnectedGet',
    'IntegrationUnConnectedRegosOffsettedArrayResult',
    'IntegrationGetRequest',
    'IntegrationGetResponse',
    'IntegrationConnectRequest',
    'IntegrationConnectResponse',
    'IntegrationAddRequest',
    'IntegrationAddResponse',
    'IntegrationEditRequest',
    'IntegrationEditResponse',
    'IntegrationDeleteRequest',
    'IntegrationDeleteResponse'
]

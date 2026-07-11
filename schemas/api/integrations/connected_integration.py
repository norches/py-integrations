"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ConnectedIntegrationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    is_active: bool | None = PydField(default=None)
    alias: str | None = PydField(default=None)
    settings: list[ConnectedIntegrationSettingEdit] | None = PydField(default=None)
    schedule: IntegrationSchedule | None = PydField(default=None)


class ConnectedIntegrationID(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    connected_integration_id: str | None = PydField(default=None)


class ConnectedIntegrationWebhookInfoGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    connected_integration_id: str | None = PydField(default=None)


class RegosIntegrationIntegrationStateEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BooleanRegosObjectResult, SingleObjectResult
from schemas.api.integrations.connected_integration_setting import ConnectedIntegrationSettingEdit
from schemas.api.integrations.integration import IntegrationConnectedGet, IntegrationConnectedRegosArrayResult, IntegrationDisconnect, IntegrationReconnect, IntegrationSchedule
from schemas.api.webhooks.webhook import WebHookStatusResponseRegosObjectResult


ConnectedIntegrationCheckRequest: TypeAlias = ConnectedIntegrationID
ConnectedIntegrationCheckResponse: TypeAlias = BooleanRegosObjectResult
ConnectedIntegrationDisconnectRequest: TypeAlias = IntegrationDisconnect
ConnectedIntegrationDisconnectResponse: TypeAlias = SingleObjectResult
ConnectedIntegrationEditRequest: TypeAlias = ConnectedIntegrationEdit
ConnectedIntegrationEditResponse: TypeAlias = SingleObjectResult
ConnectedIntegrationGetRequest: TypeAlias = IntegrationConnectedGet
ConnectedIntegrationGetResponse: TypeAlias = IntegrationConnectedRegosArrayResult
ConnectedIntegrationGetWebhookInfoRequest: TypeAlias = ConnectedIntegrationWebhookInfoGet
ConnectedIntegrationGetWebhookInfoResponse: TypeAlias = WebHookStatusResponseRegosObjectResult
ConnectedIntegrationReconnectRequest: TypeAlias = IntegrationReconnect
ConnectedIntegrationReconnectResponse: TypeAlias = SingleObjectResult


_MODEL_NAMES = ['ConnectedIntegrationEdit', 'ConnectedIntegrationID', 'ConnectedIntegrationWebhookInfoGet']


__all__ = [
    'ConnectedIntegrationEdit',
    'ConnectedIntegrationID',
    'ConnectedIntegrationWebhookInfoGet',
    'RegosIntegrationIntegrationStateEnum',
    'ConnectedIntegrationGetRequest',
    'ConnectedIntegrationGetResponse',
    'ConnectedIntegrationEditRequest',
    'ConnectedIntegrationEditResponse',
    'ConnectedIntegrationCheckRequest',
    'ConnectedIntegrationCheckResponse',
    'ConnectedIntegrationReconnectRequest',
    'ConnectedIntegrationReconnectResponse',
    'ConnectedIntegrationDisconnectRequest',
    'ConnectedIntegrationDisconnectResponse',
    'ConnectedIntegrationGetWebhookInfoRequest',
    'ConnectedIntegrationGetWebhookInfoResponse'
]

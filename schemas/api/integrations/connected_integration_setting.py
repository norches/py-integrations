"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ConnectedIntegrationSetting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ConnectedIntegrationSettingEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class ConnectedIntegrationSettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class ConnectedIntegrationSettingRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ConnectedIntegrationSetting] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, SingleObjectResult




class ConnectedIntegrationSettingEditRequest(RootModel[list[ConnectedIntegrationSettingEdit]]):
    """Compatibility root model for ConnectedIntegrationSetting/Edit."""

    pass


ConnectedIntegrationSettingEditItem: TypeAlias = ConnectedIntegrationSettingEdit
ConnectedIntegrationSettingEditResponse: TypeAlias = SingleObjectResult
ConnectedIntegrationSettingGetRequest: TypeAlias = ConnectedIntegrationSettingGet
ConnectedIntegrationSettingGetResponse: TypeAlias = ConnectedIntegrationSettingRegosArrayResult
ConnectedIntegrationSettingRequest: TypeAlias = ConnectedIntegrationSettingGet


_MODEL_NAMES = ['ConnectedIntegrationSetting', 'ConnectedIntegrationSettingEdit', 'ConnectedIntegrationSettingGet', 'ConnectedIntegrationSettingRegosArrayResult', 'ConnectedIntegrationSettingEditRequest']


__all__ = [
    'ConnectedIntegrationSetting',
    'ConnectedIntegrationSettingEdit',
    'ConnectedIntegrationSettingGet',
    'ConnectedIntegrationSettingRegosArrayResult',
    'ConnectedIntegrationSettingEditRequest',
    'ConnectedIntegrationSettingGetRequest',
    'ConnectedIntegrationSettingGetResponse',
    'ConnectedIntegrationSettingEditRequest',
    'ConnectedIntegrationSettingEditResponse',
    'ConnectedIntegrationSettingEditItem',
    'ConnectedIntegrationSettingRequest'
]

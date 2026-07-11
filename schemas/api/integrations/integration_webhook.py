"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class IntegrationWebhook(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    name: str | None = PydField(default=None)
    order: int | None = PydField(default=None)


class IntegrationWebhookRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[IntegrationWebhook] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error


IntegrationWebhookGetResponse: TypeAlias = IntegrationWebhookRegosArrayResult


_MODEL_NAMES = ['IntegrationWebhook', 'IntegrationWebhookRegosArrayResult']


__all__ = [
    'IntegrationWebhook',
    'IntegrationWebhookRegosArrayResult',
    'IntegrationWebhookGetResponse'
]

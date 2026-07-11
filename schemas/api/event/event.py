"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class EventGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    connected_integration_id: str | None = PydField(default=None)
    last_event_id: str | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    actions: list[WebHookActionsEnum] | None = PydField(default=None)


class EventGetResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    events: list[EventItem] | None = PydField(default=None)
    next_event_id: str | None = PydField(default=None)
    has_more: bool | None = PydField(default=None)


class EventGetResultRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: EventGetResult | Error | None = PydField(default=None)


class EventItem(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    event_id: str | None = PydField(default=None)
    occurred_at: _DateTime | None = PydField(default=None)
    action: WebHookActionsEnum | None = PydField(default=None)
    data: Any = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.webhooks.webhook import WebHookActionsEnum


EventGetRequest: TypeAlias = EventGet
EventGetResponse: TypeAlias = EventGetResultRegosObjectResult


_MODEL_NAMES = ['EventGet', 'EventGetResult', 'EventGetResultRegosObjectResult', 'EventItem']


__all__ = [
    'EventGet',
    'EventGetResult',
    'EventGetResultRegosObjectResult',
    'EventItem',
    'EventGetRequest',
    'EventGetResponse'
]

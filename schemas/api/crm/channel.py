"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Channel(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    queue_mode: QueueModeEnum | None = PydField(default=None)
    routing_strategy: RoutingStrategyEnum | None = PydField(default=None)
    first_response_sec: int | None = PydField(default=None)
    next_response_sec: int | None = PydField(default=None)
    resolve_sec: int | None = PydField(default=None)
    pause_on_waiting_client: bool | None = PydField(default=None)
    start_message: str | None = PydField(default=None)
    end_message: str | None = PydField(default=None)
    off_hours_message: str | None = PydField(default=None)
    rating_enabled: bool | None = PydField(default=None)
    rating_message: str | None = PydField(default=None)
    rating_positive_message: str | None = PydField(default=None)
    rating_negative_message: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    operators: list[ChannelOperator] | None = PydField(default=None)
    intervals: list[ChannelScheduleInterval] | None = PydField(default=None)


class ChannelAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    queue_mode: QueueModeEnum | None = PydField(default=None)
    routing_strategy: RoutingStrategyEnum | None = PydField(default=None)
    first_response_sec: int | None = PydField(default=None)
    next_response_sec: int | None = PydField(default=None)
    resolve_sec: int | None = PydField(default=None)
    pause_on_waiting_client: bool | None = PydField(default=None)
    start_message: str | None = PydField(default=None)
    end_message: str | None = PydField(default=None)
    off_hours_message: str | None = PydField(default=None)
    rating_enabled: bool | None = PydField(default=None)
    rating_message: str | None = PydField(default=None)
    rating_positive_message: str | None = PydField(default=None)
    rating_negative_message: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class ChannelDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ChannelEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    queue_mode: QueueModeEnum | None = PydField(default=None)
    routing_strategy: RoutingStrategyEnum | None = PydField(default=None)
    first_response_sec: int | None = PydField(default=None)
    next_response_sec: int | None = PydField(default=None)
    resolve_sec: int | None = PydField(default=None)
    pause_on_waiting_client: bool | None = PydField(default=None)
    start_message: str | None = PydField(default=None)
    end_message: str | None = PydField(default=None)
    off_hours_message: str | None = PydField(default=None)
    rating_enabled: bool | None = PydField(default=None)
    rating_message: str | None = PydField(default=None)
    rating_positive_message: str | None = PydField(default=None)
    rating_negative_message: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class ChannelGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ChannelOperator(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    channel_id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    sort_order: int | None = PydField(default=None)
    max_active_leads: int | None = PydField(default=None)
    is_active: bool | None = PydField(default=None)
    joined_date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ChannelRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Channel] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ChannelScheduleInterval(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    channel_id: int | None = PydField(default=None)
    day_of_week: int | None = PydField(default=None)
    start_minute: int | None = PydField(default=None)
    end_minute: int | None = PydField(default=None)
    cross_day: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ChannelSetInterval(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    day_of_week: int | None = PydField(default=None)
    start_minute: int | None = PydField(default=None)
    end_minute: int | None = PydField(default=None)
    cross_day: bool | None = PydField(default=None)


class ChannelSetIntervals(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    channel_id: int | None = PydField(default=None)
    intervals: list[ChannelSetInterval] | None = PydField(default=None)


class ChannelSetOperator(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    sort_order: int | None = PydField(default=None)
    max_active_leads: int | None = PydField(default=None)
    is_active: bool | None = PydField(default=None)


class ChannelSetOperators(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    channel_id: int | None = PydField(default=None)
    operators: list[ChannelSetOperator] | None = PydField(default=None)


class QueueModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class RoutingStrategyEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


ChannelAddRequest: TypeAlias = ChannelAdd
ChannelAddResponse: TypeAlias = InsertResult
ChannelDeleteRequest: TypeAlias = ChannelDelete
ChannelDeleteResponse: TypeAlias = UpdateResult
ChannelEditRequest: TypeAlias = ChannelEdit
ChannelEditResponse: TypeAlias = UpdateResult
ChannelGetRequest: TypeAlias = ChannelGet
ChannelGetResponse: TypeAlias = ChannelRegosOffsettedArrayResult
ChannelSetIntervalsRequest: TypeAlias = ChannelSetIntervals
ChannelSetIntervalsResponse: TypeAlias = UpdateResult
ChannelSetOperatorsRequest: TypeAlias = ChannelSetOperators
ChannelSetOperatorsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Channel', 'ChannelAdd', 'ChannelDelete', 'ChannelEdit', 'ChannelGet', 'ChannelOperator', 'ChannelRegosOffsettedArrayResult', 'ChannelScheduleInterval', 'ChannelSetInterval', 'ChannelSetIntervals', 'ChannelSetOperator', 'ChannelSetOperators']


__all__ = [
    'Channel',
    'ChannelAdd',
    'ChannelDelete',
    'ChannelEdit',
    'ChannelGet',
    'ChannelOperator',
    'ChannelRegosOffsettedArrayResult',
    'ChannelScheduleInterval',
    'ChannelSetInterval',
    'ChannelSetIntervals',
    'ChannelSetOperator',
    'ChannelSetOperators',
    'QueueModeEnum',
    'RoutingStrategyEnum',
    'ChannelGetRequest',
    'ChannelGetResponse',
    'ChannelAddRequest',
    'ChannelAddResponse',
    'ChannelEditRequest',
    'ChannelEditResponse',
    'ChannelDeleteRequest',
    'ChannelDeleteResponse',
    'ChannelSetOperatorsRequest',
    'ChannelSetOperatorsResponse',
    'ChannelSetIntervalsRequest',
    'ChannelSetIntervalsResponse'
]

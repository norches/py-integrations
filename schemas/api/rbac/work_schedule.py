"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class WorkSchedule(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    schedule_type: WorkScheduleTypeEnum | None = PydField(default=None)
    is_account_default: bool | None = PydField(default=None)
    check_in_early_sec: int | None = PydField(default=None)
    check_in_late_sec: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class WorkScheduleAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    schedule_type: WorkScheduleTypeEnum | None = PydField(default=None)
    is_account_default: bool | None = PydField(default=None)
    check_in_early_sec: int | None = PydField(default=None)
    check_in_late_sec: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class WorkScheduleDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class WorkScheduleEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    schedule_type: WorkScheduleTypeEnum | None = PydField(default=None)
    check_in_early_sec: int | None = PydField(default=None)
    check_in_late_sec: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class WorkScheduleException(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    schedule_id: int | None = PydField(default=None)
    date: str | None = PydField(default=None)
    is_working_day: bool | None = PydField(default=None)
    start_minute: int | None = PydField(default=None)
    end_minute: int | None = PydField(default=None)
    comment: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class WorkScheduleExceptionRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[WorkScheduleException] | Error | None = PydField(default=None)


class WorkScheduleExceptionSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: str | None = PydField(default=None)
    is_working_day: bool | None = PydField(default=None)
    start_minute: int | None = PydField(default=None)
    end_minute: int | None = PydField(default=None)
    comment: str | None = PydField(default=None)


class WorkScheduleGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class WorkScheduleGetExceptions(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    schedule_id: int | None = PydField(default=None)


class WorkScheduleGetIntervals(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    schedule_id: int | None = PydField(default=None)


class WorkScheduleInterval(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    schedule_id: int | None = PydField(default=None)
    day_of_week: int | None = PydField(default=None)
    start_minute: int | None = PydField(default=None)
    end_minute: int | None = PydField(default=None)
    cross_day: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class WorkScheduleIntervalRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[WorkScheduleInterval] | Error | None = PydField(default=None)


class WorkScheduleIntervalSet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    day_of_week: int | None = PydField(default=None)
    start_minute: int | None = PydField(default=None)
    end_minute: int | None = PydField(default=None)
    cross_day: bool | None = PydField(default=None)


class WorkScheduleRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[WorkSchedule] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class WorkScheduleSetDefault(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class WorkScheduleSetExceptions(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    schedule_id: int | None = PydField(default=None)
    exceptions: list[WorkScheduleExceptionSet] | None = PydField(default=None)


class WorkScheduleSetIntervals(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    schedule_id: int | None = PydField(default=None)
    intervals: list[WorkScheduleIntervalSet] | None = PydField(default=None)


class WorkScheduleTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult


WorkScheduleAddRequest: TypeAlias = WorkScheduleAdd
WorkScheduleAddResponse: TypeAlias = InsertResult
WorkScheduleDeleteRequest: TypeAlias = WorkScheduleDelete
WorkScheduleDeleteResponse: TypeAlias = UpdateResult
WorkScheduleEditRequest: TypeAlias = WorkScheduleEdit
WorkScheduleEditResponse: TypeAlias = UpdateResult
WorkScheduleGetExceptionsRequest: TypeAlias = WorkScheduleGetExceptions
WorkScheduleGetExceptionsResponse: TypeAlias = WorkScheduleExceptionRegosArrayResult
WorkScheduleGetIntervalsRequest: TypeAlias = WorkScheduleGetIntervals
WorkScheduleGetIntervalsResponse: TypeAlias = WorkScheduleIntervalRegosArrayResult
WorkScheduleGetRequest: TypeAlias = WorkScheduleGet
WorkScheduleGetResponse: TypeAlias = WorkScheduleRegosOffsettedArrayResult
WorkScheduleSetDefaultRequest: TypeAlias = WorkScheduleSetDefault
WorkScheduleSetDefaultResponse: TypeAlias = UpdateResult
WorkScheduleSetExceptionsRequest: TypeAlias = WorkScheduleSetExceptions
WorkScheduleSetExceptionsResponse: TypeAlias = UpdateResult
WorkScheduleSetIntervalsRequest: TypeAlias = WorkScheduleSetIntervals
WorkScheduleSetIntervalsResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['WorkSchedule', 'WorkScheduleAdd', 'WorkScheduleDelete', 'WorkScheduleEdit', 'WorkScheduleException', 'WorkScheduleExceptionRegosArrayResult', 'WorkScheduleExceptionSet', 'WorkScheduleGet', 'WorkScheduleGetExceptions', 'WorkScheduleGetIntervals', 'WorkScheduleInterval', 'WorkScheduleIntervalRegosArrayResult', 'WorkScheduleIntervalSet', 'WorkScheduleRegosOffsettedArrayResult', 'WorkScheduleSetDefault', 'WorkScheduleSetExceptions', 'WorkScheduleSetIntervals']


__all__ = [
    'WorkSchedule',
    'WorkScheduleAdd',
    'WorkScheduleDelete',
    'WorkScheduleEdit',
    'WorkScheduleException',
    'WorkScheduleExceptionRegosArrayResult',
    'WorkScheduleExceptionSet',
    'WorkScheduleGet',
    'WorkScheduleGetExceptions',
    'WorkScheduleGetIntervals',
    'WorkScheduleInterval',
    'WorkScheduleIntervalRegosArrayResult',
    'WorkScheduleIntervalSet',
    'WorkScheduleRegosOffsettedArrayResult',
    'WorkScheduleSetDefault',
    'WorkScheduleSetExceptions',
    'WorkScheduleSetIntervals',
    'WorkScheduleTypeEnum',
    'WorkScheduleGetRequest',
    'WorkScheduleGetResponse',
    'WorkScheduleGetIntervalsRequest',
    'WorkScheduleGetIntervalsResponse',
    'WorkScheduleGetExceptionsRequest',
    'WorkScheduleGetExceptionsResponse',
    'WorkScheduleAddRequest',
    'WorkScheduleAddResponse',
    'WorkScheduleEditRequest',
    'WorkScheduleEditResponse',
    'WorkScheduleDeleteRequest',
    'WorkScheduleDeleteResponse',
    'WorkScheduleSetDefaultRequest',
    'WorkScheduleSetDefaultResponse',
    'WorkScheduleSetIntervalsRequest',
    'WorkScheduleSetIntervalsResponse',
    'WorkScheduleSetExceptionsRequest',
    'WorkScheduleSetExceptionsResponse'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class SingleSms(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    entity_type: SingleSmsEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    status: SingleSmsStatusEnum | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    message: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class SingleSmsAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: SingleSmsEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)
    message: str | None = PydField(default=None)


class SingleSmsEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class SingleSmsGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    entity_type: SingleSmsEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)
    status: SingleSmsStatusEnum | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class SingleSmsRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[SingleSms] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class SingleSmsSetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    status: SingleSmsStatusEnum | None = PydField(default=None)
    error_message: str | None = PydField(default=None)


class SingleSmsStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, ObjectRegosObjectResult


SmsAddRequest: TypeAlias = SingleSmsAdd
SmsAddResponse: TypeAlias = InsertResult
SmsGetRequest: TypeAlias = SingleSmsGet
SmsGetResponse: TypeAlias = SingleSmsRegosOffsettedArrayResult
SmsSetStatusRequest: TypeAlias = SingleSmsSetStatus
SmsSetStatusResponse: TypeAlias = ObjectRegosObjectResult


_MODEL_NAMES = ['SingleSms', 'SingleSmsAdd', 'SingleSmsGet', 'SingleSmsRegosOffsettedArrayResult', 'SingleSmsSetStatus']


__all__ = [
    'SingleSms',
    'SingleSmsAdd',
    'SingleSmsEntityTypeEnum',
    'SingleSmsGet',
    'SingleSmsRegosOffsettedArrayResult',
    'SingleSmsSetStatus',
    'SingleSmsStatusEnum',
    'SmsGetRequest',
    'SmsGetResponse',
    'SmsAddRequest',
    'SmsAddResponse',
    'SmsSetStatusRequest',
    'SmsSetStatusResponse'
]

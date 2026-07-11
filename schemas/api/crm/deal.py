"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Deal(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    client_id: int | None = PydField(default=None)
    client: Client | None = PydField(default=None)
    task_id: int | None = PydField(default=None)
    lead_id: int | None = PydField(default=None)
    ticket_id: int | None = PydField(default=None)
    source_deal_id: int | None = PydField(default=None)
    deal_type_id: int | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    status: DealStatusEnum | None = PydField(default=None)
    title: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMention] | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    open_date: int | None = PydField(default=None)
    close_date: int | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)


class DealAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    source_lead_id: int | None = PydField(default=None)
    ticket_id: int | None = PydField(default=None)
    source_deal_id: int | None = PydField(default=None)
    client_id: int | None = PydField(default=None)
    task_id: int | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    lead_id: int | None = PydField(default=None)
    deal_type_id: int | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    title: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class DealClose(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)


class DealDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DealEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    task_id: int | None = PydField(default=None)
    deal_type_id: int | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    title: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class DealGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    client_ids: list[int] | None = PydField(default=None)
    task_ids: list[int] | None = PydField(default=None)
    lead_ids: list[int] | None = PydField(default=None)
    responsible_user_ids: list[int] | None = PydField(default=None)
    stage_ids: list[int] | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    to_date: int | None = PydField(default=None)
    include_mentions: bool | None = PydField(default=None)
    statuses: list[DealStatusEnum] | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DealRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Deal] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DealSetParticipants(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    replace_mode: bool | None = PydField(default=None)


class DealSetResponsible(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)


class DealSetStage(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    comment: str | None = PydField(default=None)


class DealStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CommonMention, CommonMentionInput, CommonMentionOptions, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.crm.client import Client
from schemas.api.references.currency import Currency
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit


DealAddRequest: TypeAlias = DealAdd
DealAddResponse: TypeAlias = InsertResult
DealCloseRequest: TypeAlias = DealClose
DealCloseResponse: TypeAlias = UpdateResult
DealDeleteRequest: TypeAlias = DealDelete
DealDeleteResponse: TypeAlias = UpdateResult
DealEditRequest: TypeAlias = DealEdit
DealEditResponse: TypeAlias = UpdateResult
DealGetRequest: TypeAlias = DealGet
DealGetResponse: TypeAlias = DealRegosOffsettedArrayResult
DealSetParticipantsRequest: TypeAlias = DealSetParticipants
DealSetParticipantsResponse: TypeAlias = UpdateResult
DealSetResponsibleRequest: TypeAlias = DealSetResponsible
DealSetResponsibleResponse: TypeAlias = UpdateResult
DealSetStageRequest: TypeAlias = DealSetStage
DealSetStageResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Deal', 'DealAdd', 'DealClose', 'DealDelete', 'DealEdit', 'DealGet', 'DealRegosOffsettedArrayResult', 'DealSetParticipants', 'DealSetResponsible', 'DealSetStage']


__all__ = [
    'Deal',
    'DealAdd',
    'DealClose',
    'DealDelete',
    'DealEdit',
    'DealGet',
    'DealRegosOffsettedArrayResult',
    'DealSetParticipants',
    'DealSetResponsible',
    'DealSetStage',
    'DealStatusEnum',
    'DealGetRequest',
    'DealGetResponse',
    'DealAddRequest',
    'DealAddResponse',
    'DealEditRequest',
    'DealEditResponse',
    'DealSetStageRequest',
    'DealSetStageResponse',
    'DealSetResponsibleRequest',
    'DealSetResponsibleResponse',
    'DealSetParticipantsRequest',
    'DealSetParticipantsResponse',
    'DealCloseRequest',
    'DealCloseResponse',
    'DealDeleteRequest',
    'DealDeleteResponse'
]

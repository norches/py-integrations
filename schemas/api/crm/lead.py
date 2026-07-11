"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Lead(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    client_id: int | None = PydField(default=None)
    client: Client | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    status: LeadStatusEnum | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    responsible_hold_until: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    title: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMention] | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    client_name: str | None = PydField(default=None)
    client_phone: str | None = PydField(default=None)
    client_photo_url: str | None = PydField(default=None)
    first_response_date: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    rating: int | None = PydField(default=None)
    rating_comment: str | None = PydField(default=None)
    first_response_due_date: int | None = PydField(default=None)
    resolve_due_date: int | None = PydField(default=None)
    sla_breached: bool | None = PydField(default=None)
    sla_breached_date: int | None = PydField(default=None)
    converted_deal_id: int | None = PydField(default=None)
    repeat_of_lead_id: int | None = PydField(default=None)
    ticket_id: int | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)


class LeadAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    client_id: int | None = PydField(default=None)
    ticket_id: int | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    title: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    client_name: str | None = PydField(default=None)
    client_phone: str | None = PydField(default=None)
    client_photo_url: str | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)
    copy_from_repeat: bool | None = PydField(default=None)


class LeadClose(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)


class LeadConvert(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    target_entity_type: CrmEntityTypeEnum | None = PydField(default=None)
    deal_type_id: int | None = PydField(default=None)
    deal_title: str | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class LeadDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class LeadEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    title: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    client_name: str | None = PydField(default=None)
    client_phone: str | None = PydField(default=None)
    client_photo_url: str | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class LeadGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    client_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    responsible_user_ids: list[int] | None = PydField(default=None)
    stage_ids: list[int] | None = PydField(default=None)
    statuses: list[LeadStatusEnum] | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    to_date: int | None = PydField(default=None)
    include_mentions: bool | None = PydField(default=None)
    sla_breached: bool | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class LeadRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Lead] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class LeadSetParticipants(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    replace_mode: bool | None = PydField(default=None)


class LeadSetResponsible(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)


class LeadSetStage(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stage_id: int | None = PydField(default=None)
    comment: str | None = PydField(default=None)


class LeadStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CommonMention, CommonMentionInput, CommonMentionOptions, CrmEntityTypeEnum, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.crm.client import Client
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit


LeadAddRequest: TypeAlias = LeadAdd
LeadAddResponse: TypeAlias = InsertResult
LeadCloseRequest: TypeAlias = LeadClose
LeadCloseResponse: TypeAlias = UpdateResult
LeadConvertRequest: TypeAlias = LeadConvert
LeadConvertResponse: TypeAlias = InsertResult
LeadDeleteRequest: TypeAlias = LeadDelete
LeadDeleteResponse: TypeAlias = UpdateResult
LeadEditRequest: TypeAlias = LeadEdit
LeadEditResponse: TypeAlias = UpdateResult
LeadGetRequest: TypeAlias = LeadGet
LeadGetResponse: TypeAlias = LeadRegosOffsettedArrayResult
LeadSetParticipantsRequest: TypeAlias = LeadSetParticipants
LeadSetParticipantsResponse: TypeAlias = UpdateResult
LeadSetResponsibleRequest: TypeAlias = LeadSetResponsible
LeadSetResponsibleResponse: TypeAlias = UpdateResult
LeadSetStageRequest: TypeAlias = LeadSetStage
LeadSetStageResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Lead', 'LeadAdd', 'LeadClose', 'LeadConvert', 'LeadDelete', 'LeadEdit', 'LeadGet', 'LeadRegosOffsettedArrayResult', 'LeadSetParticipants', 'LeadSetResponsible', 'LeadSetStage']


__all__ = [
    'Lead',
    'LeadAdd',
    'LeadClose',
    'LeadConvert',
    'LeadDelete',
    'LeadEdit',
    'LeadGet',
    'LeadRegosOffsettedArrayResult',
    'LeadSetParticipants',
    'LeadSetResponsible',
    'LeadSetStage',
    'LeadStatusEnum',
    'LeadGetRequest',
    'LeadGetResponse',
    'LeadAddRequest',
    'LeadAddResponse',
    'LeadEditRequest',
    'LeadEditResponse',
    'LeadSetStageRequest',
    'LeadSetStageResponse',
    'LeadSetResponsibleRequest',
    'LeadSetResponsibleResponse',
    'LeadSetParticipantsRequest',
    'LeadSetParticipantsResponse',
    'LeadCloseRequest',
    'LeadCloseResponse',
    'LeadDeleteRequest',
    'LeadDeleteResponse',
    'LeadConvertRequest',
    'LeadConvertResponse'
]

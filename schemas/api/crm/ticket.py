"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Ticket(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    client_id: int | None = PydField(default=None)
    client: Client | None = PydField(default=None)
    channel_id: int | None = PydField(default=None)
    direction: TicketDirectionEnum | None = PydField(default=None)
    external_dialog_id: str | None = PydField(default=None)
    subject: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMention] | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    status: TicketStatusEnum | None = PydField(default=None)
    first_response_date: int | None = PydField(default=None)
    first_response_due_date: int | None = PydField(default=None)
    resolve_due_date: int | None = PydField(default=None)
    sla_breached: bool | None = PydField(default=None)
    sla_breached_date: int | None = PydField(default=None)
    resolved_date: int | None = PydField(default=None)
    missed: bool | None = PydField(default=None)
    rating: int | None = PydField(default=None)
    rating_comment: str | None = PydField(default=None)
    client_sentiment_score: int | None = PydField(default=None)
    client_sentiment_comment: str | None = PydField(default=None)
    client_sentiment_user_id: int | None = PydField(default=None)
    client_sentiment_date: int | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    created_date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class TicketAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    client_id: int | None = PydField(default=None)
    channel_id: int | None = PydField(default=None)
    direction: TicketDirectionEnum | None = PydField(default=None)
    external_dialog_id: str | None = PydField(default=None)
    subject: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class TicketClose(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    resolved_date: int | None = PydField(default=None)


class TicketDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class TicketDirectionEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class TicketEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    direction: TicketDirectionEnum | None = PydField(default=None)
    subject: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class TicketGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    client_ids: list[int] | None = PydField(default=None)
    channel_ids: list[int] | None = PydField(default=None)
    external_dialog_id: str | None = PydField(default=None)
    responsible_user_ids: list[int] | None = PydField(default=None)
    statuses: list[TicketStatusEnum] | None = PydField(default=None)
    direction: TicketDirectionEnum | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    to_date: int | None = PydField(default=None)
    include_mentions: bool | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    sort_orders: list[TicketSortColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class TicketRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Ticket] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class TicketSetClientSentiment(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    sentiment_score: int | None = PydField(default=None)
    sentiment_comment: str | None = PydField(default=None)


class TicketSetParticipants(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    participant_user_ids: list[int] | None = PydField(default=None)
    replace_mode: bool | None = PydField(default=None)


class TicketSetRating(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    rating: int | None = PydField(default=None)
    rating_comment: str | None = PydField(default=None)


class TicketSetResponsible(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)


class TicketSetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    status: TicketStatusEnum | None = PydField(default=None)


class TicketSortColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: TicketSortOrderColumnsEnum | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class TicketSortOrderColumnsEnum(IntEnum):
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
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19


class TicketStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, CommonMention, CommonMentionInput, CommonMentionOptions, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.crm.client import Client
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit


TicketAddRequest: TypeAlias = TicketAdd
TicketAddResponse: TypeAlias = InsertResult
TicketCloseRequest: TypeAlias = TicketClose
TicketCloseResponse: TypeAlias = UpdateResult
TicketDeleteRequest: TypeAlias = TicketDelete
TicketDeleteResponse: TypeAlias = UpdateResult
TicketEditRequest: TypeAlias = TicketEdit
TicketEditResponse: TypeAlias = UpdateResult
TicketGetRequest: TypeAlias = TicketGet
TicketGetResponse: TypeAlias = TicketRegosOffsettedArrayResult
TicketSetClientSentimentRequest: TypeAlias = TicketSetClientSentiment
TicketSetClientSentimentResponse: TypeAlias = UpdateResult
TicketSetParticipantsRequest: TypeAlias = TicketSetParticipants
TicketSetParticipantsResponse: TypeAlias = UpdateResult
TicketSetRatingRequest: TypeAlias = TicketSetRating
TicketSetRatingResponse: TypeAlias = UpdateResult
TicketSetResponsibleRequest: TypeAlias = TicketSetResponsible
TicketSetResponsibleResponse: TypeAlias = UpdateResult
TicketSetStatusRequest: TypeAlias = TicketSetStatus
TicketSetStatusResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Ticket', 'TicketAdd', 'TicketClose', 'TicketDelete', 'TicketEdit', 'TicketGet', 'TicketRegosOffsettedArrayResult', 'TicketSetClientSentiment', 'TicketSetParticipants', 'TicketSetRating', 'TicketSetResponsible', 'TicketSetStatus', 'TicketSortColumn']


__all__ = [
    'Ticket',
    'TicketAdd',
    'TicketClose',
    'TicketDelete',
    'TicketDirectionEnum',
    'TicketEdit',
    'TicketGet',
    'TicketRegosOffsettedArrayResult',
    'TicketSetClientSentiment',
    'TicketSetParticipants',
    'TicketSetRating',
    'TicketSetResponsible',
    'TicketSetStatus',
    'TicketSortColumn',
    'TicketSortOrderColumnsEnum',
    'TicketStatusEnum',
    'TicketGetRequest',
    'TicketGetResponse',
    'TicketAddRequest',
    'TicketAddResponse',
    'TicketEditRequest',
    'TicketEditResponse',
    'TicketSetResponsibleRequest',
    'TicketSetResponsibleResponse',
    'TicketSetParticipantsRequest',
    'TicketSetParticipantsResponse',
    'TicketSetStatusRequest',
    'TicketSetStatusResponse',
    'TicketSetRatingRequest',
    'TicketSetRatingResponse',
    'TicketSetClientSentimentRequest',
    'TicketSetClientSentimentResponse',
    'TicketCloseRequest',
    'TicketCloseResponse',
    'TicketDeleteRequest',
    'TicketDeleteResponse'
]

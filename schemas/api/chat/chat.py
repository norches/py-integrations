"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Chat(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: str | None = PydField(default=None)
    chat_type: ChatTypeEnum | None = PydField(default=None)
    name: str | None = PydField(default=None)
    logo_url: str | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    last_message_id: str | None = PydField(default=None)
    last_message_date: int | None = PydField(default=None)
    last_message_text: str | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    closed: bool | None = PydField(default=None)
    closed_date: int | None = PydField(default=None)
    participants: list[ChatParticipant] | None = PydField(default=None)
    entity_type: ChatLinkedEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)
    unread_count: int | None = PydField(default=None)
    muted: bool | None = PydField(default=None)
    archived: bool | None = PydField(default=None)
    pinned: bool | None = PydField(default=None)


class ChatAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    logo_url: str | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    chat_type: ChatTypeEnum | None = PydField(default=None)
    participants: list[ChatParticipantAddEdit] | None = PydField(default=None)


class ChatAddBot(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)


class ChatAddParticipant(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    participant: ChatParticipantAddEdit | None = PydField(default=None)


class ChatAvailableReaction(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    reaction: str | None = PydField(default=None)
    sort_order: int | None = PydField(default=None)


class ChatAvailableReactionRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatAvailableReaction] | Error | None = PydField(default=None)


class ChatEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    logo_url: str | None = PydField(default=None)
    external_id: str | None = PydField(default=None)


class ChatEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_6 = 6


class ChatGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[str] | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    chat_type: ChatTypeEnum | None = PydField(default=None)
    participant_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    participant_entity_id: int | None = PydField(default=None)
    search: str | None = PydField(default=None)
    closed: bool | None = PydField(default=None)
    archived: bool | None = PydField(default=None)
    pinned: bool | None = PydField(default=None)
    entity_type: ChatLinkedEntityTypeEnum | None = PydField(default=None)
    entity_bound: bool | None = PydField(default=None)
    sort_orders: list[ChatOrder] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ChatGetAvailableReactions(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)


class ChatJoin(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)


class ChatLeave(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)


class ChatLinkedEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_11 = 11


class ChatOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: ChatOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class ChatOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class ChatParticipant(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)
    role: ChatParticipantRoleEnum | None = PydField(default=None)
    name: str | None = PydField(default=None)
    photo_url: str | None = PydField(default=None)
    joined_date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ChatParticipantAddEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)
    role: ChatParticipantRoleEnum | None = PydField(default=None)


class ChatParticipantRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    entity_id: int | None = PydField(default=None)


class ChatParticipantRoleEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ChatRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Chat] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ChatRemoveParticipants(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    participants: list[ChatParticipantRemove] | None = PydField(default=None)


class ChatSetArchived(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    archived: bool | None = PydField(default=None)


class ChatSetAvailableReactions(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    reactions: list[str] | None = PydField(default=None)


class ChatSetMuted(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    muted: bool | None = PydField(default=None)


class ChatSetParticipants(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    participants: list[ChatParticipantAddEdit] | None = PydField(default=None)


class ChatSetPinned(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    pinned: bool | None = PydField(default=None)


class ChatTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ChatUnreadCount(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    unread_count: int | None = PydField(default=None)


class ChatUnreadCountByKey(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    key: str | None = PydField(default=None)
    unread_count: int | None = PydField(default=None)


class ChatUnreadCountByKeyRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatUnreadCountByKey] | Error | None = PydField(default=None)


class ChatUnreadCountRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: ChatUnreadCount | Error | None = PydField(default=None)


class ChatUnreadCountsFilter(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    ids: list[str] | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    chat_type: ChatTypeEnum | None = PydField(default=None)
    participant_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    participant_entity_id: int | None = PydField(default=None)
    search: str | None = PydField(default=None)
    closed: bool | None = PydField(default=None)
    archived: bool | None = PydField(default=None)
    pinned: bool | None = PydField(default=None)
    entity_type: ChatLinkedEntityTypeEnum | None = PydField(default=None)
    entity_bound: bool | None = PydField(default=None)


class ChatUnreadCountsGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    participant_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    participant_entity_id: int | None = PydField(default=None)
    filters: list[ChatUnreadCountsFilter] | None = PydField(default=None)


class ChatUserPresence(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    online: bool | None = PydField(default=None)
    last_online_date: int | None = PydField(default=None)


class ChatUserPresenceGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_ids: list[int] | None = PydField(default=None)


class ChatUserPresenceRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatUserPresence] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, Insert_uuid_Result, UpdateResult


ChatAddBotRequest: TypeAlias = ChatAddBot
ChatAddBotResponse: TypeAlias = UpdateResult
ChatAddParticipantRequest: TypeAlias = ChatAddParticipant
ChatAddParticipantResponse: TypeAlias = UpdateResult
ChatAddRequest: TypeAlias = ChatAdd
ChatAddResponse: TypeAlias = Insert_uuid_Result
ChatEditRequest: TypeAlias = ChatEdit
ChatEditResponse: TypeAlias = UpdateResult
ChatGetAvailableReactionsRequest: TypeAlias = ChatGetAvailableReactions
ChatGetAvailableReactionsResponse: TypeAlias = ChatAvailableReactionRegosArrayResult
ChatGetRequest: TypeAlias = ChatGet
ChatGetResponse: TypeAlias = ChatRegosOffsettedArrayResult
ChatGetUnreadCountResponse: TypeAlias = ChatUnreadCountRegosObjectResult
ChatGetUnreadCountsRequest: TypeAlias = ChatUnreadCountsGet
ChatGetUnreadCountsResponse: TypeAlias = ChatUnreadCountByKeyRegosArrayResult
ChatGetUserPresenceRequest: TypeAlias = ChatUserPresenceGet
ChatGetUserPresenceResponse: TypeAlias = ChatUserPresenceRegosArrayResult
ChatJoinRequest: TypeAlias = ChatJoin
ChatJoinResponse: TypeAlias = UpdateResult
ChatLeaveRequest: TypeAlias = ChatLeave
ChatLeaveResponse: TypeAlias = UpdateResult
ChatRemoveParticipantsRequest: TypeAlias = ChatRemoveParticipants
ChatRemoveParticipantsResponse: TypeAlias = UpdateResult
ChatSetArchivedRequest: TypeAlias = ChatSetArchived
ChatSetArchivedResponse: TypeAlias = UpdateResult
ChatSetAvailableReactionsRequest: TypeAlias = ChatSetAvailableReactions
ChatSetAvailableReactionsResponse: TypeAlias = UpdateResult
ChatSetMutedRequest: TypeAlias = ChatSetMuted
ChatSetMutedResponse: TypeAlias = UpdateResult
ChatSetParticipantsRequest: TypeAlias = ChatSetParticipants
ChatSetParticipantsResponse: TypeAlias = UpdateResult
ChatSetPinnedRequest: TypeAlias = ChatSetPinned
ChatSetPinnedResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Chat', 'ChatAdd', 'ChatAddBot', 'ChatAddParticipant', 'ChatAvailableReaction', 'ChatAvailableReactionRegosArrayResult', 'ChatEdit', 'ChatGet', 'ChatGetAvailableReactions', 'ChatJoin', 'ChatLeave', 'ChatOrder', 'ChatParticipant', 'ChatParticipantAddEdit', 'ChatParticipantRemove', 'ChatRegosOffsettedArrayResult', 'ChatRemoveParticipants', 'ChatSetArchived', 'ChatSetAvailableReactions', 'ChatSetMuted', 'ChatSetParticipants', 'ChatSetPinned', 'ChatUnreadCount', 'ChatUnreadCountByKey', 'ChatUnreadCountByKeyRegosArrayResult', 'ChatUnreadCountRegosObjectResult', 'ChatUnreadCountsFilter', 'ChatUnreadCountsGet', 'ChatUserPresence', 'ChatUserPresenceGet', 'ChatUserPresenceRegosArrayResult']


__all__ = [
    'Chat',
    'ChatAdd',
    'ChatAddBot',
    'ChatAddParticipant',
    'ChatAvailableReaction',
    'ChatAvailableReactionRegosArrayResult',
    'ChatEdit',
    'ChatEntityTypeEnum',
    'ChatGet',
    'ChatGetAvailableReactions',
    'ChatJoin',
    'ChatLeave',
    'ChatLinkedEntityTypeEnum',
    'ChatOrder',
    'ChatOrderColumn',
    'ChatParticipant',
    'ChatParticipantAddEdit',
    'ChatParticipantRemove',
    'ChatParticipantRoleEnum',
    'ChatRegosOffsettedArrayResult',
    'ChatRemoveParticipants',
    'ChatSetArchived',
    'ChatSetAvailableReactions',
    'ChatSetMuted',
    'ChatSetParticipants',
    'ChatSetPinned',
    'ChatTypeEnum',
    'ChatUnreadCount',
    'ChatUnreadCountByKey',
    'ChatUnreadCountByKeyRegosArrayResult',
    'ChatUnreadCountRegosObjectResult',
    'ChatUnreadCountsFilter',
    'ChatUnreadCountsGet',
    'ChatUserPresence',
    'ChatUserPresenceGet',
    'ChatUserPresenceRegosArrayResult',
    'ChatGetRequest',
    'ChatGetResponse',
    'ChatAddRequest',
    'ChatAddResponse',
    'ChatEditRequest',
    'ChatEditResponse',
    'ChatSetParticipantsRequest',
    'ChatSetParticipantsResponse',
    'ChatRemoveParticipantsRequest',
    'ChatRemoveParticipantsResponse',
    'ChatLeaveRequest',
    'ChatLeaveResponse',
    'ChatJoinRequest',
    'ChatJoinResponse',
    'ChatAddParticipantRequest',
    'ChatAddParticipantResponse',
    'ChatAddBotRequest',
    'ChatAddBotResponse',
    'ChatGetUnreadCountResponse',
    'ChatGetUnreadCountsRequest',
    'ChatGetUnreadCountsResponse',
    'ChatGetUserPresenceRequest',
    'ChatGetUserPresenceResponse',
    'ChatSetMutedRequest',
    'ChatSetMutedResponse',
    'ChatSetArchivedRequest',
    'ChatSetArchivedResponse',
    'ChatSetPinnedRequest',
    'ChatSetPinnedResponse',
    'ChatGetAvailableReactionsRequest',
    'ChatGetAvailableReactionsResponse',
    'ChatSetAvailableReactionsRequest',
    'ChatSetAvailableReactionsResponse'
]

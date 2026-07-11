"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ChatMessage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    reply_id: str | None = PydField(default=None)
    replay_text: str | None = PydField(default=None)
    id: str | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    author_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    author_entity_id: int | None = PydField(default=None)
    author_role: ChatParticipantRoleEnum | None = PydField(default=None)
    author_entity_name: str | None = PydField(default=None)
    author_entity_photo: str | None = PydField(default=None)
    message_type: ChatMessageTypeEnum | None = PydField(default=None)
    text: str | None = PydField(default=None)
    mentions: list[CommonMention] | None = PydField(default=None)
    file_ids: list[int] | None = PydField(default=None)
    action_code: str | None = PydField(default=None)
    action_payload: str | None = PydField(default=None)
    actions: list[list[ChatMessageAction]] | None = PydField(default=None)
    event_id: str | None = PydField(default=None)
    external_message_id: str | None = PydField(default=None)
    edited: bool | None = PydField(default=None)
    read: bool | None = PydField(default=None)
    pinned: bool | None = PydField(default=None)
    reactions: list[ChatMessageReaction] | None = PydField(default=None)
    recipient_count: int | None = PydField(default=None)
    read_count: int | None = PydField(default=None)
    created_date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ChatMessageAction(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    text: str | None = PydField(default=None)
    payload: Any = PydField(default=None)


class ChatMessageAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    reply_id: str | None = PydField(default=None)
    replay_text: str | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    author_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    author_entity_id: int | None = PydField(default=None)
    message_type: ChatMessageTypeEnum | None = PydField(default=None)
    text: str | None = PydField(default=None)
    mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    file_ids: list[int] | None = PydField(default=None)
    actions: list[list[ChatMessageAction]] | None = PydField(default=None)
    external_message_id: str | None = PydField(default=None)


class ChatMessageAddFileResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    file_id: int | None = PydField(default=None)


class ChatMessageAddFileResultRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: ChatMessageAddFileResult | Error | None = PydField(default=None)


class ChatMessageCallback(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    message_id: str | None = PydField(default=None)
    action_id: str | None = PydField(default=None)


class ChatMessageDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)


class ChatMessageEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    text: str | None = PydField(default=None)
    mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    file_ids: list[int] | None = PydField(default=None)


class ChatMessageFile(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    message_id: str | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    author_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    author_entity_id: int | None = PydField(default=None)
    author_role: ChatParticipantRoleEnum | None = PydField(default=None)
    author_entity_name: str | None = PydField(default=None)
    author_entity_photo: str | None = PydField(default=None)
    message_type: ChatMessageTypeEnum | None = PydField(default=None)
    message_created_date: int | None = PydField(default=None)
    file_order: int | None = PydField(default=None)
    file: CommonFile | None = PydField(default=None)


class ChatMessageFileKind(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class ChatMessageFileRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatMessageFile] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ChatMessageGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    ids: list[str] | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    to_date: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    include_staff_private: bool | None = PydField(default=None)


class ChatMessageGetAround(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    id: str | None = PydField(default=None)
    limit_before: int | None = PydField(default=None)
    limit_after: int | None = PydField(default=None)
    include_staff_private: bool | None = PydField(default=None)


class ChatMessageGetFiles(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    author_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    author_entity_id: int | None = PydField(default=None)
    kind: ChatMessageFileKind | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    to_date: int | None = PydField(default=None)
    include_staff_private: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ChatMessageGetPinned(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    include_staff_private: bool | None = PydField(default=None)


class ChatMessageGetReactions(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    reaction: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ChatMessageGetReadUsers(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ChatMessageMarkRead(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    last_read_message_id: str | None = PydField(default=None)


class ChatMessageMarkSent(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    external_message_id: str | None = PydField(default=None)


class ChatMessageReaction(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    reaction: str | None = PydField(default=None)
    count: int | None = PydField(default=None)
    selected: bool | None = PydField(default=None)


class ChatMessageReactionUser(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    user_name: str | None = PydField(default=None)
    user_photo_url: str | None = PydField(default=None)
    reaction: str | None = PydField(default=None)
    created_date: int | None = PydField(default=None)


class ChatMessageReactionUserRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatMessageReactionUser] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ChatMessageReadUser(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    user_name: str | None = PydField(default=None)
    user_photo_url: str | None = PydField(default=None)
    read_date: int | None = PydField(default=None)


class ChatMessageReadUserRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatMessageReadUser] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ChatMessageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatMessage] | Error | None = PydField(default=None)


class ChatMessageRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ChatMessage] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ChatMessageSearch(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    query: str | None = PydField(default=None)
    from_date: int | None = PydField(default=None)
    to_date: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    include_staff_private: bool | None = PydField(default=None)


class ChatMessageSetPinned(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    pinned: bool | None = PydField(default=None)


class ChatMessageSetReaction(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    reaction: str | None = PydField(default=None)


class ChatMessageSuggest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    author_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    author_entity_id: int | None = PydField(default=None)
    suggestions: list[str] | None = PydField(default=None)
    source_message_id: str | None = PydField(default=None)


class ChatMessageTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ChatMessageWriting(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    author_entity_type: ChatEntityTypeEnum | None = PydField(default=None)
    author_entity_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.chat.chat import ChatEntityTypeEnum, ChatParticipantRoleEnum
from schemas.api.common.base import CommonFile, CommonMention, CommonMentionInput, CommonMentionOptions, Error, Insert_uuid_Result, UpdateResult




class ChatMessageAddFileRequest(RegosModel):
    """Compatibility request for ChatMessage/AddFile JSON payloads."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    chat_id: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    extension: str | None = PydField(default=None)
    data: str | None = PydField(default=None)


ChatMessageAddFileResponse: TypeAlias = ChatMessageAddFileResultRegosObjectResult
ChatMessageAddRequest: TypeAlias = ChatMessageAdd
ChatMessageAddResponse: TypeAlias = Insert_uuid_Result
ChatMessageCallbackRequest: TypeAlias = ChatMessageCallback
ChatMessageCallbackResponse: TypeAlias = UpdateResult
ChatMessageDeleteRequest: TypeAlias = ChatMessageDelete
ChatMessageDeleteResponse: TypeAlias = UpdateResult
ChatMessageEditRequest: TypeAlias = ChatMessageEdit
ChatMessageEditResponse: TypeAlias = UpdateResult
ChatMessageGetAroundRequest: TypeAlias = ChatMessageGetAround
ChatMessageGetAroundResponse: TypeAlias = ChatMessageRegosArrayResult
ChatMessageGetFilesRequest: TypeAlias = ChatMessageGetFiles
ChatMessageGetFilesResponse: TypeAlias = ChatMessageFileRegosOffsettedArrayResult
ChatMessageGetPinnedRequest: TypeAlias = ChatMessageGetPinned
ChatMessageGetPinnedResponse: TypeAlias = ChatMessageRegosOffsettedArrayResult
ChatMessageGetReactionsRequest: TypeAlias = ChatMessageGetReactions
ChatMessageGetReactionsResponse: TypeAlias = ChatMessageReactionUserRegosOffsettedArrayResult
ChatMessageGetReadUsersRequest: TypeAlias = ChatMessageGetReadUsers
ChatMessageGetReadUsersResponse: TypeAlias = ChatMessageReadUserRegosOffsettedArrayResult
ChatMessageGetRequest: TypeAlias = ChatMessageGet
ChatMessageGetResponse: TypeAlias = ChatMessageRegosOffsettedArrayResult
ChatMessageMarkReadRequest: TypeAlias = ChatMessageMarkRead
ChatMessageMarkReadResponse: TypeAlias = UpdateResult
ChatMessageMarkSentRequest: TypeAlias = ChatMessageMarkSent
ChatMessageMarkSentResponse: TypeAlias = UpdateResult
ChatMessageSearchRequest: TypeAlias = ChatMessageSearch
ChatMessageSearchResponse: TypeAlias = ChatMessageRegosOffsettedArrayResult
ChatMessageSetPinnedRequest: TypeAlias = ChatMessageSetPinned
ChatMessageSetPinnedResponse: TypeAlias = UpdateResult
ChatMessageSetReactionRequest: TypeAlias = ChatMessageSetReaction
ChatMessageSetReactionResponse: TypeAlias = UpdateResult
ChatMessageSuggestRequest: TypeAlias = ChatMessageSuggest
ChatMessageSuggestResponse: TypeAlias = UpdateResult
ChatMessageWritingRequest: TypeAlias = ChatMessageWriting
ChatMessageWritingResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['ChatMessage', 'ChatMessageAction', 'ChatMessageAdd', 'ChatMessageAddFileResult', 'ChatMessageAddFileResultRegosObjectResult', 'ChatMessageCallback', 'ChatMessageDelete', 'ChatMessageEdit', 'ChatMessageFile', 'ChatMessageFileRegosOffsettedArrayResult', 'ChatMessageGet', 'ChatMessageGetAround', 'ChatMessageGetFiles', 'ChatMessageGetPinned', 'ChatMessageGetReactions', 'ChatMessageGetReadUsers', 'ChatMessageMarkRead', 'ChatMessageMarkSent', 'ChatMessageReaction', 'ChatMessageReactionUser', 'ChatMessageReactionUserRegosOffsettedArrayResult', 'ChatMessageReadUser', 'ChatMessageReadUserRegosOffsettedArrayResult', 'ChatMessageRegosArrayResult', 'ChatMessageRegosOffsettedArrayResult', 'ChatMessageSearch', 'ChatMessageSetPinned', 'ChatMessageSetReaction', 'ChatMessageSuggest', 'ChatMessageWriting', 'ChatMessageAddFileRequest']


__all__ = [
    'ChatMessage',
    'ChatMessageAction',
    'ChatMessageAdd',
    'ChatMessageAddFileResult',
    'ChatMessageAddFileResultRegosObjectResult',
    'ChatMessageCallback',
    'ChatMessageDelete',
    'ChatMessageEdit',
    'ChatMessageFile',
    'ChatMessageFileKind',
    'ChatMessageFileRegosOffsettedArrayResult',
    'ChatMessageGet',
    'ChatMessageGetAround',
    'ChatMessageGetFiles',
    'ChatMessageGetPinned',
    'ChatMessageGetReactions',
    'ChatMessageGetReadUsers',
    'ChatMessageMarkRead',
    'ChatMessageMarkSent',
    'ChatMessageReaction',
    'ChatMessageReactionUser',
    'ChatMessageReactionUserRegosOffsettedArrayResult',
    'ChatMessageReadUser',
    'ChatMessageReadUserRegosOffsettedArrayResult',
    'ChatMessageRegosArrayResult',
    'ChatMessageRegosOffsettedArrayResult',
    'ChatMessageSearch',
    'ChatMessageSetPinned',
    'ChatMessageSetReaction',
    'ChatMessageSuggest',
    'ChatMessageTypeEnum',
    'ChatMessageWriting',
    'ChatMessageAddFileRequest',
    'ChatMessageGetRequest',
    'ChatMessageGetResponse',
    'ChatMessageGetFilesRequest',
    'ChatMessageGetFilesResponse',
    'ChatMessageAddRequest',
    'ChatMessageAddResponse',
    'ChatMessageAddFileResponse',
    'ChatMessageEditRequest',
    'ChatMessageEditResponse',
    'ChatMessageDeleteRequest',
    'ChatMessageDeleteResponse',
    'ChatMessageMarkReadRequest',
    'ChatMessageMarkReadResponse',
    'ChatMessageMarkSentRequest',
    'ChatMessageMarkSentResponse',
    'ChatMessageWritingRequest',
    'ChatMessageWritingResponse',
    'ChatMessageSuggestRequest',
    'ChatMessageSuggestResponse',
    'ChatMessageSearchRequest',
    'ChatMessageSearchResponse',
    'ChatMessageSetPinnedRequest',
    'ChatMessageSetPinnedResponse',
    'ChatMessageGetPinnedRequest',
    'ChatMessageGetPinnedResponse',
    'ChatMessageGetAroundRequest',
    'ChatMessageGetAroundResponse',
    'ChatMessageSetReactionRequest',
    'ChatMessageSetReactionResponse',
    'ChatMessageCallbackRequest',
    'ChatMessageCallbackResponse',
    'ChatMessageGetReactionsRequest',
    'ChatMessageGetReactionsResponse',
    'ChatMessageGetReadUsersRequest',
    'ChatMessageGetReadUsersResponse'
]

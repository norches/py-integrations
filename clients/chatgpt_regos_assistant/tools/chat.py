from __future__ import annotations

from typing import Dict

from ..models import RegosTool
from .common import LIMIT, OFFSET, UUIDS, UUID_FILTER_SCHEMA, object_schema


CHAT_TOOLS: Dict[str, RegosTool] = {
    "chat_get": RegosTool(
        name="chat_get",
        description="Find REGOS chats by id, entity filters, limit and offset.",
        service_path=("chat", "chat", "get"),
        regos_method="Chat/Get",
        mutating=False,
        input_schema=UUID_FILTER_SCHEMA,
    ),
    "chat_message_get": RegosTool(
        name="chat_message_get",
        description="Read REGOS chat messages by chat id or message id.",
        service_path=("chat", "chat_message", "get"),
        regos_method="ChatMessage/Get",
        mutating=False,
        input_schema=object_schema(
            {
                "ids": UUIDS,
                "chat_ids": UUIDS,
                "limit": LIMIT,
                "offset": OFFSET,
            }
        ),
    ),
    "chat_message_add": RegosTool(
        name="chat_message_add",
        description="Send a REGOS chat message. Requires explicit user confirmation.",
        service_path=("chat", "chat_message", "add"),
        regos_method="ChatMessage/Add",
        mutating=True,
        input_schema=object_schema(
            {
                "chat_id": {"type": "string"},
                "text": {"type": "string"},
                "type": {"type": "string"},
                "external_message_id": {"type": "string"},
            },
            required=("chat_id", "text"),
        ),
    ),
}

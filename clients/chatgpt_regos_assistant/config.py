from __future__ import annotations

from config.settings import settings as app_settings


class ChatGptRegosAssistantConfig:
    INTEGRATION_KEY = "chatgpt_regos_assistant"
    OPENAI_RESPONSES_ENDPOINT = "https://api.openai.com/v1/responses"
    SETTINGS_TTL_SEC = max(int(app_settings.redis_cache_ttl or 60), 60)
    DEFAULT_OPENAI_MODEL = "gpt-4.1-mini"
    DEFAULT_TEMPERATURE = 0.2
    DEFAULT_MAX_TOOL_ROUNDS = 5
    DEFAULT_MAX_OUTPUT_TOKENS = 1200
    MAX_OPENAI_TOOLS = 120
    DEFAULT_CONFIRMATION_TTL_SEC = 15 * 60
    CHATGPT_CONNECT_URL = app_settings.chatgpt_regos_connect_url.strip()
    EMBED_SDK_URL = "https://auth.regos.uz/widget/regos-embed-sdk.v1.1.min.js"
    EMBED_TOKEN_GRANT_TYPE = "embed_token"
    EMBED_SESSION_DEFAULT_TTL_SEC = 10 * 60
    EMBED_SESSION_MAX_TTL_SEC = 60 * 60
    EMBED_PARENT_ORIGIN = "https://regos.online"
    DEFAULT_PROMPT = (
        "You are a REGOS assistant inside ChatGPT. Help the user work with CRM, chats, "
        "items and stocks through the provided REGOS tools. Read-only requests may be "
        "executed directly. For every create, update, stage/status change, close or "
        "delete operation, explain the exact action and wait for explicit confirmation. "
        "Never invent REGOS ids; search first when an id is missing."
    )

from __future__ import annotations

import html
import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

from core.logger import setup_logger


logger = setup_logger("chatgpt_regos_assistant.ui")

_BASE_DIR = Path(__file__).resolve().parent
_TEMPLATE_PATH = _BASE_DIR / "ui_template.html"
_CSS_PATH = _BASE_DIR / "ui_template.css"


@dataclass(frozen=True)
class ChatGptRegosAssistantUiContext:
    connected_integration_id: str
    api_url: str
    external_url: str
    embed_backend_url: str
    embed_sdk_url: str
    oauth_client_id: str
    embed_parent_origin: str
    model: str
    tools_count: int
    confirmation_ttl_sec: int
    openai_api_chat_enabled: bool
    mode: str
    error: str = ""


@lru_cache(maxsize=1)
def _load_template() -> str:
    try:
        return _TEMPLATE_PATH.read_text(encoding="utf-8")
    except Exception as error:
        logger.exception("Failed to load ChatGPT REGOS UI template: %s", error)
        return "<!doctype html><html><body>{content_html}</body></html>"


@lru_cache(maxsize=1)
def _load_css() -> str:
    try:
        return _CSS_PATH.read_text(encoding="utf-8")
    except Exception as error:
        logger.exception("Failed to load ChatGPT REGOS UI CSS: %s", error)
        return "body{margin:0;font-family:Arial,sans-serif;background:#f4f6f8;color:#172033}"


def _escape(value: Any, *, quote: bool = False) -> str:
    return html.escape(str(value or ""), quote=quote)


def _json_script(value: Dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")


def _chat_disabled(ctx: ChatGptRegosAssistantUiContext) -> str:
    return "" if ctx.openai_api_chat_enabled and ctx.connected_integration_id else "disabled"


def _initial_message(ctx: ChatGptRegosAssistantUiContext) -> str:
    if not ctx.connected_integration_id:
        return "Откройте помощника внутри REGOS, чтобы начать работу."
    if not ctx.openai_api_chat_enabled:
        return "Чат ещё не включён. Попросите администратора подключить помощника."
    return (
        "Здравствуйте! Напишите, что нужно сделать. Например: найти товар, "
        "проверить остатки, показать продажи или создать задачу."
    )


def render_chatgpt_regos_assistant_ui(ctx: ChatGptRegosAssistantUiContext) -> str:
    embed_auth_enabled = bool(
        ctx.connected_integration_id
        and ctx.embed_backend_url
        and ctx.oauth_client_id
    )
    config = {
        "apiUrl": ctx.external_url.rstrip("/") if ctx.external_url else ctx.api_url,
        "connectedIntegrationId": ctx.connected_integration_id,
        "chatEnabled": bool(ctx.openai_api_chat_enabled and ctx.connected_integration_id),
        "externalUrl": ctx.external_url,
        "embedAuthEnabled": embed_auth_enabled,
        "embedBackendUrl": ctx.embed_backend_url,
        "oauthClientId": ctx.oauth_client_id,
        "embedParentOrigin": ctx.embed_parent_origin,
    }
    style_block = f"<style>{_load_css()}</style>"
    template = _load_template()
    return template.format(
        style_block=style_block,
        safe_title=_escape("REGOS помощник", quote=True),
        safe_mode=_escape(ctx.mode, quote=True),
        safe_embed_sdk_url=_escape(ctx.embed_sdk_url, quote=True),
        safe_error=_escape(ctx.error),
        chat_disabled=_chat_disabled(ctx),
        safe_initial_message=_escape(_initial_message(ctx)),
        app_config_json=_json_script(config),
    )

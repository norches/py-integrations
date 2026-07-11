from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

import httpx

from .config import ChatGptRegosAssistantConfig
from .models import OpenAIToolCall, RuntimeConfig


def build_openai_input(
    *, message: Optional[str], messages: Optional[List[Any]], kwargs: Dict[str, Any]
) -> Any:
    if messages:
        return messages
    text = str(message or kwargs.get("text") or kwargs.get("prompt") or "").strip()
    if not text:
        text = "Help me work with REGOS."
    return [{"role": "user", "content": text}]


async def post_openai_response(
    client: httpx.AsyncClient, runtime: RuntimeConfig, payload: Dict[str, Any]
) -> Dict[str, Any]:
    response = await client.post(
        ChatGptRegosAssistantConfig.OPENAI_RESPONSES_ENDPOINT,
        headers={
            "Authorization": f"Bearer {runtime.openai_api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
    )
    response.raise_for_status()
    data = response.json()
    return data if isinstance(data, dict) else {}


def extract_openai_tool_calls(response: Dict[str, Any]) -> List[OpenAIToolCall]:
    calls: List[OpenAIToolCall] = []
    for item in response.get("output") or []:
        if not isinstance(item, dict) or item.get("type") != "function_call":
            continue
        name = str(item.get("name") or "").strip()
        call_id = str(item.get("call_id") or item.get("id") or "").strip()
        if not name or not call_id:
            continue
        raw_arguments = item.get("arguments") or {}
        if isinstance(raw_arguments, str):
            try:
                parsed = json.loads(raw_arguments)
            except json.JSONDecodeError:
                parsed = {"value": raw_arguments}
        else:
            parsed = raw_arguments
        calls.append(
            OpenAIToolCall(
                call_id=call_id,
                name=name,
                arguments=parsed if isinstance(parsed, dict) else {"value": parsed},
            )
        )
    return calls


def extract_openai_text(response: Dict[str, Any]) -> str:
    direct = response.get("output_text")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()

    parts: List[str] = []
    for item in response.get("output") or []:
        if not isinstance(item, dict):
            continue
        for content in item.get("content") or []:
            if not isinstance(content, dict):
                continue
            text = content.get("text")
            if isinstance(text, str) and text.strip():
                parts.append(text.strip())
    return "\n".join(parts).strip()

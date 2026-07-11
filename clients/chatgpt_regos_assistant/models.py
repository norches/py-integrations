from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

from pydantic import BaseModel


@dataclass(frozen=True)
class RuntimeConfig:
    openai_api_key: str
    openai_model: str
    assistant_prompt: str
    temperature: float
    max_tool_rounds: int
    max_output_tokens: int
    confirmation_ttl_sec: int


@dataclass(frozen=True)
class RegosTool:
    name: str
    description: str
    service_path: Tuple[str, ...]
    regos_method: str
    mutating: bool
    input_schema: Dict[str, Any]
    payload_key: Optional[str] = None

    def as_openai_tool(self) -> Dict[str, Any]:
        return {
            "type": "function",
            "name": self.name,
            "description": self.description,
            "parameters": self.input_schema,
        }


@dataclass(frozen=True)
class OpenAIToolCall:
    call_id: str
    name: str
    arguments: Dict[str, Any]


def parse_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "y", "on"}:
        return True
    if text in {"0", "false", "no", "n", "off"}:
        return False
    return default


def parse_int(value: Any, default: int, *, minimum: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        parsed = default
    return max(minimum, min(maximum, parsed))


def parse_float(value: Any, default: float, *, minimum: float, maximum: float) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        parsed = default
    return max(minimum, min(maximum, parsed))


def jsonable(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return value.model_dump(mode="json", exclude_none=True, by_alias=True)
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def json_dumps(value: Any, *, indent: int | None = None) -> str:
    if indent is None:
        return json.dumps(jsonable(value), ensure_ascii=False, separators=(",", ":"))
    return json.dumps(jsonable(value), ensure_ascii=False, indent=indent)

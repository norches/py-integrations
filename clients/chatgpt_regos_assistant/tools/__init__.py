from __future__ import annotations

from dataclasses import replace
from typing import Dict

from ..models import RegosTool
from .chat import CHAT_TOOLS
from .common import generated_tool_input_schema
from .crm import CRM_TOOLS
from .references import REFERENCES_TOOLS
from .store import STORE_TOOLS


def _with_generated_schema(tool: RegosTool) -> RegosTool:
    generated_schema = generated_tool_input_schema(tool)
    if generated_schema is None:
        return tool
    return replace(tool, input_schema=generated_schema)


_REGOS_TOOLS: Dict[str, RegosTool] = {
    **CRM_TOOLS,
    **REFERENCES_TOOLS,
    **STORE_TOOLS,
    **CHAT_TOOLS,
}
REGOS_TOOLS: Dict[str, RegosTool] = {
    name: _with_generated_schema(tool) for name, tool in _REGOS_TOOLS.items()
}

__all__ = [
    "CHAT_TOOLS",
    "CRM_TOOLS",
    "REFERENCES_TOOLS",
    "STORE_TOOLS",
    "REGOS_TOOLS",
]

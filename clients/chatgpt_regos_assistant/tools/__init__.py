from __future__ import annotations

from typing import Dict

from ..models import RegosTool
from .chat import CHAT_TOOLS
from .crm import CRM_TOOLS
from .references import REFERENCES_TOOLS
from .store import STORE_TOOLS


REGOS_TOOLS: Dict[str, RegosTool] = {
    **CRM_TOOLS,
    **REFERENCES_TOOLS,
    **STORE_TOOLS,
    **CHAT_TOOLS,
}

__all__ = [
    "CHAT_TOOLS",
    "CRM_TOOLS",
    "REFERENCES_TOOLS",
    "STORE_TOOLS",
    "REGOS_TOOLS",
]

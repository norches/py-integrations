from __future__ import annotations

from typing import Any, Dict, Tuple


def object_schema(
    properties: Dict[str, Any],
    *,
    required: Tuple[str, ...] = (),
    additional_properties: bool = True,
) -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": list(required),
        "additionalProperties": additional_properties,
    }


IDS = {"type": "array", "items": {"type": "integer"}, "description": "REGOS ids."}
ID = {"type": "integer", "description": "REGOS id."}
UUIDS = {"type": "array", "items": {"type": "string"}, "description": "REGOS uuid ids."}
LIMIT = {"type": "integer", "minimum": 1, "maximum": 100, "default": 20}
OFFSET = {"type": "integer", "minimum": 0, "default": 0}
SEARCH = {"type": "string", "description": "Text search value when the REGOS method supports it."}
DATE_TIME = {"type": "string", "description": "Date/time value accepted by REGOS."}
AMOUNT = {"type": "number", "description": "Money amount."}
QUANTITY = {"type": "number", "description": "Item quantity."}
BOOLEAN = {"type": "boolean"}
OBJECT_ARRAY = {"type": "array", "items": {"type": "object", "additionalProperties": True}}

FILTER_SCHEMA = object_schema(
    {
        "ids": IDS,
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

UUID_FILTER_SCHEMA = object_schema(
    {
        "ids": UUIDS,
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

DOC_FILTER_SCHEMA = object_schema(
    {
        "ids": IDS,
        "firm_ids": IDS,
        "stock_ids": IDS,
        "client_ids": IDS,
        "partner_ids": IDS,
        "status_ids": IDS,
        "date_from": DATE_TIME,
        "date_to": DATE_TIME,
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

DOC_ACTION_SCHEMA = object_schema({"id": ID}, required=("id",))
DOC_LOCK_SCHEMA = object_schema({"ids": IDS}, required=("ids",))

OPERATIONS_SCHEMA = object_schema(
    {
        "operations": OBJECT_ARRAY,
    },
    required=("operations",),
    additional_properties=False,
)

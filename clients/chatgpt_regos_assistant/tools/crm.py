from __future__ import annotations

from typing import Dict

from ..models import RegosTool
from .common import IDS, LIMIT, OFFSET, SEARCH, object_schema


CRM_TOOLS: Dict[str, RegosTool] = {
    "client_get": RegosTool(
        name="client_get",
        description="Find CRM clients in REGOS by id, phone, external id, text filters, limit and offset.",
        service_path=("crm", "client", "get"),
        regos_method="Client/Get",
        mutating=False,
        input_schema=object_schema(
            {
                "ids": IDS,
                "phones": {"type": "array", "items": {"type": "string"}},
                "external_ids": {"type": "array", "items": {"type": "string"}},
                "search": SEARCH,
                "limit": LIMIT,
                "offset": OFFSET,
            }
        ),
    ),
    "client_add": RegosTool(
        name="client_add",
        description="Create a CRM client in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "client", "add"),
        regos_method="Client/Add",
        mutating=True,
        input_schema=object_schema(
            {
                "name": {"type": "string"},
                "phone": {"type": "string"},
                "email": {"type": "string"},
                "external_id": {"type": "string"},
                "responsible_user_id": {"type": "integer"},
            }
        ),
    ),
    "client_edit": RegosTool(
        name="client_edit",
        description="Update a CRM client in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "client", "edit"),
        regos_method="Client/Edit",
        mutating=True,
        input_schema=object_schema(
            {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "phone": {"type": "string"},
                "email": {"type": "string"},
                "external_id": {"type": "string"},
                "responsible_user_id": {"type": "integer"},
            },
            required=("id",),
        ),
    ),
    "client_delete": RegosTool(
        name="client_delete",
        description="Delete CRM clients in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "client", "delete"),
        regos_method="Client/Delete",
        mutating=True,
        input_schema=object_schema({"ids": IDS}, required=("ids",)),
    ),
    "deal_get": RegosTool(
        name="deal_get",
        description="Find CRM deals in REGOS by id, client, pipeline, stage, text filters, limit and offset.",
        service_path=("crm", "deal", "get"),
        regos_method="Deal/Get",
        mutating=False,
        input_schema=object_schema(
            {
                "ids": IDS,
                "client_ids": IDS,
                "pipeline_ids": IDS,
                "stage_ids": IDS,
                "search": SEARCH,
                "limit": LIMIT,
                "offset": OFFSET,
            }
        ),
    ),
    "deal_add": RegosTool(
        name="deal_add",
        description="Create a CRM deal in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "deal", "add"),
        regos_method="Deal/Add",
        mutating=True,
        input_schema=object_schema(
            {
                "name": {"type": "string"},
                "client_id": {"type": "integer"},
                "pipeline_id": {"type": "integer"},
                "stage_id": {"type": "integer"},
                "amount": {"type": "number"},
                "responsible_user_id": {"type": "integer"},
            }
        ),
    ),
    "deal_edit": RegosTool(
        name="deal_edit",
        description="Update a CRM deal in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "deal", "edit"),
        regos_method="Deal/Edit",
        mutating=True,
        input_schema=object_schema(
            {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "client_id": {"type": "integer"},
                "pipeline_id": {"type": "integer"},
                "stage_id": {"type": "integer"},
                "amount": {"type": "number"},
                "responsible_user_id": {"type": "integer"},
            },
            required=("id",),
        ),
    ),
    "deal_set_stage": RegosTool(
        name="deal_set_stage",
        description="Move a CRM deal to another stage in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "deal", "set_stage"),
        regos_method="Deal/SetStage",
        mutating=True,
        input_schema=object_schema(
            {"id": {"type": "integer"}, "stage_id": {"type": "integer"}},
            required=("id", "stage_id"),
        ),
    ),
    "deal_close": RegosTool(
        name="deal_close",
        description="Close a CRM deal in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "deal", "close"),
        regos_method="Deal/Close",
        mutating=True,
        input_schema=object_schema(
            {
                "id": {"type": "integer"},
                "success": {"type": "boolean"},
                "comment": {"type": "string"},
            },
            required=("id",),
        ),
    ),
    "deal_delete": RegosTool(
        name="deal_delete",
        description="Delete CRM deals in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "deal", "delete"),
        regos_method="Deal/Delete",
        mutating=True,
        input_schema=object_schema({"ids": IDS}, required=("ids",)),
    ),
    "ticket_get": RegosTool(
        name="ticket_get",
        description="Find CRM tickets in REGOS by id, client, status, text filters, limit and offset.",
        service_path=("crm", "ticket", "get"),
        regos_method="Ticket/Get",
        mutating=False,
        input_schema=object_schema(
            {
                "ids": IDS,
                "client_ids": IDS,
                "status_ids": IDS,
                "search": SEARCH,
                "limit": LIMIT,
                "offset": OFFSET,
            }
        ),
    ),
    "ticket_add": RegosTool(
        name="ticket_add",
        description="Create a CRM ticket in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "ticket", "add"),
        regos_method="Ticket/Add",
        mutating=True,
        input_schema=object_schema(
            {
                "name": {"type": "string"},
                "client_id": {"type": "integer"},
                "status_id": {"type": "integer"},
                "responsible_user_id": {"type": "integer"},
            }
        ),
    ),
    "ticket_edit": RegosTool(
        name="ticket_edit",
        description="Update a CRM ticket in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "ticket", "edit"),
        regos_method="Ticket/Edit",
        mutating=True,
        input_schema=object_schema(
            {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "client_id": {"type": "integer"},
                "status_id": {"type": "integer"},
                "responsible_user_id": {"type": "integer"},
            },
            required=("id",),
        ),
    ),
    "ticket_set_status": RegosTool(
        name="ticket_set_status",
        description="Change a CRM ticket status in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "ticket", "set_status"),
        regos_method="Ticket/SetStatus",
        mutating=True,
        input_schema=object_schema(
            {"id": {"type": "integer"}, "status_id": {"type": "integer"}},
            required=("id", "status_id"),
        ),
    ),
    "ticket_close": RegosTool(
        name="ticket_close",
        description="Close a CRM ticket in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "ticket", "close"),
        regos_method="Ticket/Close",
        mutating=True,
        input_schema=object_schema(
            {"id": {"type": "integer"}, "comment": {"type": "string"}},
            required=("id",),
        ),
    ),
    "ticket_delete": RegosTool(
        name="ticket_delete",
        description="Delete CRM tickets in REGOS. Requires explicit user confirmation.",
        service_path=("crm", "ticket", "delete"),
        regos_method="Ticket/Delete",
        mutating=True,
        input_schema=object_schema({"ids": IDS}, required=("ids",)),
    ),
}

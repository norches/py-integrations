from __future__ import annotations

import importlib
import inspect
from copy import deepcopy
from decimal import Decimal
from enum import Enum
from types import UnionType
from typing import (
    Any,
    Dict,
    Literal,
    Tuple,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from pydantic import BaseModel

from core.api.service import RegosAPIService


COMMON_FIELD_DESCRIPTIONS = {
    "address": "Warehouse or customer address.",
    "amount": "Deal or document amount.",
    "article": "Item article/vendor code.",
    "barcode": "Single item barcode value.",
    "barcodes": "Item barcode values used for filtering or mutation.",
    "chat_id": "REGOS chat uuid.",
    "client_id": "REGOS CRM client id.",
    "code": "REGOS item or document code.",
    "comment": "Free-form comment for the action or document.",
    "confirm_code": "Confirmation code returned or requested by REGOS.",
    "description": "Free-form item description.",
    "email": "Client email address.",
    "external_id": "External system id linked to the REGOS record.",
    "external_ids": "External system ids linked to REGOS records.",
    "external_message_id": "External chat message id for idempotency or linking.",
    "full_name": "Full item name.",
    "id": "REGOS record id.",
    "is_active": "Whether the item is active.",
    "is_base": "Whether the barcode is the base barcode for the item.",
    "is_service": "Whether the item is a service instead of a stock item.",
    "limit": "Maximum number of records to return.",
    "name": "Human-readable record name.",
    "number": "Document number.",
    "offset": "Zero-based pagination offset.",
    "operations": "Document row/operation payloads accepted by the target REGOS method.",
    "phone": "Client phone number.",
    "phones": "Client phone numbers used for lookup.",
    "pipeline_id": "REGOS CRM pipeline id.",
    "position": "Target row position inside the document.",
    "prefix": "Code prefix used by REGOS code generation.",
    "responsible_user_id": "REGOS user id responsible for the record.",
    "stage_id": "REGOS CRM deal stage id.",
    "status_id": "REGOS status id.",
    "success": "Whether the deal was closed successfully.",
    "text": "Message text.",
    "type": "REGOS enum value or message type.",
}


def _with_common_description(name: str, schema: Any) -> Any:
    if not isinstance(schema, dict):
        return schema

    enriched = deepcopy(schema)
    description = (
        COMMON_FIELD_DESCRIPTIONS.get(name)
        or f"REGOS field: {name.replace('_', ' ')}."
    )
    if description and not enriched.get("description"):
        enriched["description"] = description
    return enriched


def object_schema(
    properties: Dict[str, Any],
    *,
    required: Tuple[str, ...] = (),
    additional_properties: bool = True,
) -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            name: _with_common_description(name, schema)
            for name, schema in properties.items()
        },
        "required": list(required),
        "additionalProperties": additional_properties,
    }


def _compact_description(value: Any, *, max_len: int = 700) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def _enum_type(values: list[Any]) -> str:
    if any(isinstance(value, str) for value in values):
        return "string"
    if all(isinstance(value, int) and not isinstance(value, bool) for value in values):
        return "integer"
    if all(
        isinstance(value, (int, float)) and not isinstance(value, bool)
        for value in values
    ):
        return "number"
    return "string"


def _simple_schema_for_annotation(annotation: Any) -> Dict[str, Any]:
    none_type = type(None)
    origin = get_origin(annotation)

    if origin in (Union, UnionType):
        args = [arg for arg in get_args(annotation) if arg is not none_type]
        if len(args) == 1:
            return _simple_schema_for_annotation(args[0])
        for arg in args:
            candidate = _simple_schema_for_annotation(arg)
            if candidate.get("type") not in {"object", "array"}:
                return candidate
        return {"type": "object", "additionalProperties": True}

    if origin is Literal:
        values = list(get_args(annotation))
        return {"type": _enum_type(values), "enum": values}

    if origin in (list, set, tuple):
        args = get_args(annotation)
        item_annotation = args[0] if args else Any
        return {
            "type": "array",
            "items": _simple_schema_for_annotation(item_annotation),
        }

    if origin in (dict, Dict):
        return {"type": "object", "additionalProperties": True}

    if annotation is Any:
        return {"type": "object", "additionalProperties": True}
    if annotation is str:
        return {"type": "string"}
    if annotation is bool:
        return {"type": "boolean"}
    if annotation is int:
        return {"type": "integer"}
    if annotation in (float, Decimal):
        return {"type": "number"}

    if inspect.isclass(annotation) and issubclass(annotation, Enum):
        values = [member.value for member in annotation]
        return {"type": _enum_type(values), "enum": values}

    if inspect.isclass(annotation) and issubclass(annotation, BaseModel):
        return {"type": "object", "additionalProperties": True}

    return {"type": "object", "additionalProperties": True}


def model_input_schema(model: type[BaseModel]) -> Dict[str, Any]:
    properties: Dict[str, Any] = {}
    required: list[str] = []

    for name, field in model.model_fields.items():
        schema = _simple_schema_for_annotation(field.annotation)
        description = _compact_description(field.description)
        if description:
            schema["description"] = description
        properties[name] = schema
        if field.is_required():
            required.append(name)

    return object_schema(
        properties,
        required=tuple(required),
        additional_properties=False,
    )


def _service_class(service_path: Tuple[str, ...]) -> type[RegosAPIService] | None:
    module_name = "core.api." + ".".join(service_path[:-1])
    module = importlib.import_module(module_name)
    for value in vars(module).values():
        if (
            inspect.isclass(value)
            and issubclass(value, RegosAPIService)
            and value is not RegosAPIService
        ):
            return value
    return None


def _extract_model_from_annotation(annotation: Any) -> tuple[type[BaseModel] | None, bool]:
    origin = get_origin(annotation)
    if origin in (Union, UnionType):
        for arg in get_args(annotation):
            model, is_list = _extract_model_from_annotation(arg)
            if model is not None:
                return model, is_list
        return None, False

    if origin in (list, set, tuple):
        args = get_args(annotation)
        if not args:
            return None, True
        model, _ = _extract_model_from_annotation(args[0])
        return model, True

    if inspect.isclass(annotation) and issubclass(annotation, BaseModel):
        return annotation, False

    return None, False


def service_request_model(
    service_path: Tuple[str, ...],
) -> tuple[type[BaseModel] | None, bool]:
    service_cls = _service_class(service_path)
    if service_cls is None:
        return None, False

    method_name = service_path[-1]
    registered = service_cls.REQUEST_MODELS.get(method_name)
    if registered is not None:
        return registered, False

    method = getattr(service_cls, method_name, None)
    if method is None:
        return None, False

    try:
        hints = get_type_hints(method)
    except Exception:
        return None, False

    for parameter_name in inspect.signature(method).parameters:
        if parameter_name == "self":
            continue
        annotation = hints.get(parameter_name)
        if annotation is None:
            continue
        model, is_list = _extract_model_from_annotation(annotation)
        if model is not None:
            return model, is_list
    return None, False


def generated_tool_input_schema(tool: Any) -> Dict[str, Any] | None:
    model, is_list = service_request_model(tuple(tool.service_path))
    if model is None:
        return None

    if is_list:
        payload_key = str(tool.payload_key or "items")
        return object_schema(
            {
                payload_key: {
                    "type": "array",
                    "items": model_input_schema(model),
                    "description": f"Rows accepted by {tool.regos_method}.",
                }
            },
            required=(payload_key,),
            additional_properties=False,
        )

    return model_input_schema(model)


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

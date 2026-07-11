from __future__ import annotations

from typing import Dict, Iterable, Literal

from ..models import RegosTool
from .common import (
    AMOUNT,
    DATE_TIME,
    DOC_ACTION_SCHEMA,
    DOC_FILTER_SCHEMA,
    DOC_LOCK_SCHEMA,
    ID,
    IDS,
    LIMIT,
    OFFSET,
    OPERATIONS_SCHEMA,
    QUANTITY,
    SEARCH,
    object_schema,
)


Lifecycle = Literal["perform", "close"]

DOC_MUTATION_SCHEMA = object_schema(
    {
        "id": ID,
        "firm_id": ID,
        "stock_id": ID,
        "stock_from_id": ID,
        "stock_to_id": ID,
        "partner_id": ID,
        "client_id": ID,
        "date": DATE_TIME,
        "number": {"type": "string"},
        "comment": {"type": "string"},
        "status_id": ID,
        "responsible_user_id": ID,
    }
)

OPERATION_FILTER_SCHEMA = object_schema(
    {
        "ids": IDS,
        "doc_id": ID,
        "doc_ids": IDS,
        "item_ids": IDS,
        "stock_ids": IDS,
        "firm_ids": IDS,
        "date_from": DATE_TIME,
        "date_to": DATE_TIME,
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

SET_PRICE_SCHEMA = object_schema(
    {
        "doc_id": ID,
        "operation_ids": IDS,
        "price_type_id": ID,
        "stock_id": ID,
        "date": DATE_TIME,
    }
)

SET_COST_SCHEMA = object_schema(
    {
        "doc_id": ID,
        "operation_ids": IDS,
        "item_ids": IDS,
        "date": DATE_TIME,
    }
)

MOVE_OPERATIONS_SCHEMA = object_schema(
    {
        "doc_id": ID,
        "from_doc_id": ID,
        "to_doc_id": ID,
        "operation_ids": IDS,
        "position": {"type": "integer"},
    }
)

COPY_OPERATIONS_SCHEMA = object_schema(
    {
        "from_doc_id": ID,
        "to_doc_id": ID,
        "operation_ids": IDS,
        "quantity": QUANTITY,
    }
)

DISCOUNT_SCHEMA = object_schema(
    {
        "doc_id": ID,
        "operation_id": ID,
        "operation_ids": IDS,
        "discount": AMOUNT,
        "discount_percent": AMOUNT,
    }
)


def _doc_tools(
    *,
    prefix: str,
    title: str,
    service: str,
    method: str,
    lifecycle: Lifecycle = "perform",
) -> Dict[str, RegosTool]:
    tools: Dict[str, RegosTool] = {
        f"{prefix}_get": RegosTool(
            name=f"{prefix}_get",
            description=f"Find {title} documents in REGOS.",
            service_path=("docs", service, "get"),
            regos_method=f"{method}/Get",
            mutating=False,
            input_schema=DOC_FILTER_SCHEMA,
        ),
        f"{prefix}_add": RegosTool(
            name=f"{prefix}_add",
            description=f"Create a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "add"),
            regos_method=f"{method}/Add",
            mutating=True,
            input_schema=DOC_MUTATION_SCHEMA,
        ),
        f"{prefix}_edit": RegosTool(
            name=f"{prefix}_edit",
            description=f"Update a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "edit"),
            regos_method=f"{method}/Edit",
            mutating=True,
            input_schema=DOC_MUTATION_SCHEMA,
        ),
        f"{prefix}_delete_mark": RegosTool(
            name=f"{prefix}_delete_mark",
            description=f"Mark a {title} document as deleted in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "delete_mark"),
            regos_method=f"{method}/DeleteMark",
            mutating=True,
            input_schema=DOC_ACTION_SCHEMA,
        ),
        f"{prefix}_delete": RegosTool(
            name=f"{prefix}_delete",
            description=f"Delete a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "delete"),
            regos_method=f"{method}/Delete",
            mutating=True,
            input_schema=DOC_ACTION_SCHEMA,
        ),
        f"{prefix}_lock": RegosTool(
            name=f"{prefix}_lock",
            description=f"Lock a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "lock"),
            regos_method=f"{method}/Lock",
            mutating=True,
            input_schema=DOC_LOCK_SCHEMA,
        ),
        f"{prefix}_unlock": RegosTool(
            name=f"{prefix}_unlock",
            description=f"Unlock a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "unlock"),
            regos_method=f"{method}/Unlock",
            mutating=True,
            input_schema=DOC_LOCK_SCHEMA,
        ),
    }
    if lifecycle == "close":
        tools.update(
            {
                f"{prefix}_close": RegosTool(
                    name=f"{prefix}_close",
                    description=f"Close a {title} document in REGOS. Requires explicit user confirmation.",
                    service_path=("docs", service, "close"),
                    regos_method=f"{method}/Close",
                    mutating=True,
                    input_schema=DOC_ACTION_SCHEMA,
                ),
                f"{prefix}_open": RegosTool(
                    name=f"{prefix}_open",
                    description=f"Open a closed {title} document in REGOS. Requires explicit user confirmation.",
                    service_path=("docs", service, "open"),
                    regos_method=f"{method}/Open",
                    mutating=True,
                    input_schema=DOC_ACTION_SCHEMA,
                ),
            }
        )
    else:
        tools.update(
            {
                f"{prefix}_perform": RegosTool(
                    name=f"{prefix}_perform",
                    description=f"Perform/post a {title} document in REGOS. Requires explicit user confirmation.",
                    service_path=("docs", service, "perform"),
                    regos_method=f"{method}/Perform",
                    mutating=True,
                    input_schema=DOC_ACTION_SCHEMA,
                ),
                f"{prefix}_perform_cancel": RegosTool(
                    name=f"{prefix}_perform_cancel",
                    description=f"Cancel posting of a {title} document in REGOS. Requires explicit user confirmation.",
                    service_path=("docs", service, "perform_cancel"),
                    regos_method=f"{method}/PerformCancel",
                    mutating=True,
                    input_schema=DOC_ACTION_SCHEMA,
                ),
            }
        )
    return tools


def _operation_tools(
    *,
    prefix: str,
    title: str,
    service: str,
    method: str,
    extra_actions: Iterable[str] = (),
) -> Dict[str, RegosTool]:
    tools: Dict[str, RegosTool] = {
        f"{prefix}_get": RegosTool(
            name=f"{prefix}_get",
            description=f"Find rows/operations for {title} documents in REGOS.",
            service_path=("docs", service, "get"),
            regos_method=f"{method}/Get",
            mutating=False,
            input_schema=OPERATION_FILTER_SCHEMA,
        ),
        f"{prefix}_add": RegosTool(
            name=f"{prefix}_add",
            description=f"Add rows/operations to a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "add"),
            regos_method=f"{method}/Add",
            mutating=True,
            input_schema=OPERATIONS_SCHEMA,
            payload_key="operations",
        ),
        f"{prefix}_edit": RegosTool(
            name=f"{prefix}_edit",
            description=f"Update rows/operations in a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "edit"),
            regos_method=f"{method}/Edit",
            mutating=True,
            input_schema=OPERATIONS_SCHEMA,
            payload_key="operations",
        ),
        f"{prefix}_delete": RegosTool(
            name=f"{prefix}_delete",
            description=f"Delete rows/operations from a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "delete"),
            regos_method=f"{method}/Delete",
            mutating=True,
            input_schema=OPERATIONS_SCHEMA,
            payload_key="operations",
        ),
        f"{prefix}_move_operations": RegosTool(
            name=f"{prefix}_move_operations",
            description=f"Move/reorder rows in a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "move_operations"),
            regos_method=f"{method}/MoveOperations",
            mutating=True,
            input_schema=MOVE_OPERATIONS_SCHEMA,
        ),
    }
    if "add_bulk" in extra_actions:
        tools[f"{prefix}_add_bulk"] = RegosTool(
            name=f"{prefix}_add_bulk",
            description=f"Bulk add rows/operations to a {title} document in REGOS. Requires explicit user confirmation.",
            service_path=("docs", service, "add_bulk"),
            regos_method=f"{method}/AddBulk",
            mutating=True,
            input_schema=object_schema({"doc_id": ID, "operations": {"type": "array", "items": {"type": "object"}}}),
        )
    if "set_price_by_price_type" in extra_actions:
        tools[f"{prefix}_set_price_by_price_type"] = RegosTool(
            name=f"{prefix}_set_price_by_price_type",
            description=f"Set row prices by price type for {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "set_price_by_price_type"),
            regos_method=f"{method}/SetPriceByPriceType",
            mutating=True,
            input_schema=SET_PRICE_SCHEMA,
        )
    if "set_cost_by_last_purchase" in extra_actions:
        tools[f"{prefix}_set_cost_by_last_purchase"] = RegosTool(
            name=f"{prefix}_set_cost_by_last_purchase",
            description=f"Set operation cost by last purchase for {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "set_cost_by_last_purchase"),
            regos_method=f"{method}/SetCostByLastPurchase",
            mutating=True,
            input_schema=SET_COST_SCHEMA,
        )
    if "copy_from_inventory" in extra_actions:
        tools[f"{prefix}_copy_from_inventory"] = RegosTool(
            name=f"{prefix}_copy_from_inventory",
            description=f"Copy rows from an inventory document into {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "copy_operations_from_doc_inventory"),
            regos_method=f"{method}/CopyOperationsFromDocInventory",
            mutating=True,
            input_schema=COPY_OPERATIONS_SCHEMA,
        )
    if "copy_from_purchase" in extra_actions:
        tools[f"{prefix}_copy_from_purchase"] = RegosTool(
            name=f"{prefix}_copy_from_purchase",
            description=f"Copy rows from a purchase document into {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "copy_operations_from_doc_purchase"),
            regos_method=f"{method}/CopyOperationsFromDocPurchase",
            mutating=True,
            input_schema=COPY_OPERATIONS_SCHEMA,
        )
    if "copy_from_whole_sale" in extra_actions:
        tools[f"{prefix}_copy_from_whole_sale"] = RegosTool(
            name=f"{prefix}_copy_from_whole_sale",
            description=f"Copy rows from a wholesale document into {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "copy_operations_from_doc_whole_sale"),
            regos_method=f"{method}/CopyOperationsFromDocWholeSale",
            mutating=True,
            input_schema=COPY_OPERATIONS_SCHEMA,
        )
    if "discounts" in extra_actions:
        tools[f"{prefix}_discount_get"] = RegosTool(
            name=f"{prefix}_discount_get",
            description=f"Get operation discounts for {title} documents in REGOS.",
            service_path=("docs", service, "get_discount"),
            regos_method=f"{method}/GetDiscount",
            mutating=False,
            input_schema=DISCOUNT_SCHEMA,
        )
        tools[f"{prefix}_discount_add"] = RegosTool(
            name=f"{prefix}_discount_add",
            description=f"Add operation discount for {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "add_discount"),
            regos_method=f"{method}/AddDiscount",
            mutating=True,
            input_schema=DISCOUNT_SCHEMA,
        )
        tools[f"{prefix}_discount_delete"] = RegosTool(
            name=f"{prefix}_discount_delete",
            description=f"Delete operation discount for {title}. Requires explicit user confirmation.",
            service_path=("docs", service, "delete_discount"),
            regos_method=f"{method}/DeleteDiscount",
            mutating=True,
            input_schema=DISCOUNT_SCHEMA,
        )
    return tools


STORE_TOOLS: Dict[str, RegosTool] = {
    **_doc_tools(
        prefix="doc_inventory",
        title="inventory",
        service="doc_inventory",
        method="DocInventory",
        lifecycle="close",
    ),
    **_operation_tools(
        prefix="inventory_operation",
        title="inventory",
        service="inventory_operation",
        method="InventoryOperation",
        extra_actions=("add_bulk", "set_price_by_price_type"),
    ),
    **_doc_tools(
        prefix="doc_movement",
        title="stock movement",
        service="doc_movement",
        method="DocMovement",
    ),
    **_operation_tools(
        prefix="movement_operation",
        title="stock movement",
        service="movement_operation",
        method="MovementOperation",
        extra_actions=("set_price_by_price_type",),
    ),
    **_doc_tools(
        prefix="doc_in_out",
        title="stock in/out",
        service="doc_in_out",
        method="DocInOut",
    ),
    **_operation_tools(
        prefix="in_out_operation",
        title="stock in/out",
        service="in_out_operation",
        method="InOutOperation",
        extra_actions=("copy_from_inventory",),
    ),
    **_doc_tools(
        prefix="doc_purchase",
        title="purchase",
        service="doc_purchase",
        method="DocPurchase",
    ),
    **_operation_tools(
        prefix="purchase_operation",
        title="purchase",
        service="purchase_operation",
        method="PurchaseOperation",
        extra_actions=(
            "set_cost_by_last_purchase",
            "set_price_by_price_type",
            "copy_from_whole_sale",
            "discounts",
        ),
    ),
    **_doc_tools(
        prefix="doc_whole_sale",
        title="wholesale",
        service="doc_whole_sale",
        method="DocWholeSale",
    ),
    **_operation_tools(
        prefix="whole_sale_operation",
        title="wholesale",
        service="whole_sale_operation",
        method="WholeSaleOperation",
        extra_actions=(
            "set_price_by_price_type",
            "copy_from_purchase",
            "discounts",
        ),
    ),
    "doc_stock_aggregation_get": RegosTool(
        name="doc_stock_aggregation_get",
        description="Find stock aggregation documents in REGOS.",
        service_path=("docs", "doc_stock_aggregation", "get"),
        regos_method="DocStockAggregation/Get",
        mutating=False,
        input_schema=DOC_FILTER_SCHEMA,
    ),
    "stock_aggregation_operation_get": RegosTool(
        name="stock_aggregation_operation_get",
        description="Find stock aggregation rows/operations in REGOS.",
        service_path=("docs", "stock_agregation_operation", "get"),
        regos_method="StockAgregationOperation/Get",
        mutating=False,
        input_schema=OPERATION_FILTER_SCHEMA,
    ),
}

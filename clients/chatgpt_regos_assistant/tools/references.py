from __future__ import annotations

from typing import Dict

from ..models import RegosTool
from .common import (
    AMOUNT,
    BOOLEAN,
    DATE_TIME,
    FILTER_SCHEMA,
    ID,
    IDS,
    LIMIT,
    OFFSET,
    QUANTITY,
    SEARCH,
    object_schema,
)


ITEM_FILTER_SCHEMA = object_schema(
    {
        "ids": IDS,
        "group_ids": IDS,
        "item_group_ids": IDS,
        "brand_ids": IDS,
        "producer_ids": IDS,
        "barcodes": {"type": "array", "items": {"type": "string"}},
        "code": {"type": "string"},
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

ITEM_MUTATION_SCHEMA = object_schema(
    {
        "id": ID,
        "name": {"type": "string"},
        "full_name": {"type": "string"},
        "code": {"type": "string"},
        "article": {"type": "string"},
        "item_group_id": ID,
        "group_id": ID,
        "brand_id": ID,
        "producer_id": ID,
        "unit_id": ID,
        "tax_vat_id": ID,
        "is_service": BOOLEAN,
        "is_active": BOOLEAN,
        "description": {"type": "string"},
    }
)
ITEM_EDIT_SCHEMA = object_schema(ITEM_MUTATION_SCHEMA["properties"], required=("id",))

ITEM_QUANTITY_SCHEMA = object_schema(
    {
        "item_ids": IDS,
        "stock_ids": IDS,
        "firm_ids": IDS,
        "date": DATE_TIME,
        "date_from": DATE_TIME,
        "date_to": DATE_TIME,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

ITEM_OPERATION_FILTER_SCHEMA = object_schema(
    {
        "ids": IDS,
        "item_ids": IDS,
        "stock_ids": IDS,
        "firm_ids": IDS,
        "doc_ids": IDS,
        "document_ids": IDS,
        "date_from": DATE_TIME,
        "date_to": DATE_TIME,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

ITEM_GROUP_SCHEMA = object_schema(
    {
        "id": ID,
        "ids": IDS,
        "parent_id": ID,
        "name": {"type": "string"},
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)
ITEM_GROUP_EDIT_SCHEMA = object_schema(ITEM_GROUP_SCHEMA["properties"], required=("id",))

BARCODE_SCHEMA = object_schema(
    {
        "id": ID,
        "ids": IDS,
        "item_id": ID,
        "item_ids": IDS,
        "barcode": {"type": "string"},
        "barcodes": {"type": "array", "items": {"type": "string"}},
        "is_base": BOOLEAN,
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

ITEM_PRICE_SCHEMA = object_schema(
    {
        "item_ids": IDS,
        "price_type_ids": IDS,
        "stock_ids": IDS,
        "firm_ids": IDS,
        "date": DATE_TIME,
        "price": AMOUNT,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)

STOCK_SCHEMA = object_schema(
    {
        "id": ID,
        "ids": IDS,
        "firm_ids": IDS,
        "name": {"type": "string"},
        "address": {"type": "string"},
        "search": SEARCH,
        "limit": LIMIT,
        "offset": OFFSET,
    }
)
STOCK_EDIT_SCHEMA = object_schema(STOCK_SCHEMA["properties"], required=("id",))

COMPOUND_SCHEMA = object_schema(
    {
        "compound_id": ID,
        "item_id": ID,
        "quantity": QUANTITY,
    },
    required=("compound_id", "item_id", "quantity"),
)


REFERENCES_TOOLS: Dict[str, RegosTool] = {
    "item_get": RegosTool(
        name="item_get",
        description="Find goods/items in REGOS by id, barcode, code, group, brand, search, limit and offset.",
        service_path=("references", "item", "get"),
        regos_method="Item/Get",
        mutating=False,
        input_schema=ITEM_FILTER_SCHEMA,
    ),
    "item_get_short": RegosTool(
        name="item_get_short",
        description="Find compact goods/items data in REGOS.",
        service_path=("references", "item", "get_short"),
        regos_method="Item/GetShort",
        mutating=False,
        input_schema=ITEM_FILTER_SCHEMA,
    ),
    "item_get_ext": RegosTool(
        name="item_get_ext",
        description="Find extended goods/items data in REGOS.",
        service_path=("references", "item", "get_ext"),
        regos_method="Item/GetExt",
        mutating=False,
        input_schema=ITEM_FILTER_SCHEMA,
    ),
    "item_search": RegosTool(
        name="item_search",
        description="Search REGOS items and return matching item ids.",
        service_path=("references", "item", "search"),
        regos_method="Item/Search",
        mutating=False,
        input_schema=ITEM_FILTER_SCHEMA,
    ),
    "item_add": RegosTool(
        name="item_add",
        description="Create an item/good in REGOS. Requires explicit user confirmation.",
        service_path=("references", "item", "add"),
        regos_method="Item/Add",
        mutating=True,
        input_schema=ITEM_MUTATION_SCHEMA,
    ),
    "item_copy": RegosTool(
        name="item_copy",
        description="Copy an existing REGOS item. Requires explicit user confirmation.",
        service_path=("references", "item", "copy"),
        regos_method="Item/Copy",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "item_edit": RegosTool(
        name="item_edit",
        description="Update an item/good in REGOS. Requires explicit user confirmation.",
        service_path=("references", "item", "edit"),
        regos_method="Item/Edit",
        mutating=True,
        input_schema=ITEM_EDIT_SCHEMA,
    ),
    "item_delete_mark": RegosTool(
        name="item_delete_mark",
        description="Mark REGOS items as deleted. Requires explicit user confirmation.",
        service_path=("references", "item", "delete_mark"),
        regos_method="Item/DeleteMark",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "item_delete": RegosTool(
        name="item_delete",
        description="Delete REGOS items. Requires explicit user confirmation.",
        service_path=("references", "item", "delete"),
        regos_method="Item/Delete",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "item_check_code": RegosTool(
        name="item_check_code",
        description="Check whether an item code is available in REGOS.",
        service_path=("references", "item", "check_code"),
        regos_method="Item/CheckCode",
        mutating=False,
        input_schema=object_schema({"code": {"type": "string"}}, required=("code",)),
    ),
    "item_get_code": RegosTool(
        name="item_get_code",
        description="Get or generate the next item code from REGOS.",
        service_path=("references", "item", "get_code"),
        regos_method="Item/GetCode",
        mutating=False,
        input_schema=object_schema({"prefix": {"type": "string"}}),
    ),
    "item_get_quantity": RegosTool(
        name="item_get_quantity",
        description="Get item quantities by item, stock, firm and date filters.",
        service_path=("references", "item", "get_quantity"),
        regos_method="Item/GetQuantity",
        mutating=False,
        input_schema=ITEM_QUANTITY_SCHEMA,
    ),
    "item_get_current_quantity": RegosTool(
        name="item_get_current_quantity",
        description="Get current item quantity balances by item, stock and firm filters.",
        service_path=("references", "item", "get_current_quantity"),
        regos_method="Item/GetCurrentQuantity",
        mutating=False,
        input_schema=ITEM_QUANTITY_SCHEMA,
    ),
    "item_operation_get": RegosTool(
        name="item_operation_get",
        description="Find item movement/stock operations in REGOS.",
        service_path=("references", "item_operation", "get"),
        regos_method="ItemOperation/Get",
        mutating=False,
        input_schema=ITEM_OPERATION_FILTER_SCHEMA,
    ),
    "item_get_compound": RegosTool(
        name="item_get_compound",
        description="Get compound/composition rows for a REGOS item.",
        service_path=("references", "item", "get_compound"),
        regos_method="Item/GetCompound",
        mutating=False,
        input_schema=object_schema({"item_id": ID}, required=("item_id",)),
    ),
    "item_add_to_compound": RegosTool(
        name="item_add_to_compound",
        description="Add a component to a compound REGOS item. Requires explicit user confirmation.",
        service_path=("references", "item", "add_to_compound"),
        regos_method="Item/AddToCompound",
        mutating=True,
        input_schema=COMPOUND_SCHEMA,
    ),
    "item_delete_from_compound": RegosTool(
        name="item_delete_from_compound",
        description="Delete a component from a compound REGOS item. Requires explicit user confirmation.",
        service_path=("references", "item", "delete_from_compound"),
        regos_method="Item/DeleteFromCompound",
        mutating=True,
        input_schema=object_schema(
            {"compound_id": ID, "item_id": ID},
            required=("compound_id", "item_id"),
        ),
    ),
    "item_group_get": RegosTool(
        name="item_group_get",
        description="Find item groups/categories in REGOS.",
        service_path=("references", "item_group", "get"),
        regos_method="ItemGroup/Get",
        mutating=False,
        input_schema=ITEM_GROUP_SCHEMA,
    ),
    "item_group_add": RegosTool(
        name="item_group_add",
        description="Create an item group/category in REGOS. Requires explicit user confirmation.",
        service_path=("references", "item_group", "add"),
        regos_method="ItemGroup/Add",
        mutating=True,
        input_schema=ITEM_GROUP_SCHEMA,
    ),
    "item_group_edit": RegosTool(
        name="item_group_edit",
        description="Update an item group/category in REGOS. Requires explicit user confirmation.",
        service_path=("references", "item_group", "edit"),
        regos_method="ItemGroup/Edit",
        mutating=True,
        input_schema=ITEM_GROUP_EDIT_SCHEMA,
    ),
    "item_group_delete": RegosTool(
        name="item_group_delete",
        description="Delete item groups/categories in REGOS. Requires explicit user confirmation.",
        service_path=("references", "item_group", "delete"),
        regos_method="ItemGroup/Delete",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "barcode_get": RegosTool(
        name="barcode_get",
        description="Find item barcodes in REGOS.",
        service_path=("references", "barcode", "get"),
        regos_method="Barcode/Get",
        mutating=False,
        input_schema=BARCODE_SCHEMA,
    ),
    "barcode_add": RegosTool(
        name="barcode_add",
        description="Add a barcode to a REGOS item. Requires explicit user confirmation.",
        service_path=("references", "barcode", "add"),
        regos_method="Barcode/Add",
        mutating=True,
        input_schema=BARCODE_SCHEMA,
    ),
    "barcode_add_ean13": RegosTool(
        name="barcode_add_ean13",
        description="Generate and add an EAN13 barcode to a REGOS item. Requires explicit user confirmation.",
        service_path=("references", "barcode", "add_ean13"),
        regos_method="Barcode/AddEAN13",
        mutating=True,
        input_schema=object_schema({"item_id": ID}, required=("item_id",)),
    ),
    "barcode_set_base": RegosTool(
        name="barcode_set_base",
        description="Set the base barcode for a REGOS item. Requires explicit user confirmation.",
        service_path=("references", "barcode", "set_base"),
        regos_method="Barcode/SetBase",
        mutating=True,
        input_schema=object_schema({"id": ID, "item_id": ID}, required=("id",)),
    ),
    "barcode_delete": RegosTool(
        name="barcode_delete",
        description="Delete item barcodes in REGOS. Requires explicit user confirmation.",
        service_path=("references", "barcode", "delete"),
        regos_method="Barcode/Delete",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "barcode_generate_ean13": RegosTool(
        name="barcode_generate_ean13",
        description="Generate an EAN13 barcode value in REGOS.",
        service_path=("references", "barcode", "generate_ean13"),
        regos_method="Barcode/GenerateEan13",
        mutating=False,
        input_schema=object_schema({}),
    ),
    "item_price_get": RegosTool(
        name="item_price_get",
        description="Get item prices by item, price type, stock, firm and date filters.",
        service_path=("references", "item_price", "get"),
        regos_method="ItemPrice/Get",
        mutating=False,
        input_schema=ITEM_PRICE_SCHEMA,
    ),
    "item_price_get_pre_cost": RegosTool(
        name="item_price_get_pre_cost",
        description="Get item pre-cost/cost data in REGOS.",
        service_path=("references", "item_price", "get_pre_cost"),
        regos_method="ItemPrice/GetPreCost",
        mutating=False,
        input_schema=ITEM_PRICE_SCHEMA,
    ),
    "stock_get": RegosTool(
        name="stock_get",
        description="Find stocks/warehouses in REGOS by id, firm, search, limit and offset.",
        service_path=("references", "stock", "get"),
        regos_method="Stock/Get",
        mutating=False,
        input_schema=STOCK_SCHEMA,
    ),
    "stock_add": RegosTool(
        name="stock_add",
        description="Create a warehouse/stock in REGOS. Requires explicit user confirmation.",
        service_path=("references", "stock", "add"),
        regos_method="Stock/Add",
        mutating=True,
        input_schema=STOCK_SCHEMA,
    ),
    "stock_edit": RegosTool(
        name="stock_edit",
        description="Update a warehouse/stock in REGOS. Requires explicit user confirmation.",
        service_path=("references", "stock", "edit"),
        regos_method="Stock/Edit",
        mutating=True,
        input_schema=STOCK_EDIT_SCHEMA,
    ),
    "stock_delete_mark": RegosTool(
        name="stock_delete_mark",
        description="Mark warehouses/stocks as deleted. Requires explicit user confirmation.",
        service_path=("references", "stock", "delete_mark"),
        regos_method="Stock/DeleteMark",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "stock_delete": RegosTool(
        name="stock_delete",
        description="Delete warehouses/stocks in REGOS. Requires explicit user confirmation.",
        service_path=("references", "stock", "delete"),
        regos_method="Stock/Delete",
        mutating=True,
        input_schema=object_schema({"id": ID}, required=("id",)),
    ),
    "stock_delete_confirm": RegosTool(
        name="stock_delete_confirm",
        description="Confirm warehouse/stock deletion in REGOS. Requires explicit user confirmation.",
        service_path=("references", "stock", "delete_confirm"),
        regos_method="Stock/DeleteConfirm",
        mutating=True,
        input_schema=object_schema(
            {"id": ID, "confirm_code": {"type": "string"}},
            required=("id",),
        ),
    ),
    "brand_get": RegosTool(
        name="brand_get",
        description="Find item brands in REGOS.",
        service_path=("references", "brand", "get"),
        regos_method="Brand/Get",
        mutating=False,
        input_schema=FILTER_SCHEMA,
    ),
    "unit_get": RegosTool(
        name="unit_get",
        description="Find item measurement units in REGOS.",
        service_path=("references", "unit", "get"),
        regos_method="Unit/Get",
        mutating=False,
        input_schema=FILTER_SCHEMA,
    ),
    "price_type_get": RegosTool(
        name="price_type_get",
        description="Find price types in REGOS.",
        service_path=("references", "price_type", "get"),
        regos_method="PriceType/Get",
        mutating=False,
        input_schema=FILTER_SCHEMA,
    ),
}

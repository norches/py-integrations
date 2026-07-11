"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class GetWithoutICPSRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ImageSize(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ImportItems(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    comparation_value: ItemImportComparationValue | None = PydField(default=None)
    group_separator: str | None = PydField(default=None)
    barcode_separator: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    unit_id: int | None = PydField(default=None)
    vat_value_id: int | None = PydField(default=None)
    data: list[ItemImportData] | None = PydField(default=None)


class Int64ArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[int] | Error | None = PydField(default=None)


class Item(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    type: ItemType | None = PydField(default=None)
    code: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    kdt: int | None = PydField(default=None)
    icps: str | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    is_labeled: bool | None = PydField(default=None)
    comission_tin: str | None = PydField(default=None)
    package_code: str | None = PydField(default=None)
    origin: ItemOriginEnum | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group: ItemGroup | None = PydField(default=None)
    department: Department | None = PydField(default=None)
    vat: TaxVat | None = PydField(default=None)
    barcode_list: str | None = PydField(default=None)
    base_barcode: str | None = PydField(default=None)
    unit: Unit | None = PydField(default=None)
    unit2: Unit | None = PydField(default=None)
    color: Color | None = PydField(default=None)
    size: SizeChart | None = PydField(default=None)
    brand: Brand | None = PydField(default=None)
    producer: Producer | None = PydField(default=None)
    country: Country | None = PydField(default=None)
    compound: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    image_url: str | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    has_child: bool | None = PydField(default=None)
    min_quantity: int | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ItemAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: ItemType | None = PydField(default=None)
    code: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    kdt: int | None = PydField(default=None)
    icps: str | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    is_labeled: bool | None = PydField(default=None)
    comission_tin: str | None = PydField(default=None)
    package_code: str | None = PydField(default=None)
    origin: ItemOriginEnum | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    department_id: int | None = PydField(default=None)
    vat_id: int | None = PydField(default=None)
    unit_id: int | None = PydField(default=None)
    unit2_id: int | None = PydField(default=None)
    color_id: int | None = PydField(default=None)
    size_id: int | None = PydField(default=None)
    brand_id: int | None = PydField(default=None)
    producer_id: int | None = PydField(default=None)
    country_id: int | None = PydField(default=None)
    compound: bool | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    min_quantity: int | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class ItemAddCopy(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ItemAddToCompound(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    compound_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)


class ItemCodeCheckIn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code: int | None = PydField(default=None)


class ItemCodeCheckOut(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    enable: bool | None = PydField(default=None)


class ItemCodeCheckOutRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: ItemCodeCheckOut | Error | None = PydField(default=None)


class ItemCodeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code: int | None = PydField(default=None)


class ItemCodeGetRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: ItemCodeGet | Error | None = PydField(default=None)


class ItemCompound(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    image_url: str | None = PydField(default=None)


class ItemCompoundGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    image_size: ImageSize | None = PydField(default=None)


class ItemCompoundRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemCompound] | Error | None = PydField(default=None)


class ItemCurrentQuantity(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)


class ItemCurrentQuantityGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)


class ItemCurrentQuantityRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemCurrentQuantity] | Error | None = PydField(default=None)


class ItemDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ItemDeleteFromCompound(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    compound_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)


class ItemDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ItemEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: ItemType | None = PydField(default=None)
    code: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    kdt: int | None = PydField(default=None)
    icps: str | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    is_labeled: bool | None = PydField(default=None)
    comission_tin: str | None = PydField(default=None)
    package_code: str | None = PydField(default=None)
    origin: ItemOriginEnum | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    department_id: int | None = PydField(default=None)
    vat_id: int | None = PydField(default=None)
    unit_id: int | None = PydField(default=None)
    unit2_id: int | None = PydField(default=None)
    color_id: int | None = PydField(default=None)
    size_id: int | None = PydField(default=None)
    brand_id: int | None = PydField(default=None)
    producer_id: int | None = PydField(default=None)
    country_id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    min_quantity: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class ItemExt(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    item: Item | None = PydField(default=None)
    quantity: ItemQuantity | None = PydField(default=None)
    pricetype: PriceType | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    last_purchase_cost: _Decimal | None = PydField(default=None)
    image_url: str | None = PydField(default=None)


class ItemExtGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    type: ItemType | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)
    codes: list[int] | None = PydField(default=None)
    department_ids: list[int] | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    compound: bool | None = PydField(default=None)
    has_child: bool | None = PydField(default=None)
    is_labeled: bool | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    sort_orders: list[ItemOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    zero_quantity: bool | None = PydField(default=None)
    zero_price: bool | None = PydField(default=None)
    has_image: bool | None = PydField(default=None)
    image_size: ImageSize | None = PydField(default=None)


class ItemExtRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemExt] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ItemGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    type: ItemType | None = PydField(default=None)
    parent_ids: list[int] | None = PydField(default=None)
    codes: list[int] | None = PydField(default=None)
    department_ids: list[int] | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    compound: bool | None = PydField(default=None)
    has_child: bool | None = PydField(default=None)
    is_labeled: bool | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ItemGetQuantityIncome(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    date: int | None = PydField(default=None)


class ItemGetQuantityOutcome(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    common: _Decimal | None = PydField(default=None)
    allowed: _Decimal | None = PydField(default=None)
    booked: _Decimal | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)


class ItemGetQuantityOutcomeRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemGetQuantityOutcome] | Error | None = PydField(default=None)


class ItemGetQuantityPosIncome(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    date: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class ItemGetQuantityPosOutcome(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    common: _Decimal | None = PydField(default=None)
    allowed: _Decimal | None = PydField(default=None)
    booked: _Decimal | None = PydField(default=None)
    stock_name: str | None = PydField(default=None)
    firm_name: str | None = PydField(default=None)


class ItemGetQuantityPosOutcomeRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemGetQuantityPosOutcome] | Error | None = PydField(default=None)


class ItemImportComparationValue(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class ItemImportData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    index: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    group_path: str | None = PydField(default=None)
    barcodes: str | None = PydField(default=None)
    color_name: str | None = PydField(default=None)
    brand_name: str | None = PydField(default=None)
    producer_name: str | None = PydField(default=None)
    size_name: str | None = PydField(default=None)
    unit_name: str | None = PydField(default=None)
    department_name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_name: str | None = PydField(default=None)
    icps: str | None = PydField(default=None)
    icpsbarcode: str | None = PydField(default=None)
    labeled: int | None = PydField(default=None)
    package_code: int | None = PydField(default=None)
    parent_code: int | None = PydField(default=None)


class ItemImportDataResponse(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    success: bool | None = PydField(default=None)
    index: str | None = PydField(default=None)
    item_id: int | None = PydField(default=None)


class ItemImportDataResponseArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemImportDataResponse] | Error | None = PydField(default=None)


class ItemMatchingRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: MatchingType | None = PydField(default=None)
    data: list[ItemMatchingRequestData] | None = PydField(default=None)


class ItemMatchingRequestData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    index: str | None = PydField(default=None)
    value: str | None = PydField(default=None)


class ItemMatchingResponse(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    index: str | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)


class ItemMatchingResponseArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemMatchingResponse] | Error | None = PydField(default=None)


class ItemOFDPackage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    code: str | None = PydField(default=None)
    nameUz: str | None = PydField(default=None)
    nameRu: str | None = PydField(default=None)
    nameLat: str | None = PydField(default=None)


class ItemOFDPackageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemOFDPackage] | Error | None = PydField(default=None)


class ItemOFDPackagesGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    icps: str | None = PydField(default=None)


class ItemOprOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: ItemOprOrderColumn | None = PydField(default=None)
    direction: ItemOprOrderDirection | None = PydField(default=None)


class ItemOprOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class ItemOprOrderDirection(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class ItemOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: ItemOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class ItemOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11


class ItemOriginEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    NEGATIVE_1 = -1


class ItemPreCost(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    item_id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    cost_date: int | None = PydField(default=None)


class ItemPreCostArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemPreCost] | Error | None = PydField(default=None)


class ItemPreCostGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    item_ids: list[int] | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    cost_date: int | None = PydField(default=None)


class ItemQuantity(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    common: _Decimal | None = PydField(default=None)
    allowed: _Decimal | None = PydField(default=None)
    booked: _Decimal | None = PydField(default=None)


class ItemRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Item] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ItemReplaceICPS(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    old_icps: str | None = PydField(default=None)
    new_icps: str | None = PydField(default=None)


class ItemSearch(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    barcode: str | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    compound: bool | None = PydField(default=None)
    has_child: bool | None = PydField(default=None)
    type: ItemType | None = PydField(default=None)


class ItemSetICPS(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    icps: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)


class ItemShort(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    type: ItemType | None = PydField(default=None)
    code: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    articul: str | None = PydField(default=None)
    kdt: int | None = PydField(default=None)
    icps: str | None = PydField(default=None)
    assemblable: bool | None = PydField(default=None)
    disassemblable: bool | None = PydField(default=None)
    is_labeled: bool | None = PydField(default=None)
    comission_tin: str | None = PydField(default=None)
    package_code: str | None = PydField(default=None)
    origin: ItemOriginEnum | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    department_id: int | None = PydField(default=None)
    vat_id: int | None = PydField(default=None)
    unit_id: int | None = PydField(default=None)
    unit2_id: int | None = PydField(default=None)
    color_id: int | None = PydField(default=None)
    size_id: int | None = PydField(default=None)
    brand_id: int | None = PydField(default=None)
    producer_id: int | None = PydField(default=None)
    country_id: int | None = PydField(default=None)
    compound: bool | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    has_child: bool | None = PydField(default=None)
    min_quantity: int | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    base_barcode: str | None = PydField(default=None)


class ItemShortRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemShort] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ItemType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2


class ItemWithoutICPS(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    barcode: str | None = PydField(default=None)
    name: str | None = PydField(default=None)


class ItemWithoutICPSRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemWithoutICPS] | Error | None = PydField(default=None)


class ItemWithoutICPSShort(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    barcode: str | None = PydField(default=None)


class ItemWithoutICPSShortRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ItemWithoutICPSShort] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class MatchingType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BooleanRegosObjectResult, ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.references.brand import Brand
from schemas.api.references.color import Color
from schemas.api.references.country import Country
from schemas.api.references.department import Department
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit
from schemas.api.references.item_group import ItemGroup
from schemas.api.references.price_type import PriceType
from schemas.api.references.producer import Producer
from schemas.api.references.size_chart import SizeChart
from schemas.api.references.stock import Stock
from schemas.api.references.tax_vat import TaxVat
from schemas.api.references.unit import Unit


ItemAddRequest: TypeAlias = ItemAdd
ItemAddResponse: TypeAlias = InsertResult
ItemAddToCompoundRequest: TypeAlias = ItemAddToCompound
ItemAddToCompoundResponse: TypeAlias = UpdateResult
ItemCheckCodeRequest: TypeAlias = ItemCodeCheckIn
ItemCheckCodeResponse: TypeAlias = ItemCodeCheckOutRegosObjectResult
ItemCopyRequest: TypeAlias = ItemAddCopy
ItemCopyResponse: TypeAlias = InsertResult
ItemDeleteFromCompoundRequest: TypeAlias = ItemDeleteFromCompound
ItemDeleteFromCompoundResponse: TypeAlias = UpdateResult
ItemDeleteMarkRequest: TypeAlias = ItemDeleteMark
ItemDeleteMarkResponse: TypeAlias = UpdateResult
ItemDeleteRequest: TypeAlias = ItemDelete
ItemDeleteResponse: TypeAlias = UpdateResult
ItemEditRequest: TypeAlias = ItemEdit
ItemEditResponse: TypeAlias = UpdateResult
ItemFillIcpsByBarcodeRequest: TypeAlias = list[ItemWithoutICPSShort]
ItemFillIcpsByBarcodeResponse: TypeAlias = ItemWithoutICPSRegosArrayResult
ItemGetCodeRequest: TypeAlias = ItemCodeGet
ItemGetCodeResponse: TypeAlias = ItemCodeGetRegosObjectResult
ItemGetCompoundRequest: TypeAlias = ItemCompoundGet
ItemGetCompoundResponse: TypeAlias = ItemCompoundRegosArrayResult
ItemGetCurrentQuantityRequest: TypeAlias = ItemCurrentQuantityGet
ItemGetCurrentQuantityResponse: TypeAlias = ItemCurrentQuantityRegosArrayResult
ItemGetExtImageSize: TypeAlias = ImageSize
ItemGetExtRequest: TypeAlias = ItemExtGet
ItemGetExtResponse: TypeAlias = ItemExtRegosOffsettedArrayResult
ItemGetPackagesByIcpsRequest: TypeAlias = ItemOFDPackagesGet
ItemGetPackagesByIcpsResponse: TypeAlias = ItemOFDPackageRegosArrayResult
ItemGetQuantityPosRequest: TypeAlias = ItemGetQuantityPosIncome
ItemGetQuantityPosResponse: TypeAlias = ItemGetQuantityPosOutcomeRegosArrayResult
ItemGetQuantityRequest: TypeAlias = ItemGetQuantityIncome
ItemGetQuantityResponse: TypeAlias = ItemGetQuantityOutcomeRegosArrayResult
ItemGetRequest: TypeAlias = ItemGet
ItemGetResponse: TypeAlias = ItemRegosOffsettedArrayResult
ItemGetShortRequest: TypeAlias = ItemGet
ItemGetShortResponse: TypeAlias = ItemShortRegosOffsettedArrayResult
ItemGetWithoutIcpsRequest: TypeAlias = GetWithoutICPSRequest
ItemGetWithoutIcpsResponse: TypeAlias = ItemWithoutICPSShortRegosOffsettedArrayResult
ItemImportRequest: TypeAlias = ImportItems
ItemImportResponse: TypeAlias = ItemImportDataResponseArrayRegosObjectResult
ItemMatchRequest: TypeAlias = ItemMatchingRequest
ItemMatchResponse: TypeAlias = ItemMatchingResponseArrayRegosObjectResult
ItemMatchingData: TypeAlias = ItemMatchingRequestData
ItemMatchingType: TypeAlias = MatchingType
ItemReplaceIcpsRequest: TypeAlias = ItemReplaceICPS
ItemReplaceIcpsResponse: TypeAlias = BooleanRegosObjectResult
ItemSearchRequest: TypeAlias = ItemSearch
ItemSearchResponse: TypeAlias = Int64ArrayRegosObjectResult
ItemSetIcpsFromServerRequest: TypeAlias = list[ItemWithoutICPSShort]
ItemSetIcpsFromServerResponse: TypeAlias = ItemWithoutICPSRegosArrayResult
ItemSetIcpsRequest: TypeAlias = ItemSetICPS
ItemSetIcpsResponse: TypeAlias = BooleanRegosObjectResult
ItemSetLabeledMarkResponse: TypeAlias = BooleanRegosObjectResult


_MODEL_NAMES = ['GetWithoutICPSRequest', 'ImportItems', 'Int64ArrayRegosObjectResult', 'Item', 'ItemAdd', 'ItemAddCopy', 'ItemAddToCompound', 'ItemCodeCheckIn', 'ItemCodeCheckOut', 'ItemCodeCheckOutRegosObjectResult', 'ItemCodeGet', 'ItemCodeGetRegosObjectResult', 'ItemCompound', 'ItemCompoundGet', 'ItemCompoundRegosArrayResult', 'ItemCurrentQuantity', 'ItemCurrentQuantityGet', 'ItemCurrentQuantityRegosArrayResult', 'ItemDelete', 'ItemDeleteFromCompound', 'ItemDeleteMark', 'ItemEdit', 'ItemExt', 'ItemExtGet', 'ItemExtRegosOffsettedArrayResult', 'ItemGet', 'ItemGetQuantityIncome', 'ItemGetQuantityOutcome', 'ItemGetQuantityOutcomeRegosArrayResult', 'ItemGetQuantityPosIncome', 'ItemGetQuantityPosOutcome', 'ItemGetQuantityPosOutcomeRegosArrayResult', 'ItemImportData', 'ItemImportDataResponse', 'ItemImportDataResponseArrayRegosObjectResult', 'ItemMatchingRequest', 'ItemMatchingRequestData', 'ItemMatchingResponse', 'ItemMatchingResponseArrayRegosObjectResult', 'ItemOFDPackage', 'ItemOFDPackageRegosArrayResult', 'ItemOFDPackagesGet', 'ItemOprOrder', 'ItemOrder', 'ItemPreCost', 'ItemPreCostArrayRegosObjectResult', 'ItemPreCostGet', 'ItemQuantity', 'ItemRegosOffsettedArrayResult', 'ItemReplaceICPS', 'ItemSearch', 'ItemSetICPS', 'ItemShort', 'ItemShortRegosOffsettedArrayResult', 'ItemWithoutICPS', 'ItemWithoutICPSRegosArrayResult', 'ItemWithoutICPSShort', 'ItemWithoutICPSShortRegosOffsettedArrayResult']


__all__ = [
    'GetWithoutICPSRequest',
    'ImageSize',
    'ImportItems',
    'Int64ArrayRegosObjectResult',
    'Item',
    'ItemAdd',
    'ItemAddCopy',
    'ItemAddToCompound',
    'ItemCodeCheckIn',
    'ItemCodeCheckOut',
    'ItemCodeCheckOutRegosObjectResult',
    'ItemCodeGet',
    'ItemCodeGetRegosObjectResult',
    'ItemCompound',
    'ItemCompoundGet',
    'ItemCompoundRegosArrayResult',
    'ItemCurrentQuantity',
    'ItemCurrentQuantityGet',
    'ItemCurrentQuantityRegosArrayResult',
    'ItemDelete',
    'ItemDeleteFromCompound',
    'ItemDeleteMark',
    'ItemEdit',
    'ItemExt',
    'ItemExtGet',
    'ItemExtRegosOffsettedArrayResult',
    'ItemGet',
    'ItemGetQuantityIncome',
    'ItemGetQuantityOutcome',
    'ItemGetQuantityOutcomeRegosArrayResult',
    'ItemGetQuantityPosIncome',
    'ItemGetQuantityPosOutcome',
    'ItemGetQuantityPosOutcomeRegosArrayResult',
    'ItemImportComparationValue',
    'ItemImportData',
    'ItemImportDataResponse',
    'ItemImportDataResponseArrayRegosObjectResult',
    'ItemMatchingRequest',
    'ItemMatchingRequestData',
    'ItemMatchingResponse',
    'ItemMatchingResponseArrayRegosObjectResult',
    'ItemOFDPackage',
    'ItemOFDPackageRegosArrayResult',
    'ItemOFDPackagesGet',
    'ItemOprOrder',
    'ItemOprOrderColumn',
    'ItemOprOrderDirection',
    'ItemOrder',
    'ItemOrderColumn',
    'ItemOriginEnum',
    'ItemPreCost',
    'ItemPreCostArrayRegosObjectResult',
    'ItemPreCostGet',
    'ItemQuantity',
    'ItemRegosOffsettedArrayResult',
    'ItemReplaceICPS',
    'ItemSearch',
    'ItemSetICPS',
    'ItemShort',
    'ItemShortRegosOffsettedArrayResult',
    'ItemType',
    'ItemWithoutICPS',
    'ItemWithoutICPSRegosArrayResult',
    'ItemWithoutICPSShort',
    'ItemWithoutICPSShortRegosOffsettedArrayResult',
    'MatchingType',
    'ItemGetRequest',
    'ItemGetResponse',
    'ItemGetShortRequest',
    'ItemGetShortResponse',
    'ItemGetExtRequest',
    'ItemGetExtResponse',
    'ItemAddRequest',
    'ItemAddResponse',
    'ItemCopyRequest',
    'ItemCopyResponse',
    'ItemEditRequest',
    'ItemEditResponse',
    'ItemDeleteMarkRequest',
    'ItemDeleteMarkResponse',
    'ItemDeleteRequest',
    'ItemDeleteResponse',
    'ItemCheckCodeRequest',
    'ItemCheckCodeResponse',
    'ItemGetCodeRequest',
    'ItemGetCodeResponse',
    'ItemSearchRequest',
    'ItemSearchResponse',
    'ItemGetQuantityRequest',
    'ItemGetQuantityResponse',
    'ItemGetQuantityPosRequest',
    'ItemGetQuantityPosResponse',
    'ItemGetCurrentQuantityRequest',
    'ItemGetCurrentQuantityResponse',
    'ItemMatchRequest',
    'ItemMatchResponse',
    'ItemImportRequest',
    'ItemImportResponse',
    'ItemSetIcpsRequest',
    'ItemSetIcpsResponse',
    'ItemReplaceIcpsRequest',
    'ItemReplaceIcpsResponse',
    'ItemGetWithoutIcpsRequest',
    'ItemGetWithoutIcpsResponse',
    'ItemSetIcpsFromServerRequest',
    'ItemSetIcpsFromServerResponse',
    'ItemSetLabeledMarkResponse',
    'ItemFillIcpsByBarcodeRequest',
    'ItemFillIcpsByBarcodeResponse',
    'ItemGetPackagesByIcpsRequest',
    'ItemGetPackagesByIcpsResponse',
    'ItemGetCompoundRequest',
    'ItemGetCompoundResponse',
    'ItemAddToCompoundRequest',
    'ItemAddToCompoundResponse',
    'ItemDeleteFromCompoundRequest',
    'ItemDeleteFromCompoundResponse',
    'ItemGetExtImageSize',
    'ItemMatchingData',
    'ItemMatchingType'
]

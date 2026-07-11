"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailCard(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    group: RetailCardGroup | None = PydField(default=None)
    customer: RetailCustomer | None = PydField(default=None)
    barcode_value: str | None = PydField(default=None)
    barcode_type: BarcodeType | None = PydField(default=None)
    promo: PromoProgram | None = PydField(default=None)
    bonus_amount: _Decimal | None = PydField(default=None)
    date: int | None = PydField(default=None)
    unlimited: bool | None = PydField(default=None)
    expiry_date: str | None = PydField(default=None)
    last_purchase: int | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailCardAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    group_id: int | None = PydField(default=None)
    customer_id: int | None = PydField(default=None)
    barcode_value: str | None = PydField(default=None)
    barcode_type_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    unlimited: bool | None = PydField(default=None)
    expiry_date: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class RetailCardAddWithCustomer(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    customer_id: int | None = PydField(default=None)
    first_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    main_phone: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    barcode_value: str | None = PydField(default=None)
    barcode_type_id: int | None = PydField(default=None)
    unlimited: bool | None = PydField(default=None)
    expiry_date: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class RetailCardDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class RetailCardEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    customer_id: int | None = PydField(default=None)
    barcode_value: str | None = PydField(default=None)
    barcode_type_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    unlimited: bool | None = PydField(default=None)
    expiry_date: str | None = PydField(default=None)
    enabled: bool | None = PydField(default=None)


class RetailCardGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    customer_ids: list[int] | None = PydField(default=None)
    promo_ids: list[int] | None = PydField(default=None)
    barcode_value: str | None = PydField(default=None)
    sort_orders: list[RetailCard_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailCardOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    type: PromoBonusType | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    used_value: _Decimal | None = PydField(default=None)
    is_payment: bool | None = PydField(default=None)
    date: int | None = PydField(default=None)
    exp_date: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailCardOperationColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: RetailCardOperationColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class RetailCardOperationColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class RetailCardOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuids: list[str] | None = PydField(default=None)
    card_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    type: PromoBonusType | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    sort_orders: list[RetailCardOperationColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailCardOperationRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: RetailCardOperation | Error | None = PydField(default=None)


class RetailCardOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCardOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailCardRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: RetailCard | Error | None = PydField(default=None)


class RetailCardRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCard] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailCard_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: RetailCard_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class RetailCard_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, SexEnum, UpdateResult
from schemas.api.references.barcode_type import BarcodeType
from schemas.api.references.promo_bonus import PromoBonusType, PromoBonusesRemainderGet, PromoBonusesRemainderRegosObjectResult
from schemas.api.references.promo_program import PromoProgram
from schemas.api.references.retail_card_group import RetailCardGroup
from schemas.api.references.retail_card_migration import RetailCardMigrationHistoryGet, RetailCardMigrationHistoryRegosArrayResult
from schemas.api.references.retail_customer import RetailCustomer


RetailCardAddRequest: TypeAlias = RetailCardAdd
RetailCardAddResponse: TypeAlias = InsertResult
RetailCardAddWithCustomerRequest: TypeAlias = RetailCardAddWithCustomer
RetailCardAddWithCustomerResponse: TypeAlias = RetailCardRegosObjectResult
RetailCardDeleteRequest: TypeAlias = RetailCardDelete
RetailCardDeleteResponse: TypeAlias = UpdateResult
RetailCardEditRequest: TypeAlias = RetailCardEdit
RetailCardEditResponse: TypeAlias = UpdateResult
RetailCardGetBalanceRequest: TypeAlias = PromoBonusesRemainderGet
RetailCardGetBalanceResponse: TypeAlias = PromoBonusesRemainderRegosObjectResult
RetailCardGetMigrationHistoryRequest: TypeAlias = RetailCardMigrationHistoryGet
RetailCardGetMigrationHistoryResponse: TypeAlias = RetailCardMigrationHistoryRegosArrayResult
RetailCardGetOperationsRequest: TypeAlias = RetailCardOperationGet
RetailCardGetOperationsResponse: TypeAlias = RetailCardOperationRegosOffsettedArrayResult
RetailCardGetRequest: TypeAlias = RetailCardGet
RetailCardGetResponse: TypeAlias = RetailCardRegosOffsettedArrayResult


_MODEL_NAMES = ['RetailCard', 'RetailCardAdd', 'RetailCardAddWithCustomer', 'RetailCardDelete', 'RetailCardEdit', 'RetailCardGet', 'RetailCardOperation', 'RetailCardOperationColumn', 'RetailCardOperationGet', 'RetailCardOperationRegosObjectResult', 'RetailCardOperationRegosOffsettedArrayResult', 'RetailCardRegosObjectResult', 'RetailCardRegosOffsettedArrayResult', 'RetailCard_SortOrder']


__all__ = [
    'RetailCard',
    'RetailCardAdd',
    'RetailCardAddWithCustomer',
    'RetailCardDelete',
    'RetailCardEdit',
    'RetailCardGet',
    'RetailCardOperation',
    'RetailCardOperationColumn',
    'RetailCardOperationColumns',
    'RetailCardOperationGet',
    'RetailCardOperationRegosObjectResult',
    'RetailCardOperationRegosOffsettedArrayResult',
    'RetailCardRegosObjectResult',
    'RetailCardRegosOffsettedArrayResult',
    'RetailCard_SortOrder',
    'RetailCard_SortOrderColumn',
    'RetailCardGetRequest',
    'RetailCardGetResponse',
    'RetailCardAddRequest',
    'RetailCardAddResponse',
    'RetailCardEditRequest',
    'RetailCardEditResponse',
    'RetailCardDeleteRequest',
    'RetailCardDeleteResponse',
    'RetailCardAddWithCustomerRequest',
    'RetailCardAddWithCustomerResponse',
    'RetailCardGetBalanceRequest',
    'RetailCardGetBalanceResponse',
    'RetailCardGetOperationsRequest',
    'RetailCardGetOperationsResponse',
    'RetailCardGetMigrationHistoryRequest',
    'RetailCardGetMigrationHistoryResponse'
]

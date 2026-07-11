"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocOrderDelivery(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    customer: RetailCustomer | None = PydField(default=None)
    card: RetailCard | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    status: DocumentStatus | None = PydField(default=None)
    delivery_date: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    external_code: str | None = PydField(default=None)
    from_: DeliveryFrom | None = PydField(default=None, alias="from")
    location: Location | None = PydField(default=None)
    delivery_type: DeliveryType | None = PydField(default=None)
    courier: DeliveryCourier | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    qrcodeurl: str | None = PydField(default=None)
    payment_type: PaymentType | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocOrderDeliveryActualize(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    data: list[DocOrderDeliveryActualizeData] | None = PydField(default=None)


class DocOrderDeliveryActualizeData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)


class DocOrderDeliveryAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    delivery_date: int | None = PydField(default=None)
    address: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    external_code: str | None = PydField(default=None)
    from_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    customer_id: int | None = PydField(default=None)
    card_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    delivery_type_id: int | None = PydField(default=None)
    payment_type_id: int | None = PydField(default=None)
    courier_id: int | None = PydField(default=None)
    location: Location | None = PydField(default=None)
    qrcodeurl: str | None = PydField(default=None)


class DocOrderDeliveryAddFull(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document: DocOrderDeliveryAdd | None = PydField(default=None)
    operations: list[OrderDeliveryOperationAdd] | None = PydField(default=None)


class DocOrderDeliveryColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocOrderDeliveryColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocOrderDeliveryColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_9 = 9


class DocOrderDeliveryDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderDeliveryDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderDeliveryEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    delivery_date: int | None = PydField(default=None)
    address: str | None = PydField(default=None)
    external_code: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    from_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    customer_id: int | None = PydField(default=None)
    card_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    delivery_type_id: int | None = PydField(default=None)
    payment_type_id: int | None = PydField(default=None)
    courier_id: int | None = PydField(default=None)
    location: Location | None = PydField(default=None)
    qrcodeurl: str | None = PydField(default=None)


class DocOrderDeliveryGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    status_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    customer_ids: list[int] | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)
    from_ids: list[int] | None = PydField(default=None)
    external_code: str | None = PydField(default=None)
    sort_orders: list[DocOrderDeliveryColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocOrderDeliveryLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocOrderDeliveryRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocOrderDelivery] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocOrderDeliveryReturnProcessing(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    data: list[DocOrderDeliveryReturnProcessingData] | None = PydField(default=None)


class DocOrderDeliveryReturnProcessingData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)


class DocOrderDeliverySetStock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)


class DocOrderDeliveryStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_31 = 31


class DocOrderDelivery_Beginning(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocOrderDelivery_SetCourier(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    courier_id: int | None = PydField(default=None)


class DocOrderDelivery_SetFiscalInfo(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    qrcodeurl: str | None = PydField(default=None)


class DocOrderDelivery_SetOperatingCash(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)


class DocOrderDelivery_SetRetailCard(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    card_id: int | None = PydField(default=None)


class DocOrderDelivery_SetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    status: DocOrderDeliveryStatusEnum | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, Int64RegosObjectResult, Location, UpdateResult
from schemas.api.docs.document_status import DocumentStatus
from schemas.api.docs.order_delivery_operation import OrderDeliveryOperationAdd
from schemas.api.references.delivery_courier import DeliveryCourier
from schemas.api.references.delivery_from import DeliveryFrom
from schemas.api.references.delivery_type import DeliveryType
from schemas.api.references.payment_type import PaymentType
from schemas.api.references.price_type import PriceType
from schemas.api.references.retail_card import RetailCard
from schemas.api.references.retail_customer import RetailCustomer
from schemas.api.references.stock import Stock


DocOrderDeliveryActualizeRequest: TypeAlias = DocOrderDeliveryActualize
DocOrderDeliveryActualizeResponse: TypeAlias = UpdateResult
DocOrderDeliveryAddFullRequest: TypeAlias = DocOrderDeliveryAddFull
DocOrderDeliveryAddFullResponse: TypeAlias = InsertResult
DocOrderDeliveryAddRequest: TypeAlias = DocOrderDeliveryAdd
DocOrderDeliveryAddResponse: TypeAlias = InsertResult
DocOrderDeliveryDeleteMarkRequest: TypeAlias = DocOrderDeliveryDeleteMark
DocOrderDeliveryDeleteMarkResponse: TypeAlias = UpdateResult
DocOrderDeliveryDeleteRequest: TypeAlias = DocOrderDeliveryDelete
DocOrderDeliveryDeleteResponse: TypeAlias = UpdateResult
DocOrderDeliveryEditRequest: TypeAlias = DocOrderDeliveryEdit
DocOrderDeliveryEditResponse: TypeAlias = UpdateResult
DocOrderDeliveryGetCountRequest: TypeAlias = DocOrderDeliveryGet
DocOrderDeliveryGetCountResponse: TypeAlias = Int64RegosObjectResult
DocOrderDeliveryGetRequest: TypeAlias = DocOrderDeliveryGet
DocOrderDeliveryGetResponse: TypeAlias = DocOrderDeliveryRegosOffsettedArrayResult
DocOrderDeliveryLockRequest: TypeAlias = DocOrderDeliveryLockAndUnlock
DocOrderDeliveryLockResponse: TypeAlias = UpdateResult
DocOrderDeliveryReturnRequest: TypeAlias = DocOrderDeliveryReturnProcessing
DocOrderDeliveryReturnResponse: TypeAlias = UpdateResult
DocOrderDeliverySetCourierRequest: TypeAlias = DocOrderDelivery_SetCourier
DocOrderDeliverySetCourierResponse: TypeAlias = UpdateResult
DocOrderDeliverySetFiscalInfoRequest: TypeAlias = DocOrderDelivery_SetFiscalInfo
DocOrderDeliverySetFiscalInfoResponse: TypeAlias = UpdateResult
DocOrderDeliverySetOperatingCashRequest: TypeAlias = DocOrderDelivery_SetOperatingCash
DocOrderDeliverySetOperatingCashResponse: TypeAlias = UpdateResult
DocOrderDeliverySetRetailCardRequest: TypeAlias = DocOrderDelivery_SetRetailCard
DocOrderDeliverySetRetailCardResponse: TypeAlias = UpdateResult
DocOrderDeliverySetStatusRequest: TypeAlias = DocOrderDelivery_SetStatus
DocOrderDeliverySetStatusResponse: TypeAlias = UpdateResult
DocOrderDeliverySetStockRequest: TypeAlias = DocOrderDeliverySetStock
DocOrderDeliverySetStockResponse: TypeAlias = UpdateResult
DocOrderDeliveryToBeginningRequest: TypeAlias = DocOrderDelivery_Beginning
DocOrderDeliveryToBeginningResponse: TypeAlias = UpdateResult
DocOrderDeliveryUnlockRequest: TypeAlias = DocOrderDeliveryLockAndUnlock
DocOrderDeliveryUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocOrderDelivery', 'DocOrderDeliveryActualize', 'DocOrderDeliveryActualizeData', 'DocOrderDeliveryAdd', 'DocOrderDeliveryAddFull', 'DocOrderDeliveryColumn', 'DocOrderDeliveryDelete', 'DocOrderDeliveryDeleteMark', 'DocOrderDeliveryEdit', 'DocOrderDeliveryGet', 'DocOrderDeliveryLockAndUnlock', 'DocOrderDeliveryRegosOffsettedArrayResult', 'DocOrderDeliveryReturnProcessing', 'DocOrderDeliveryReturnProcessingData', 'DocOrderDeliverySetStock', 'DocOrderDelivery_Beginning', 'DocOrderDelivery_SetCourier', 'DocOrderDelivery_SetFiscalInfo', 'DocOrderDelivery_SetOperatingCash', 'DocOrderDelivery_SetRetailCard', 'DocOrderDelivery_SetStatus']


__all__ = [
    'DocOrderDelivery',
    'DocOrderDeliveryActualize',
    'DocOrderDeliveryActualizeData',
    'DocOrderDeliveryAdd',
    'DocOrderDeliveryAddFull',
    'DocOrderDeliveryColumn',
    'DocOrderDeliveryColumns',
    'DocOrderDeliveryDelete',
    'DocOrderDeliveryDeleteMark',
    'DocOrderDeliveryEdit',
    'DocOrderDeliveryGet',
    'DocOrderDeliveryLockAndUnlock',
    'DocOrderDeliveryRegosOffsettedArrayResult',
    'DocOrderDeliveryReturnProcessing',
    'DocOrderDeliveryReturnProcessingData',
    'DocOrderDeliverySetStock',
    'DocOrderDeliveryStatusEnum',
    'DocOrderDelivery_Beginning',
    'DocOrderDelivery_SetCourier',
    'DocOrderDelivery_SetFiscalInfo',
    'DocOrderDelivery_SetOperatingCash',
    'DocOrderDelivery_SetRetailCard',
    'DocOrderDelivery_SetStatus',
    'DocOrderDeliveryGetRequest',
    'DocOrderDeliveryGetResponse',
    'DocOrderDeliveryGetCountRequest',
    'DocOrderDeliveryGetCountResponse',
    'DocOrderDeliveryAddRequest',
    'DocOrderDeliveryAddResponse',
    'DocOrderDeliveryAddFullRequest',
    'DocOrderDeliveryAddFullResponse',
    'DocOrderDeliveryEditRequest',
    'DocOrderDeliveryEditResponse',
    'DocOrderDeliveryDeleteMarkRequest',
    'DocOrderDeliveryDeleteMarkResponse',
    'DocOrderDeliveryDeleteRequest',
    'DocOrderDeliveryDeleteResponse',
    'DocOrderDeliveryLockRequest',
    'DocOrderDeliveryLockResponse',
    'DocOrderDeliveryUnlockRequest',
    'DocOrderDeliveryUnlockResponse',
    'DocOrderDeliverySetStatusRequest',
    'DocOrderDeliverySetStatusResponse',
    'DocOrderDeliverySetFiscalInfoRequest',
    'DocOrderDeliverySetFiscalInfoResponse',
    'DocOrderDeliveryToBeginningRequest',
    'DocOrderDeliveryToBeginningResponse',
    'DocOrderDeliverySetStockRequest',
    'DocOrderDeliverySetStockResponse',
    'DocOrderDeliverySetOperatingCashRequest',
    'DocOrderDeliverySetOperatingCashResponse',
    'DocOrderDeliverySetCourierRequest',
    'DocOrderDeliverySetCourierResponse',
    'DocOrderDeliverySetRetailCardRequest',
    'DocOrderDeliverySetRetailCardResponse',
    'DocOrderDeliveryReturnRequest',
    'DocOrderDeliveryReturnResponse',
    'DocOrderDeliveryActualizeRequest',
    'DocOrderDeliveryActualizeResponse'
]

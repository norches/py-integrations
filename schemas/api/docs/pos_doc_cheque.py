"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Cheque(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    status: SaleStatus | None = PydField(default=None)
    session_uuid: str | None = PydField(default=None)
    session_code: str | None = PydField(default=None)
    cashier: User | None = PydField(default=None)
    cashier_id: int | None = PydField(default=None)
    seller: User | None = PydField(default=None)
    seller_id: int | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    return_reason: RetailReturnReason | None = PydField(default=None)
    card_id: int | None = PydField(default=None)
    card: RetailCard | None = PydField(default=None)
    doc_order_delivery_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    amount2: _Decimal | None = PydField(default=None)
    payments_amount: _Decimal | None = PydField(default=None)
    card_discount_percent: _Decimal | None = PydField(default=None)
    debt_payment: bool | None = PydField(default=None)
    debt_uuid: str | None = PydField(default=None)
    refund_info: RefundInfo | None = PydField(default=None)


class ChequeArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Cheque] | Error | None = PydField(default=None)


class ChequeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    session_uuid: str | None = PydField(default=None)
    cashier_id: int | None = PydField(default=None)
    seller_id: int | None = PydField(default=None)
    card_id: int | None = PydField(default=None)
    doc_order_delivery_id: int | None = PydField(default=None)
    statuses: list[SaleStatus] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    return_reason: int | None = PydField(default=None)


class ChequePrint_RequestModel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_uuid: str | None = PydField(default=None)


class ChequePrint_ResponseModel(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    print_data: str | None = PydField(default=None)


class ChequePrint_ResponseModelRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: ChequePrint_ResponseModel | Error | None = PydField(default=None)


class ChequeRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Cheque | Error | None = PydField(default=None)


class ChequeTestPrintRequestModel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_id: int | None = PydField(default=None)


class ChequeUuid(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)


class Cheque_AddPayDebt(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    debt_uuid: str | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)


class Cheque_AddRetailCard(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    barcode_value: str | None = PydField(default=None)
    card_id: int | None = PydField(default=None)


class Cheque_SetAmountDiscount(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)


class Cheque_SetDocOrderDelivery(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    doc_order_delivery_id: int | None = PydField(default=None)


class Cheque_SetIsReturn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    return_reason_id: int | None = PydField(default=None)


class Cheque_SetPercentDiscount(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    percent: _Decimal | None = PydField(default=None)


class RefundInfo(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    terminal_id: str | None = PydField(default=None)
    receipt_no: str | None = PydField(default=None)
    datetime: _DateTime | None = PydField(default=None)
    fiscal_sign: str | None = PydField(default=None)
    qrcode_url: str | None = PydField(default=None)


class RemoveSeller(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)


class SaleStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class SetQrCodeUrl(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    qrcode_url: str | None = PydField(default=None)


class SetRefundInfo(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    terminal_id: str | None = PydField(default=None)
    receipt_no: str | None = PydField(default=None)
    datetime: _DateTime | None = PydField(default=None)
    fiscal_sign: str | None = PydField(default=None)
    qrcode_url: str | None = PydField(default=None)
    uuid: str | None = PydField(default=None)


class SetSeller(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    barcode: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, Insert_uuid_Result, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.retail_card import RetailCard
from schemas.api.references.retail_return_reason import RetailReturnReason


PosDocChequeAddRetailCardRequest: TypeAlias = Cheque_AddRetailCard
PosDocChequeAddRetailCardResponse: TypeAlias = ChequeArrayRegosObjectResult
PosDocChequeAddSellerRequest: TypeAlias = SetSeller
PosDocChequeAddSellerResponse: TypeAlias = UpdateResult
PosDocChequeBackToOperationsRequest: TypeAlias = ChequeUuid
PosDocChequeBackToOperationsResponse: TypeAlias = UpdateResult
PosDocChequeCancelRequest: TypeAlias = ChequeUuid
PosDocChequeCancelResponse: TypeAlias = UpdateResult
PosDocChequeCloseRequest: TypeAlias = ChequeUuid
PosDocChequeCloseResponse: TypeAlias = UpdateResult
PosDocChequeContinueDelayedRequest: TypeAlias = ChequeUuid
PosDocChequeContinueDelayedResponse: TypeAlias = UpdateResult
PosDocChequeCreateResponse: TypeAlias = Insert_uuid_Result
PosDocChequeDelayRequest: TypeAlias = ChequeUuid
PosDocChequeDelayResponse: TypeAlias = UpdateResult
PosDocChequeGetClosedResponse: TypeAlias = ChequeArrayRegosObjectResult
PosDocChequeGetPrintedRequest: TypeAlias = ChequePrint_RequestModel
PosDocChequeGetPrintedResponse: TypeAlias = ChequePrint_ResponseModelRegosObjectResult
PosDocChequeGetRequest: TypeAlias = ChequeGet
PosDocChequeGetResponse: TypeAlias = ChequeArrayRegosObjectResult
PosDocChequeGetTestPrintedRequest: TypeAlias = ChequeTestPrintRequestModel
PosDocChequeGetTestPrintedResponse: TypeAlias = ChequePrint_ResponseModelRegosObjectResult
PosDocChequeGetcurrentResponse: TypeAlias = ChequeArrayRegosObjectResult
PosDocChequePayDebtRequest: TypeAlias = Cheque_AddPayDebt
PosDocChequePayDebtResponse: TypeAlias = ChequeRegosObjectResult
PosDocChequePayRequest: TypeAlias = ChequeUuid
PosDocChequePayResponse: TypeAlias = UpdateResult
PosDocChequeRemoveSellerRequest: TypeAlias = RemoveSeller
PosDocChequeRemoveSellerResponse: TypeAlias = UpdateResult
PosDocChequeSetAmountDiscountRequest: TypeAlias = Cheque_SetAmountDiscount
PosDocChequeSetAmountDiscountResponse: TypeAlias = UpdateResult
PosDocChequeSetDocOrderDeliveryRequest: TypeAlias = Cheque_SetDocOrderDelivery
PosDocChequeSetDocOrderDeliveryResponse: TypeAlias = UpdateResult
PosDocChequeSetPercentDiscountRequest: TypeAlias = Cheque_SetPercentDiscount
PosDocChequeSetPercentDiscountResponse: TypeAlias = UpdateResult
PosDocChequeSetQrCodeUrlRequest: TypeAlias = SetQrCodeUrl
PosDocChequeSetQrCodeUrlResponse: TypeAlias = UpdateResult
PosDocChequeSetRefundInfoRequest: TypeAlias = SetRefundInfo
PosDocChequeSetRefundInfoResponse: TypeAlias = UpdateResult
PosDocChequeSetReturnRequest: TypeAlias = Cheque_SetIsReturn
PosDocChequeSetReturnResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Cheque', 'ChequeArrayRegosObjectResult', 'ChequeGet', 'ChequePrint_RequestModel', 'ChequePrint_ResponseModel', 'ChequePrint_ResponseModelRegosObjectResult', 'ChequeRegosObjectResult', 'ChequeTestPrintRequestModel', 'ChequeUuid', 'Cheque_AddPayDebt', 'Cheque_AddRetailCard', 'Cheque_SetAmountDiscount', 'Cheque_SetDocOrderDelivery', 'Cheque_SetIsReturn', 'Cheque_SetPercentDiscount', 'RefundInfo', 'RemoveSeller', 'SetQrCodeUrl', 'SetRefundInfo', 'SetSeller']


__all__ = [
    'Cheque',
    'ChequeArrayRegosObjectResult',
    'ChequeGet',
    'ChequePrint_RequestModel',
    'ChequePrint_ResponseModel',
    'ChequePrint_ResponseModelRegosObjectResult',
    'ChequeRegosObjectResult',
    'ChequeTestPrintRequestModel',
    'ChequeUuid',
    'Cheque_AddPayDebt',
    'Cheque_AddRetailCard',
    'Cheque_SetAmountDiscount',
    'Cheque_SetDocOrderDelivery',
    'Cheque_SetIsReturn',
    'Cheque_SetPercentDiscount',
    'RefundInfo',
    'RemoveSeller',
    'SaleStatus',
    'SetQrCodeUrl',
    'SetRefundInfo',
    'SetSeller',
    'PosDocChequeGetRequest',
    'PosDocChequeGetResponse',
    'PosDocChequeGetcurrentResponse',
    'PosDocChequeGetClosedResponse',
    'PosDocChequeCreateResponse',
    'PosDocChequeSetRefundInfoRequest',
    'PosDocChequeSetRefundInfoResponse',
    'PosDocChequeSetQrCodeUrlRequest',
    'PosDocChequeSetQrCodeUrlResponse',
    'PosDocChequeAddSellerRequest',
    'PosDocChequeAddSellerResponse',
    'PosDocChequeRemoveSellerRequest',
    'PosDocChequeRemoveSellerResponse',
    'PosDocChequePayRequest',
    'PosDocChequePayResponse',
    'PosDocChequeCloseRequest',
    'PosDocChequeCloseResponse',
    'PosDocChequeDelayRequest',
    'PosDocChequeDelayResponse',
    'PosDocChequeContinueDelayedRequest',
    'PosDocChequeContinueDelayedResponse',
    'PosDocChequeCancelRequest',
    'PosDocChequeCancelResponse',
    'PosDocChequeBackToOperationsRequest',
    'PosDocChequeBackToOperationsResponse',
    'PosDocChequeSetPercentDiscountRequest',
    'PosDocChequeSetPercentDiscountResponse',
    'PosDocChequeSetAmountDiscountRequest',
    'PosDocChequeSetAmountDiscountResponse',
    'PosDocChequeAddRetailCardRequest',
    'PosDocChequeAddRetailCardResponse',
    'PosDocChequeSetReturnRequest',
    'PosDocChequeSetReturnResponse',
    'PosDocChequeSetDocOrderDeliveryRequest',
    'PosDocChequeSetDocOrderDeliveryResponse',
    'PosDocChequeGetPrintedRequest',
    'PosDocChequeGetPrintedResponse',
    'PosDocChequeGetTestPrintedRequest',
    'PosDocChequeGetTestPrintedResponse',
    'PosDocChequePayDebtRequest',
    'PosDocChequePayDebtResponse'
]

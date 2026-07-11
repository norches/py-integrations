"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocRetailPayment(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    has_storno: bool | None = PydField(default=None)
    storno_uuid: str | None = PydField(default=None)
    document: str | None = PydField(default=None)
    order: int | None = PydField(default=None)
    type: PaymentType | None = PydField(default=None)
    payment_type: PaymentType | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    has_change: bool | None = PydField(default=None)
    change_uuid: str | None = PydField(default=None)


class DocRetailPaymentGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    doc_sale_uuid: str | None = PydField(default=None)
    uuids: list[str] | None = PydField(default=None)


class DocRetailPaymentRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocRetailPayment] | Error | None = PydField(default=None)


class Payment(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    has_storno: bool | None = PydField(default=None)
    storno_uuid: str | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    order: int | None = PydField(default=None)
    type: PaymentType | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    payment_id: str | None = PydField(default=None)
    has_change: bool | None = PydField(default=None)
    change_uuid: str | None = PydField(default=None)


class PaymentAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_uuid: str | None = PydField(default=None)
    type_id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    data: str | None = PydField(default=None)


class PaymentArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Payment] | Error | None = PydField(default=None)


class PaymentGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuids: list[str] | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    payment_type_ids: list[int] | None = PydField(default=None)
    exclude_storno: bool | None = PydField(default=None)


class PaymentStorno(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)


class PosPaymentSystemGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_uuid: str | None = PydField(default=None)
    payment_type_id: int | None = PydField(default=None)


class PosPaymentSystemID(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    payment_system_id: int | None = PydField(default=None)


class PosPaymentSystemIDRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: PosPaymentSystemID | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, Insert_uuid_Result
from schemas.api.references.payment_type import PaymentType


ChequePaymentOperationAddRequest: TypeAlias = PaymentAdd
ChequePaymentOperationAddResponse: TypeAlias = Insert_uuid_Result
ChequePaymentOperationGetPaymentSystemIdRequest: TypeAlias = PosPaymentSystemGet
ChequePaymentOperationGetPaymentSystemIdResponse: TypeAlias = PosPaymentSystemIDRegosObjectResult
ChequePaymentOperationGetRequest: TypeAlias = DocRetailPaymentGet
ChequePaymentOperationGetResponse: TypeAlias = DocRetailPaymentRegosArrayResult
ChequePaymentOperationPosGetRequest: TypeAlias = PaymentGet
ChequePaymentOperationPosGetResponse: TypeAlias = PaymentArrayRegosObjectResult
ChequePaymentOperationStornoRequest: TypeAlias = PaymentStorno
ChequePaymentOperationStornoResponse: TypeAlias = Insert_uuid_Result


_MODEL_NAMES = ['DocRetailPayment', 'DocRetailPaymentGet', 'DocRetailPaymentRegosArrayResult', 'Payment', 'PaymentAdd', 'PaymentArrayRegosObjectResult', 'PaymentGet', 'PaymentStorno', 'PosPaymentSystemGet', 'PosPaymentSystemID', 'PosPaymentSystemIDRegosObjectResult']


__all__ = [
    'DocRetailPayment',
    'DocRetailPaymentGet',
    'DocRetailPaymentRegosArrayResult',
    'Payment',
    'PaymentAdd',
    'PaymentArrayRegosObjectResult',
    'PaymentGet',
    'PaymentStorno',
    'PosPaymentSystemGet',
    'PosPaymentSystemID',
    'PosPaymentSystemIDRegosObjectResult',
    'ChequePaymentOperationPosGetRequest',
    'ChequePaymentOperationPosGetResponse',
    'ChequePaymentOperationAddRequest',
    'ChequePaymentOperationAddResponse',
    'ChequePaymentOperationStornoRequest',
    'ChequePaymentOperationStornoResponse',
    'ChequePaymentOperationGetPaymentSystemIdRequest',
    'ChequePaymentOperationGetPaymentSystemIdResponse',
    'ChequePaymentOperationGetRequest',
    'ChequePaymentOperationGetResponse'
]

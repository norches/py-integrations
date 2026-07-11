"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PromoBonusCancelPayment(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)


class PromoBonusCreateEnrollment(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    card_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)


class PromoBonusCreateManualOperation(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    card_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    exp_date: int | None = PydField(default=None)


class PromoBonusCreatePayment(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    card_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    document_uuid: str | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)


class PromoBonusGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)


class PromoBonusPerformEnrollment(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)


class PromoBonusPerformPayment(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    uuid: str | None = PydField(default=None)


class PromoBonusType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class PromoBonusesRemainder(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    value: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PromoBonusesRemainderGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    card_id: int | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)


class PromoBonusesRemainderRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: PromoBonusesRemainder | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, Insert_uuid_Result, UpdateResult
from schemas.api.references.retail_card import RetailCardOperationRegosObjectResult


PromoBonusCancelPaymentRequest: TypeAlias = PromoBonusCancelPayment
PromoBonusCancelPaymentResponse: TypeAlias = UpdateResult
PromoBonusCreateEnrollmentRequest: TypeAlias = PromoBonusCreateEnrollment
PromoBonusCreateEnrollmentResponse: TypeAlias = Insert_uuid_Result
PromoBonusCreateManualIncomeOperationRequest: TypeAlias = PromoBonusCreateManualOperation
PromoBonusCreateManualIncomeOperationResponse: TypeAlias = UpdateResult
PromoBonusCreateManualOutcomeOperationRequest: TypeAlias = PromoBonusCreateManualOperation
PromoBonusCreateManualOutcomeOperationResponse: TypeAlias = UpdateResult
PromoBonusCreatePaymentRequest: TypeAlias = PromoBonusCreatePayment
PromoBonusCreatePaymentResponse: TypeAlias = Insert_uuid_Result
PromoBonusGetRequest: TypeAlias = PromoBonusGet
PromoBonusGetResponse: TypeAlias = RetailCardOperationRegosObjectResult
PromoBonusPerformEnrollmentRequest: TypeAlias = PromoBonusPerformEnrollment
PromoBonusPerformEnrollmentResponse: TypeAlias = UpdateResult
PromoBonusPerformPaymentRequest: TypeAlias = PromoBonusPerformPayment
PromoBonusPerformPaymentResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['PromoBonusCancelPayment', 'PromoBonusCreateEnrollment', 'PromoBonusCreateManualOperation', 'PromoBonusCreatePayment', 'PromoBonusGet', 'PromoBonusPerformEnrollment', 'PromoBonusPerformPayment', 'PromoBonusesRemainder', 'PromoBonusesRemainderGet', 'PromoBonusesRemainderRegosObjectResult']


__all__ = [
    'PromoBonusCancelPayment',
    'PromoBonusCreateEnrollment',
    'PromoBonusCreateManualOperation',
    'PromoBonusCreatePayment',
    'PromoBonusGet',
    'PromoBonusPerformEnrollment',
    'PromoBonusPerformPayment',
    'PromoBonusType',
    'PromoBonusesRemainder',
    'PromoBonusesRemainderGet',
    'PromoBonusesRemainderRegosObjectResult',
    'PromoBonusCreatePaymentRequest',
    'PromoBonusCreatePaymentResponse',
    'PromoBonusPerformPaymentRequest',
    'PromoBonusPerformPaymentResponse',
    'PromoBonusCreateEnrollmentRequest',
    'PromoBonusCreateEnrollmentResponse',
    'PromoBonusPerformEnrollmentRequest',
    'PromoBonusPerformEnrollmentResponse',
    'PromoBonusCancelPaymentRequest',
    'PromoBonusCancelPaymentResponse',
    'PromoBonusCreateManualIncomeOperationRequest',
    'PromoBonusCreateManualIncomeOperationResponse',
    'PromoBonusCreateManualOutcomeOperationRequest',
    'PromoBonusCreateManualOutcomeOperationResponse',
    'PromoBonusGetRequest',
    'PromoBonusGetResponse'
]

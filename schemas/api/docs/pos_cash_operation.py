"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RegosOnlineCashAmountDetailsGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)


class RegosOnlineCashOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    payment_type_id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


class RegosOnlineCashOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RegosOnlineCashOperationPaymentAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    payment_type_id: int | None = PydField(default=None)
    category_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CashAmountDetailsRegosObjectResult, InsertResult
from schemas.api.docs.cash_operation import CashOperationRegosOffsettedArrayResult


PosCashOperationGetAmountDetailsRequest: TypeAlias = RegosOnlineCashAmountDetailsGet
PosCashOperationGetAmountDetailsResponse: TypeAlias = CashAmountDetailsRegosObjectResult
PosCashOperationGetRequest: TypeAlias = RegosOnlineCashOperationGet
PosCashOperationGetResponse: TypeAlias = CashOperationRegosOffsettedArrayResult
PosCashOperationIncomeAddRequest: TypeAlias = RegosOnlineCashOperationAdd
PosCashOperationIncomeAddResponse: TypeAlias = InsertResult
PosCashOperationOutcomeAddRequest: TypeAlias = RegosOnlineCashOperationAdd
PosCashOperationOutcomeAddResponse: TypeAlias = InsertResult
PosCashOperationPaymentAddRequest: TypeAlias = RegosOnlineCashOperationPaymentAdd
PosCashOperationPaymentAddResponse: TypeAlias = InsertResult


_MODEL_NAMES = ['RegosOnlineCashAmountDetailsGet', 'RegosOnlineCashOperationAdd', 'RegosOnlineCashOperationGet', 'RegosOnlineCashOperationPaymentAdd']


__all__ = [
    'RegosOnlineCashAmountDetailsGet',
    'RegosOnlineCashOperationAdd',
    'RegosOnlineCashOperationGet',
    'RegosOnlineCashOperationPaymentAdd',
    'PosCashOperationGetRequest',
    'PosCashOperationGetResponse',
    'PosCashOperationGetAmountDetailsRequest',
    'PosCashOperationGetAmountDetailsResponse',
    'PosCashOperationIncomeAddRequest',
    'PosCashOperationIncomeAddResponse',
    'PosCashOperationOutcomeAddRequest',
    'PosCashOperationOutcomeAddResponse',
    'PosCashOperationPaymentAddRequest',
    'PosCashOperationPaymentAddResponse'
]

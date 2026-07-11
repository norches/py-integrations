"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Session(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: str | None = PydField(default=None)
    user: User | None = PydField(default=None)
    ip: str | None = PydField(default=None)
    device_name: str | None = PydField(default=None)
    start_time: int | None = PydField(default=None)
    duration: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class SessionCashOprPaymentAmount(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    opr_sale: _Decimal | None = PydField(default=None)
    opr_return: _Decimal | None = PydField(default=None)
    opr_cash_in: _Decimal | None = PydField(default=None)
    opr_cash_out: _Decimal | None = PydField(default=None)
    opr_change_out: _Decimal | None = PydField(default=None)
    opr_change_in: _Decimal | None = PydField(default=None)
    opr_payment_out: _Decimal | None = PydField(default=None)


class SessionGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[str] | None = PydField(default=None)


class SessionPaymentSale(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    amount: _Decimal | None = PydField(default=None)
    payment_type: PaymentType | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)


class SessionRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Session] | Error | None = PydField(default=None)


class SessionSaleDetails(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    position_counter: int | None = PydField(default=None)
    units_counter: _Decimal | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.rbac.user import User
from schemas.api.references.payment_type import PaymentType


SessionGetRequest: TypeAlias = SessionGet
SessionGetResponse: TypeAlias = SessionRegosArrayResult


_MODEL_NAMES = ['Session', 'SessionCashOprPaymentAmount', 'SessionGet', 'SessionPaymentSale', 'SessionRegosArrayResult', 'SessionSaleDetails']


__all__ = [
    'Session',
    'SessionCashOprPaymentAmount',
    'SessionGet',
    'SessionPaymentSale',
    'SessionRegosArrayResult',
    'SessionSaleDetails',
    'SessionGetRequest',
    'SessionGetResponse'
]

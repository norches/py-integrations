"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocAdditionalExpenses(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    parent_document: DocShort | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    contract: DocContractShort | None = PydField(default=None)
    description: str | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocAdditionalExpensesAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    parent_doc_type_id: int | None = PydField(default=None)
    parent_doc_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)


class DocAdditionalExpensesEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)


class DocAdditionalExpensesGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    parent_doc_type_id: int | None = PydField(default=None)
    parent_doc_id: int | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocAdditionalExpensesRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocAdditionalExpenses] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocShort(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    doc_type: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseLockAndUnlock, BaseSortColumn, Base_ID, Error, InsertResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.references.currency import Currency
from schemas.api.references.partner import Partner
from schemas.api.references.stock import Stock


DocAdditionalExpensesAddRequest: TypeAlias = DocAdditionalExpensesAdd
DocAdditionalExpensesAddResponse: TypeAlias = InsertResult
DocAdditionalExpensesDeleteMarkRequest: TypeAlias = Base_ID
DocAdditionalExpensesDeleteMarkResponse: TypeAlias = UpdateResult
DocAdditionalExpensesDeleteRequest: TypeAlias = Base_ID
DocAdditionalExpensesDeleteResponse: TypeAlias = UpdateResult
DocAdditionalExpensesEditRequest: TypeAlias = DocAdditionalExpensesEdit
DocAdditionalExpensesEditResponse: TypeAlias = UpdateResult
DocAdditionalExpensesGetRequest: TypeAlias = DocAdditionalExpensesGet
DocAdditionalExpensesGetResponse: TypeAlias = DocAdditionalExpensesRegosOffsettedArrayResult
DocAdditionalExpensesLockRequest: TypeAlias = BaseLockAndUnlock
DocAdditionalExpensesLockResponse: TypeAlias = UpdateResult
DocAdditionalExpensesPerformCancelRequest: TypeAlias = Base_ID
DocAdditionalExpensesPerformCancelResponse: TypeAlias = UpdateResult
DocAdditionalExpensesPerformRequest: TypeAlias = Base_ID
DocAdditionalExpensesPerformResponse: TypeAlias = UpdateResult
DocAdditionalExpensesUnlockRequest: TypeAlias = BaseLockAndUnlock
DocAdditionalExpensesUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocAdditionalExpenses', 'DocAdditionalExpensesAdd', 'DocAdditionalExpensesEdit', 'DocAdditionalExpensesGet', 'DocAdditionalExpensesRegosOffsettedArrayResult', 'DocShort']


__all__ = [
    'DocAdditionalExpenses',
    'DocAdditionalExpensesAdd',
    'DocAdditionalExpensesEdit',
    'DocAdditionalExpensesGet',
    'DocAdditionalExpensesRegosOffsettedArrayResult',
    'DocShort',
    'DocAdditionalExpensesGetRequest',
    'DocAdditionalExpensesGetResponse',
    'DocAdditionalExpensesAddRequest',
    'DocAdditionalExpensesAddResponse',
    'DocAdditionalExpensesEditRequest',
    'DocAdditionalExpensesEditResponse',
    'DocAdditionalExpensesDeleteMarkRequest',
    'DocAdditionalExpensesDeleteMarkResponse',
    'DocAdditionalExpensesDeleteRequest',
    'DocAdditionalExpensesDeleteResponse',
    'DocAdditionalExpensesLockRequest',
    'DocAdditionalExpensesLockResponse',
    'DocAdditionalExpensesUnlockRequest',
    'DocAdditionalExpensesUnlockResponse',
    'DocAdditionalExpensesPerformRequest',
    'DocAdditionalExpensesPerformResponse',
    'DocAdditionalExpensesPerformCancelRequest',
    'DocAdditionalExpensesPerformCancelResponse'
]

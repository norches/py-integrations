"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocAdditionalExpensesOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocAdditionalExpensesOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    item_id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)


class DocAdditionalExpensesOperationEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    cost: _Decimal | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)


class DocAdditionalExpensesOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    item_ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocAdditionalExpensesOperationRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocAdditionalExpensesOperation] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, Error, UpdateResult, VatCalculationTypeEnum
from schemas.api.references.item import Item


DocAdditionalExpensesOperationAddRequest: TypeAlias = list[DocAdditionalExpensesOperationAdd]
DocAdditionalExpensesOperationAddResponse: TypeAlias = UpdateResult
DocAdditionalExpensesOperationDeleteRequest: TypeAlias = list[Base_ID]
DocAdditionalExpensesOperationDeleteResponse: TypeAlias = UpdateResult
DocAdditionalExpensesOperationEditRequest: TypeAlias = list[DocAdditionalExpensesOperationEdit]
DocAdditionalExpensesOperationEditResponse: TypeAlias = UpdateResult
DocAdditionalExpensesOperationGetRequest: TypeAlias = DocAdditionalExpensesOperationGet
DocAdditionalExpensesOperationGetResponse: TypeAlias = DocAdditionalExpensesOperationRegosOffsettedArrayResult


_MODEL_NAMES = ['DocAdditionalExpensesOperation', 'DocAdditionalExpensesOperationAdd', 'DocAdditionalExpensesOperationEdit', 'DocAdditionalExpensesOperationGet', 'DocAdditionalExpensesOperationRegosOffsettedArrayResult']


__all__ = [
    'DocAdditionalExpensesOperation',
    'DocAdditionalExpensesOperationAdd',
    'DocAdditionalExpensesOperationEdit',
    'DocAdditionalExpensesOperationGet',
    'DocAdditionalExpensesOperationRegosOffsettedArrayResult',
    'DocAdditionalExpensesOperationGetRequest',
    'DocAdditionalExpensesOperationGetResponse',
    'DocAdditionalExpensesOperationAddRequest',
    'DocAdditionalExpensesOperationAddResponse',
    'DocAdditionalExpensesOperationEditRequest',
    'DocAdditionalExpensesOperationEditResponse',
    'DocAdditionalExpensesOperationDeleteRequest',
    'DocAdditionalExpensesOperationDeleteResponse'
]

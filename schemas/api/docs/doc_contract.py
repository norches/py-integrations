"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocContract(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    direction: ContractDirection | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    details: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocContractAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    direction: ContractDirection | None = PydField(default=None)
    name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    details: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class DocContractColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocContractColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocContractColumns(IntEnum):
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


class DocContractDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocContractDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocContractEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    direction: ContractDirection | None = PydField(default=None)
    name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    details: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocContractGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    direction: ContractDirection | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[DocContractColumn] | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocContractRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocContract] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocContractShort(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    partner_name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    direction: ContractDirection | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    details: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocContractShortRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocContractShort] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, ContractDirection, Error, InsertResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.firm import Firm
from schemas.api.references.partner import Partner


ContractDirection: TypeAlias = ContractDirection
DocContractAddRequest: TypeAlias = DocContractAdd
DocContractAddResponse: TypeAlias = InsertResult
DocContractDeleteMarkRequest: TypeAlias = DocContractDeleteMark
DocContractDeleteMarkResponse: TypeAlias = UpdateResult
DocContractDeleteRequest: TypeAlias = DocContractDelete
DocContractDeleteResponse: TypeAlias = UpdateResult
DocContractEditRequest: TypeAlias = DocContractEdit
DocContractEditResponse: TypeAlias = UpdateResult
DocContractGetRequest: TypeAlias = DocContractGet
DocContractGetResponse: TypeAlias = DocContractRegosOffsettedArrayResult
DocContractGetShortRequest: TypeAlias = DocContractGet
DocContractGetShortResponse: TypeAlias = DocContractShortRegosOffsettedArrayResult


_MODEL_NAMES = ['DocContract', 'DocContractAdd', 'DocContractColumn', 'DocContractDelete', 'DocContractDeleteMark', 'DocContractEdit', 'DocContractGet', 'DocContractRegosOffsettedArrayResult', 'DocContractShort', 'DocContractShortRegosOffsettedArrayResult']


__all__ = [
    'DocContract',
    'DocContractAdd',
    'DocContractColumn',
    'DocContractColumns',
    'DocContractDelete',
    'DocContractDeleteMark',
    'DocContractEdit',
    'DocContractGet',
    'DocContractRegosOffsettedArrayResult',
    'DocContractShort',
    'DocContractShortRegosOffsettedArrayResult',
    'DocContractGetRequest',
    'DocContractGetResponse',
    'DocContractGetShortRequest',
    'DocContractGetShortResponse',
    'DocContractAddRequest',
    'DocContractAddResponse',
    'DocContractEditRequest',
    'DocContractEditResponse',
    'DocContractDeleteMarkRequest',
    'DocContractDeleteMarkResponse',
    'DocContractDeleteRequest',
    'DocContractDeleteResponse',
    'ContractDirection'
]

"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Partner(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    legal_status: LegalStatus | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    boss_name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    inn: str | None = PydField(default=None)
    bank_name: str | None = PydField(default=None)
    mfo: str | None = PydField(default=None)
    rs: str | None = PydField(default=None)
    oked: str | None = PydField(default=None)
    vat_index: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group: PartnerGroup | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PartnerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    legal_status: LegalStatus | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    boss_name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    inn: str | None = PydField(default=None)
    bank_name: str | None = PydField(default=None)
    mfo: str | None = PydField(default=None)
    rs: str | None = PydField(default=None)
    oked: str | None = PydField(default=None)
    vat_index: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class PartnerCurrentBalanceGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class PartnerDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PartnerDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PartnerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    legal_status: LegalStatus | None = PydField(default=None)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    boss_name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    inn: str | None = PydField(default=None)
    bank_name: str | None = PydField(default=None)
    mfo: str | None = PydField(default=None)
    rs: str | None = PydField(default=None)
    oked: str | None = PydField(default=None)
    vat_index: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class PartnerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    legal_status: LegalStatus | None = PydField(default=None)
    sort_orders: list[PartnerSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class PartnerRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Partner] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class PartnerSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: PartnerSortOrderColumnsEnum | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class PartnerSortOrderColumnsEnum(IntEnum):
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
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, DecimalRegosObjectResult, Error, InsertResult, LegalStatus, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit
from schemas.api.references.partner_group import PartnerGroup


LegalStatus: TypeAlias = LegalStatus
PartnerAddRequest: TypeAlias = PartnerAdd
PartnerAddResponse: TypeAlias = InsertResult
PartnerDeleteMarkRequest: TypeAlias = PartnerDeleteMark
PartnerDeleteMarkResponse: TypeAlias = UpdateResult
PartnerDeleteRequest: TypeAlias = PartnerDelete
PartnerDeleteResponse: TypeAlias = UpdateResult
PartnerEditRequest: TypeAlias = PartnerEdit
PartnerEditResponse: TypeAlias = UpdateResult
PartnerGetCurrentBalanceRequest: TypeAlias = PartnerCurrentBalanceGet
PartnerGetCurrentBalanceResponse: TypeAlias = DecimalRegosObjectResult
PartnerGetRequest: TypeAlias = PartnerGet
PartnerGetResponse: TypeAlias = PartnerRegosOffsettedArrayResult


_MODEL_NAMES = ['Partner', 'PartnerAdd', 'PartnerCurrentBalanceGet', 'PartnerDelete', 'PartnerDeleteMark', 'PartnerEdit', 'PartnerGet', 'PartnerRegosOffsettedArrayResult', 'PartnerSortOrder']


__all__ = [
    'Partner',
    'PartnerAdd',
    'PartnerCurrentBalanceGet',
    'PartnerDelete',
    'PartnerDeleteMark',
    'PartnerEdit',
    'PartnerGet',
    'PartnerRegosOffsettedArrayResult',
    'PartnerSortOrder',
    'PartnerSortOrderColumnsEnum',
    'PartnerGetRequest',
    'PartnerGetResponse',
    'PartnerAddRequest',
    'PartnerAddResponse',
    'PartnerEditRequest',
    'PartnerEditResponse',
    'PartnerDeleteMarkRequest',
    'PartnerDeleteMarkResponse',
    'PartnerDeleteRequest',
    'PartnerDeleteResponse',
    'PartnerGetCurrentBalanceRequest',
    'PartnerGetCurrentBalanceResponse',
    'LegalStatus'
]

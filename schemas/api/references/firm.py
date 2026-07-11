"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Firm(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    boss_name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    inn: str | None = PydField(default=None)
    bank_name: str | None = PydField(default=None)
    mfo: str | None = PydField(default=None)
    rs: str | None = PydField(default=None)
    oked: str | None = PydField(default=None)
    vat_index: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group: FirmGroup | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class FirmAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    boss_name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    inn: str | None = PydField(default=None)
    bank_name: str | None = PydField(default=None)
    mfo: str | None = PydField(default=None)
    rs: str | None = PydField(default=None)
    oked: str | None = PydField(default=None)
    vat_index: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)


class FirmDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class FirmDeleteConfirm(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    confirm_code: str | None = PydField(default=None)


class FirmDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class FirmEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    fullname: str | None = PydField(default=None)
    boss_name: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    inn: str | None = PydField(default=None)
    bank_name: str | None = PydField(default=None)
    mfo: str | None = PydField(default=None)
    rs: str | None = PydField(default=None)
    oked: str | None = PydField(default=None)
    vat_index: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)


class FirmGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    sort_orders: list[FirmSortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class FirmImage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    size: int | None = PydField(default=None)
    file: str | None = PydField(default=None)
    url: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class FirmImageDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class FirmImageGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)
    compress_data: bool | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class FirmImageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[FirmImage] | Error | None = PydField(default=None)


class FirmRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Firm] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class FirmSetting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    dataType: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class FirmSettingArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[FirmSetting] | Error | None = PydField(default=None)


class FirmSortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: FirmSortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class FirmSortOrderColumn(IntEnum):
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


class Firm_SettingEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)


class Firm_SettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    firm_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ApiResult, ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.firm_group import FirmGroup


FirmAddImageResponse: TypeAlias = UpdateResult
FirmAddRequest: TypeAlias = FirmAdd
FirmAddResponse: TypeAlias = InsertResult
FirmDeleteConfirmRequest: TypeAlias = FirmDeleteConfirm
FirmDeleteConfirmResponse: TypeAlias = ApiResult
FirmDeleteImageRequest: TypeAlias = FirmImageDelete
FirmDeleteImageResponse: TypeAlias = UpdateResult
FirmDeleteMarkRequest: TypeAlias = FirmDeleteMark
FirmDeleteMarkResponse: TypeAlias = UpdateResult
FirmDeleteRequest: TypeAlias = FirmDelete
FirmDeleteResponse: TypeAlias = ApiResult
FirmEditRequest: TypeAlias = FirmEdit
FirmEditResponse: TypeAlias = UpdateResult
FirmEditSettingsRequest: TypeAlias = list[Firm_SettingEdit]
FirmEditSettingsResponse: TypeAlias = UpdateResult
FirmGetImageRequest: TypeAlias = FirmImageGet
FirmGetImageResponse: TypeAlias = FirmImageRegosArrayResult
FirmGetRequest: TypeAlias = FirmGet
FirmGetResponse: TypeAlias = FirmRegosOffsettedArrayResult
FirmGetSettingsRequest: TypeAlias = Firm_SettingGet
FirmGetSettingsResponse: TypeAlias = FirmSettingArrayRegosObjectResult


_MODEL_NAMES = ['Firm', 'FirmAdd', 'FirmDelete', 'FirmDeleteConfirm', 'FirmDeleteMark', 'FirmEdit', 'FirmGet', 'FirmImage', 'FirmImageDelete', 'FirmImageGet', 'FirmImageRegosArrayResult', 'FirmRegosOffsettedArrayResult', 'FirmSetting', 'FirmSettingArrayRegosObjectResult', 'FirmSortOrder', 'Firm_SettingEdit', 'Firm_SettingGet']


__all__ = [
    'Firm',
    'FirmAdd',
    'FirmDelete',
    'FirmDeleteConfirm',
    'FirmDeleteMark',
    'FirmEdit',
    'FirmGet',
    'FirmImage',
    'FirmImageDelete',
    'FirmImageGet',
    'FirmImageRegosArrayResult',
    'FirmRegosOffsettedArrayResult',
    'FirmSetting',
    'FirmSettingArrayRegosObjectResult',
    'FirmSortOrder',
    'FirmSortOrderColumn',
    'Firm_SettingEdit',
    'Firm_SettingGet',
    'FirmGetRequest',
    'FirmGetResponse',
    'FirmAddRequest',
    'FirmAddResponse',
    'FirmEditRequest',
    'FirmEditResponse',
    'FirmDeleteMarkRequest',
    'FirmDeleteMarkResponse',
    'FirmDeleteRequest',
    'FirmDeleteResponse',
    'FirmDeleteConfirmRequest',
    'FirmDeleteConfirmResponse',
    'FirmGetImageRequest',
    'FirmGetImageResponse',
    'FirmAddImageResponse',
    'FirmDeleteImageRequest',
    'FirmDeleteImageResponse',
    'FirmGetSettingsRequest',
    'FirmGetSettingsResponse',
    'FirmEditSettingsRequest',
    'FirmEditSettingsResponse'
]

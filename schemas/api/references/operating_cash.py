"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class OperatingCash(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    stock: Stock | None = PydField(default=None)
    key: str | None = PydField(default=None)
    price_type: PriceType | None = PydField(default=None)
    description: str | None = PydField(default=None)
    virtual_: bool | None = PydField(default=None)
    auto_close: bool | None = PydField(default=None)
    max_cheque_quantity_in_session: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    userAccept: User | None = PydField(default=None)


class OperatingCashAccept(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_id: int | None = PydField(default=None)


class OperatingCashAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    stock_id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    virtual_: bool | None = PydField(default=None)
    auto_close: bool | None = PydField(default=None)
    max_cheque_quantity_in_session: int | None = PydField(default=None)


class OperatingCashChequeTemplate(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    type_id: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)
    template: str | None = PydField(default=None)
    logo: int | None = PydField(default=None)
    logo_width: int | None = PydField(default=None)
    logo_height: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class OperatingCashChequeTemplateEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    logo: int | None = PydField(default=None)
    logo_width: int | None = PydField(default=None)
    logo_height: int | None = PydField(default=None)
    template: str | None = PydField(default=None)


class OperatingCashChequeTemplateGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    operating_cash_ids: list[int] | None = PydField(default=None)
    cheque_type_ids: list[int] | None = PydField(default=None)


class OperatingCashChequeTemplateRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[OperatingCashChequeTemplate] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class OperatingCashDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class OperatingCashDiscard(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class OperatingCashEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    auto_close: bool | None = PydField(default=None)
    max_cheque_quantity_in_session: int | None = PydField(default=None)


class OperatingCashGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    price_type_ids: list[int] | None = PydField(default=None)
    is_virtual: bool | None = PydField(default=None)
    accepted_user_id: int | None = PydField(default=None)
    sort_orders: list[OperatingCash_SortOrder] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class OperatingCashImage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    size: int | None = PydField(default=None)
    file: str | None = PydField(default=None)
    url: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)


class OperatingCashImageDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class OperatingCashImageGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)
    compress_data: bool | None = PydField(default=None)
    operating_cash_id: int | None = PydField(default=None)


class OperatingCashImageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[OperatingCashImage] | Error | None = PydField(default=None)


class OperatingCashRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[OperatingCash] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class OperatingCash_Setting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    key: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    value: str | None = PydField(default=None)


class OperatingCash_SettingArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[OperatingCash_Setting] | Error | None = PydField(default=None)


class OperatingCash_SettingEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    value: str | None = PydField(default=None)


class OperatingCash_SettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_id: int | None = PydField(default=None)


class OperatingCash_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: OperatingCash_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class OperatingCash_SortOrderColumn(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, ObjectRegosObjectResult, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.references.price_type import PriceType
from schemas.api.references.stock import Stock


OperatingCashAcceptRequest: TypeAlias = OperatingCashAccept
OperatingCashAcceptResponse: TypeAlias = ObjectRegosObjectResult
OperatingCashAddImageResponse: TypeAlias = UpdateResult
OperatingCashAddRequest: TypeAlias = OperatingCashAdd
OperatingCashAddResponse: TypeAlias = InsertResult
OperatingCashDeleteImageRequest: TypeAlias = OperatingCashImageDelete
OperatingCashDeleteImageResponse: TypeAlias = UpdateResult
OperatingCashDeleteRequest: TypeAlias = OperatingCashDelete
OperatingCashDeleteResponse: TypeAlias = UpdateResult
OperatingCashDiscardRequest: TypeAlias = OperatingCashDiscard
OperatingCashDiscardResponse: TypeAlias = ObjectRegosObjectResult
OperatingCashEditChequeTemplateRequest: TypeAlias = OperatingCashChequeTemplateEdit
OperatingCashEditChequeTemplateResponse: TypeAlias = UpdateResult
OperatingCashEditRequest: TypeAlias = OperatingCashEdit
OperatingCashEditResponse: TypeAlias = UpdateResult
OperatingCashEditSettingsRequest: TypeAlias = list[OperatingCash_SettingEdit]
OperatingCashEditSettingsResponse: TypeAlias = UpdateResult
OperatingCashGetChequeTemplateRequest: TypeAlias = OperatingCashChequeTemplateGet
OperatingCashGetChequeTemplateResponse: TypeAlias = OperatingCashChequeTemplateRegosOffsettedArrayResult
OperatingCashGetImageRequest: TypeAlias = OperatingCashImageGet
OperatingCashGetImageResponse: TypeAlias = OperatingCashImageRegosArrayResult
OperatingCashGetRequest: TypeAlias = OperatingCashGet
OperatingCashGetResponse: TypeAlias = OperatingCashRegosOffsettedArrayResult
OperatingCashGetSettingsRequest: TypeAlias = OperatingCash_SettingGet
OperatingCashGetSettingsResponse: TypeAlias = OperatingCash_SettingArrayRegosObjectResult


_MODEL_NAMES = ['OperatingCash', 'OperatingCashAccept', 'OperatingCashAdd', 'OperatingCashChequeTemplate', 'OperatingCashChequeTemplateEdit', 'OperatingCashChequeTemplateGet', 'OperatingCashChequeTemplateRegosOffsettedArrayResult', 'OperatingCashDelete', 'OperatingCashDiscard', 'OperatingCashEdit', 'OperatingCashGet', 'OperatingCashImage', 'OperatingCashImageDelete', 'OperatingCashImageGet', 'OperatingCashImageRegosArrayResult', 'OperatingCashRegosOffsettedArrayResult', 'OperatingCash_Setting', 'OperatingCash_SettingArrayRegosObjectResult', 'OperatingCash_SettingEdit', 'OperatingCash_SettingGet', 'OperatingCash_SortOrder']


__all__ = [
    'OperatingCash',
    'OperatingCashAccept',
    'OperatingCashAdd',
    'OperatingCashChequeTemplate',
    'OperatingCashChequeTemplateEdit',
    'OperatingCashChequeTemplateGet',
    'OperatingCashChequeTemplateRegosOffsettedArrayResult',
    'OperatingCashDelete',
    'OperatingCashDiscard',
    'OperatingCashEdit',
    'OperatingCashGet',
    'OperatingCashImage',
    'OperatingCashImageDelete',
    'OperatingCashImageGet',
    'OperatingCashImageRegosArrayResult',
    'OperatingCashRegosOffsettedArrayResult',
    'OperatingCash_Setting',
    'OperatingCash_SettingArrayRegosObjectResult',
    'OperatingCash_SettingEdit',
    'OperatingCash_SettingGet',
    'OperatingCash_SortOrder',
    'OperatingCash_SortOrderColumn',
    'OperatingCashGetRequest',
    'OperatingCashGetResponse',
    'OperatingCashAddRequest',
    'OperatingCashAddResponse',
    'OperatingCashEditRequest',
    'OperatingCashEditResponse',
    'OperatingCashDeleteRequest',
    'OperatingCashDeleteResponse',
    'OperatingCashAcceptRequest',
    'OperatingCashAcceptResponse',
    'OperatingCashDiscardRequest',
    'OperatingCashDiscardResponse',
    'OperatingCashGetSettingsRequest',
    'OperatingCashGetSettingsResponse',
    'OperatingCashEditSettingsRequest',
    'OperatingCashEditSettingsResponse',
    'OperatingCashGetChequeTemplateRequest',
    'OperatingCashGetChequeTemplateResponse',
    'OperatingCashEditChequeTemplateRequest',
    'OperatingCashEditChequeTemplateResponse',
    'OperatingCashGetImageRequest',
    'OperatingCashGetImageResponse',
    'OperatingCashAddImageResponse',
    'OperatingCashDeleteImageRequest',
    'OperatingCashDeleteImageResponse'
]

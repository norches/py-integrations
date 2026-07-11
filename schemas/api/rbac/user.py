"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class User(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    first_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    login: str | None = PydField(default=None)
    can_authorize: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    language_code: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    full_name: str | None = PydField(default=None)
    main_phone: str | None = PydField(default=None)
    internal_phone: str | None = PydField(default=None)
    user_group: UserGroup | None = PydField(default=None)
    enable_hints: bool | None = PydField(default=None)
    system: bool | None = PydField(default=None)
    sub: str | None = PydField(default=None)
    photo_url: str | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    seller_barcode: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class UserAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    first_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    login: str | None = PydField(default=None)
    can_authorize: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    language_code: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    new_password: str | None = PydField(default=None)
    new_password_confirm: str | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class UserAddGlobal(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    phone: str | None = PydField(default=None)
    group_id: int | None = PydField(default=None)


class UserAddGlobalResposne(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    send_registration: bool | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class UserAddGlobalResposneRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: UserAddGlobalResposne | Error | None = PydField(default=None)


class UserCheckLoginIn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    login: str | None = PydField(default=None)


class UserCheckLoginOut(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    enable: bool | None = PydField(default=None)


class UserCheckLoginOutRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: UserCheckLoginOut | Error | None = PydField(default=None)


class UserDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    first_name: str | None = PydField(default=None)
    last_name: str | None = PydField(default=None)
    middle_name: str | None = PydField(default=None)
    sex: SexEnum | None = PydField(default=None)
    date_of_birth: str | None = PydField(default=None)
    address: str | None = PydField(default=None)
    phones: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    login: str | None = PydField(default=None)
    can_authorize: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    language_code: str | None = PydField(default=None)
    id: int | None = PydField(default=None)
    group_id: int | None = PydField(default=None)
    internal_phone: str | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class UserGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)
    gender: SexEnum | None = PydField(default=None)
    can_authorize: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    language_code: str | None = PydField(default=None)
    sub: str | None = PydField(default=None)
    sort_orders: list[User_SortOrder] | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    seller_barcode: str | None = PydField(default=None)
    search: str | None = PydField(default=None)
    internal_phone: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class UserImage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    size: int | None = PydField(default=None)
    file: str | None = PydField(default=None)
    url: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class UserImageDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class UserImageGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)
    compress_data: bool | None = PydField(default=None)
    user_id: int | None = PydField(default=None)


class UserImageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[UserImage] | Error | None = PydField(default=None)


class UserPasswordChange(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    user_id: int | None = PydField(default=None)
    new_password: str | None = PydField(default=None)
    new_password_confirm: str | None = PydField(default=None)


class UserPhoneChangeConfirmRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    confirm_code: str | None = PydField(default=None)


class UserPhoneChangeRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    phone: str | None = PydField(default=None)


class UserRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[User] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class User_SortOrder(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: User_SortOrderColumn | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class User_SortOrderColumn(IntEnum):
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
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ApiResult, ColumnSortOrderDirection, Error, InsertResult, SexEnum, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.rbac.user_group import UserGroup
from schemas.api.rbac.user_permission import UserPermissionGet, UserPermissionShortRegosArrayResult
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit


UserAddGlobalRequest: TypeAlias = UserAddGlobal
UserAddGlobalResponse: TypeAlias = UserAddGlobalResposneRegosObjectResult
UserAddImageResponse: TypeAlias = UpdateResult
UserAddRequest: TypeAlias = UserAdd
UserAddResponse: TypeAlias = InsertResult
UserCheckLoginRequest: TypeAlias = UserCheckLoginIn
UserCheckLoginResponse: TypeAlias = UserCheckLoginOutRegosObjectResult
UserDeleteImageRequest: TypeAlias = UserImageDelete
UserDeleteImageResponse: TypeAlias = UpdateResult
UserDeleteRequest: TypeAlias = UserDelete
UserDeleteResponse: TypeAlias = UpdateResult
UserEditRequest: TypeAlias = UserEdit
UserEditResponse: TypeAlias = UpdateResult
UserGetImageRequest: TypeAlias = UserImageGet
UserGetImageResponse: TypeAlias = UserImageRegosArrayResult
UserGetPermissionsRequest: TypeAlias = UserPermissionGet
UserGetPermissionsResponse: TypeAlias = UserPermissionShortRegosArrayResult
UserGetRequest: TypeAlias = UserGet
UserGetResponse: TypeAlias = UserRegosOffsettedArrayResult
UserPasswordChangeRequest: TypeAlias = UserPasswordChange
UserPasswordChangeResponse: TypeAlias = UpdateResult
UserPhoneChangeConfirmResponse: TypeAlias = ApiResult
UserPhoneChangeResponse: TypeAlias = ApiResult


_MODEL_NAMES = ['User', 'UserAdd', 'UserAddGlobal', 'UserAddGlobalResposne', 'UserAddGlobalResposneRegosObjectResult', 'UserCheckLoginIn', 'UserCheckLoginOut', 'UserCheckLoginOutRegosObjectResult', 'UserDelete', 'UserEdit', 'UserGet', 'UserImage', 'UserImageDelete', 'UserImageGet', 'UserImageRegosArrayResult', 'UserPasswordChange', 'UserPhoneChangeConfirmRequest', 'UserPhoneChangeRequest', 'UserRegosOffsettedArrayResult', 'User_SortOrder']


__all__ = [
    'User',
    'UserAdd',
    'UserAddGlobal',
    'UserAddGlobalResposne',
    'UserAddGlobalResposneRegosObjectResult',
    'UserCheckLoginIn',
    'UserCheckLoginOut',
    'UserCheckLoginOutRegosObjectResult',
    'UserDelete',
    'UserEdit',
    'UserGet',
    'UserImage',
    'UserImageDelete',
    'UserImageGet',
    'UserImageRegosArrayResult',
    'UserPasswordChange',
    'UserPhoneChangeConfirmRequest',
    'UserPhoneChangeRequest',
    'UserRegosOffsettedArrayResult',
    'User_SortOrder',
    'User_SortOrderColumn',
    'UserGetPermissionsRequest',
    'UserGetPermissionsResponse',
    'UserGetRequest',
    'UserGetResponse',
    'UserAddGlobalRequest',
    'UserAddGlobalResponse',
    'UserAddRequest',
    'UserAddResponse',
    'UserEditRequest',
    'UserEditResponse',
    'UserDeleteRequest',
    'UserDeleteResponse',
    'UserCheckLoginRequest',
    'UserCheckLoginResponse',
    'UserPasswordChangeRequest',
    'UserPasswordChangeResponse',
    'UserGetImageRequest',
    'UserGetImageResponse',
    'UserAddImageResponse',
    'UserDeleteImageRequest',
    'UserDeleteImageResponse',
    'UserPhoneChangeResponse',
    'UserPhoneChangeConfirmResponse'
]

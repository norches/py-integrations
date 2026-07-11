"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class PaymentType(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    account: Account | None = PydField(default=None)
    shortkey: int | None = PydField(default=None)
    is_cash: bool | None = PydField(default=None)
    kkm_code: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    enabled: PaymentTypeEnabled | None = PydField(default=None)
    image_url: str | None = PydField(default=None)


class PaymentTypeAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    account_id: int | None = PydField(default=None)
    is_cash: bool | None = PydField(default=None)
    kkm_code: int | None = PydField(default=None)
    shortkey: int | None = PydField(default=None)
    enabled: PaymentTypeEnabled | None = PydField(default=None)


class PaymentTypeArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PaymentType] | Error | None = PydField(default=None)


class PaymentTypeDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PaymentTypeEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    account_id: int | None = PydField(default=None)
    is_cash: bool | None = PydField(default=None)
    kkm_code: int | None = PydField(default=None)
    shortkey: int | None = PydField(default=None)
    enabled: PaymentTypeEnabled | None = PydField(default=None)


class PaymentTypeEnabled(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class PaymentTypeGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    account_ids: list[int] | None = PydField(default=None)
    enabled: PaymentTypeEnabled | None = PydField(default=None)
    is_cash: bool | None = PydField(default=None)


class PaymentTypeImage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    payment_type_id: int | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    size: int | None = PydField(default=None)
    url: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class PaymentTypeImageGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    payment_type_ids: list[int] | None = PydField(default=None)


class PaymentTypeImageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[PaymentTypeImage] | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, Error, InsertResult, UpdateResult
from schemas.api.references.account import Account


PaymentTypeAddImageResponse: TypeAlias = UpdateResult
PaymentTypeAddRequest: TypeAlias = PaymentTypeAdd
PaymentTypeAddResponse: TypeAlias = InsertResult
PaymentTypeDeleteImageRequest: TypeAlias = Base_ID
PaymentTypeDeleteImageResponse: TypeAlias = UpdateResult
PaymentTypeDeleteRequest: TypeAlias = PaymentTypeDelete
PaymentTypeDeleteResponse: TypeAlias = UpdateResult
PaymentTypeEditRequest: TypeAlias = PaymentTypeEdit
PaymentTypeEditResponse: TypeAlias = UpdateResult
PaymentTypeGetImageRequest: TypeAlias = PaymentTypeImageGet
PaymentTypeGetImageResponse: TypeAlias = PaymentTypeImageRegosArrayResult
PaymentTypeGetRequest: TypeAlias = PaymentTypeGet
PaymentTypeGetResponse: TypeAlias = PaymentTypeArrayRegosObjectResult


_MODEL_NAMES = ['PaymentType', 'PaymentTypeAdd', 'PaymentTypeArrayRegosObjectResult', 'PaymentTypeDelete', 'PaymentTypeEdit', 'PaymentTypeGet', 'PaymentTypeImage', 'PaymentTypeImageGet', 'PaymentTypeImageRegosArrayResult']


__all__ = [
    'PaymentType',
    'PaymentTypeAdd',
    'PaymentTypeArrayRegosObjectResult',
    'PaymentTypeDelete',
    'PaymentTypeEdit',
    'PaymentTypeEnabled',
    'PaymentTypeGet',
    'PaymentTypeImage',
    'PaymentTypeImageGet',
    'PaymentTypeImageRegosArrayResult',
    'PaymentTypeGetRequest',
    'PaymentTypeGetResponse',
    'PaymentTypeAddRequest',
    'PaymentTypeAddResponse',
    'PaymentTypeEditRequest',
    'PaymentTypeEditResponse',
    'PaymentTypeDeleteRequest',
    'PaymentTypeDeleteResponse',
    'PaymentTypeGetImageRequest',
    'PaymentTypeGetImageResponse',
    'PaymentTypeAddImageResponse',
    'PaymentTypeDeleteImageRequest',
    'PaymentTypeDeleteImageResponse'
]

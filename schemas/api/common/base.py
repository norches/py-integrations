"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.base import BaseSchema


JToken: TypeAlias = Any


class RegosModel(BaseSchema):
    """Base class for REGOS API Swagger schemas."""

    model_config = ConfigDict(extra="ignore", populate_by_name=True)


class AgregateStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ApiOffsettedResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Any | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ApiResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Any | Error | None = PydField(default=None)


class BaseLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class BaseSortColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: str | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class Base_ID(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class BooleanRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: bool | Error | None = PydField(default=None)


class CashAmountDetails(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    current_amount: _Decimal | None = PydField(default=None)
    start_amount: _Decimal | None = PydField(default=None)
    income: _Decimal | None = PydField(default=None)
    outcome: _Decimal | None = PydField(default=None)
    end_amount: _Decimal | None = PydField(default=None)


class CashAmountDetailsRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: CashAmountDetails | Error | None = PydField(default=None)


class ColumnSortOrderDirection(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class CommonFile(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    size: int | None = PydField(default=None)
    extension: str | None = PydField(default=None)
    mime_type: str | None = PydField(default=None)
    media_type: CommonFileMediaTypeEnum | None = PydField(default=None)
    width: int | None = PydField(default=None)
    height: int | None = PydField(default=None)
    duration_ms: int | None = PydField(default=None)
    aspect_ratio: _Decimal | None = PydField(default=None)
    date: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)
    hash: str | None = PydField(default=None)
    folder: CommonFolder | None = PydField(default=None)
    folder_id: int | None = PydField(default=None)
    cdn_name: str | None = PydField(default=None)
    url: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CommonFileAccessLevelEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class CommonFileMediaTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class CommonFolder(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    path: str | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    user_id: int | None = PydField(default=None)
    access_level: CommonFileAccessLevelEnum | None = PydField(default=None)
    date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)


class CommonMention(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    source_entity_type: MentionSourceEntityTypeEnum | None = PydField(default=None)
    source_entity_id: str | None = PydField(default=None)
    source_field: str | None = PydField(default=None)
    mentioned_entity_type: MentionedEntityTypeEnum | None = PydField(default=None)
    mentioned_entity_id: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    length: int | None = PydField(default=None)
    text: str | None = PydField(default=None)
    mentioned_entity_name: str | None = PydField(default=None)
    mentioned_entity_photo_url: str | None = PydField(default=None)
    read: bool | None = PydField(default=None)
    read_date: int | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    created_date: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CommonMentionInput(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    mentioned_entity_type: MentionedEntityTypeEnum | None = PydField(default=None)
    mentioned_entity_id: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    length: int | None = PydField(default=None)
    text: str | None = PydField(default=None)


class CommonMentionOptions(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    add_missing_users_to_context: bool | None = PydField(default=None)


class ContractDirection(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class CrmEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DataType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DecimalRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: _Decimal | Error | None = PydField(default=None)


class DiscountAction(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DiscountOperation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    action: DiscountAction | None = PydField(default=None)
    type: DiscountType | None = PydField(default=None)
    percent: _Decimal | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DiscountOperationAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    document_type_id__: int | None = PydField(default=None, alias="_document_type_id_")
    action: DiscountAction | None = PydField(default=None)
    type: DiscountType | None = PydField(default=None)
    percent: _Decimal | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)


class DiscountOperationDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    document_type_id__: int | None = PydField(default=None, alias="_document_type_id_")


class DiscountOperationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    document_ids: list[int] | None = PydField(default=None)
    document_type_id__: int | None = PydField(default=None, alias="_document_type_id_")


class DiscountOperationRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DiscountOperation] | Error | None = PydField(default=None)


class DiscountType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DocsOperationsCopy(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    doc_from_id: int | None = PydField(default=None)
    doc_to_id: int | None = PydField(default=None)


class DocsOperationsMovement(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    doc_from_id: int | None = PydField(default=None)
    doc_to_id: int | None = PydField(default=None)


class Error(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    error: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class ErrorResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Error | None = PydField(default=None)


class Insert(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    new_id: int | None = PydField(default=None)


class InsertResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Insert | Error | None = PydField(default=None)


class Insert_uuid(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    new_uuid: str | None = PydField(default=None)


class Insert_uuid_Result(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Insert_uuid | Error | None = PydField(default=None)


class Int64RegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: int | Error | None = PydField(default=None)


class LegalStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Location(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    longitude: _Decimal | None = PydField(default=None)
    latitude: _Decimal | None = PydField(default=None)


class MentionSourceEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_11 = 11


class MentionedEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class ObjectRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Any | Error | None = PydField(default=None)


class OkResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)


class Permission(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    permission_group: PermissionGroup | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    default_value: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class SetPriceByPriceType_Model(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)


class SexEnum(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class SingleArrayOffsettedResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Any | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class SingleArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Any | Error | None = PydField(default=None)


class SingleObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Any | Error | None = PydField(default=None)


class StringRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: str | Error | None = PydField(default=None)


class Table(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class Update(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    row_affected: int | None = PydField(default=None)
    ids: list[Any] | None = PydField(default=None)


class UpdateResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: Update | Error | None = PydField(default=None)


class VatCalculationTypeEnum(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.rbac.permission_group import PermissionGroup


_MODEL_NAMES = ['ApiOffsettedResult', 'ApiResult', 'BaseLockAndUnlock', 'BaseSortColumn', 'Base_ID', 'BooleanRegosObjectResult', 'CashAmountDetails', 'CashAmountDetailsRegosObjectResult', 'CommonFile', 'CommonFolder', 'CommonMention', 'CommonMentionInput', 'CommonMentionOptions', 'DecimalRegosObjectResult', 'DiscountOperation', 'DiscountOperationAdd', 'DiscountOperationDelete', 'DiscountOperationGet', 'DiscountOperationRegosArrayResult', 'DocsOperationsCopy', 'DocsOperationsMovement', 'Error', 'ErrorResult', 'Insert', 'InsertResult', 'Insert_uuid', 'Insert_uuid_Result', 'Int64RegosObjectResult', 'Location', 'ObjectRegosObjectResult', 'OkResult', 'Permission', 'SetPriceByPriceType_Model', 'SingleArrayOffsettedResult', 'SingleArrayResult', 'SingleObjectResult', 'StringRegosObjectResult', 'Table', 'Update', 'UpdateResult']


__all__ = [
    'JToken',
    'RegosModel',
    'AgregateStatusEnum',
    'ApiOffsettedResult',
    'ApiResult',
    'BaseLockAndUnlock',
    'BaseSortColumn',
    'Base_ID',
    'BooleanRegosObjectResult',
    'CashAmountDetails',
    'CashAmountDetailsRegosObjectResult',
    'ColumnSortOrderDirection',
    'CommonFile',
    'CommonFileAccessLevelEnum',
    'CommonFileMediaTypeEnum',
    'CommonFolder',
    'CommonMention',
    'CommonMentionInput',
    'CommonMentionOptions',
    'ContractDirection',
    'CrmEntityTypeEnum',
    'DataType',
    'DecimalRegosObjectResult',
    'DiscountAction',
    'DiscountOperation',
    'DiscountOperationAdd',
    'DiscountOperationDelete',
    'DiscountOperationGet',
    'DiscountOperationRegosArrayResult',
    'DiscountType',
    'DocsOperationsCopy',
    'DocsOperationsMovement',
    'Error',
    'ErrorResult',
    'Insert',
    'InsertResult',
    'Insert_uuid',
    'Insert_uuid_Result',
    'Int64RegosObjectResult',
    'LegalStatus',
    'Location',
    'MentionSourceEntityTypeEnum',
    'MentionedEntityTypeEnum',
    'ObjectRegosObjectResult',
    'OkResult',
    'Permission',
    'SetPriceByPriceType_Model',
    'SexEnum',
    'SingleArrayOffsettedResult',
    'SingleArrayResult',
    'SingleObjectResult',
    'StringRegosObjectResult',
    'Table',
    'Update',
    'UpdateResult',
    'VatCalculationTypeEnum'
]

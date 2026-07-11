"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class RetailCardMigrationHistory(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    type: RetailCardMigrationHistoryType | None = PydField(default=None)
    promo_old: int | None = PydField(default=None)
    promo_old_string: str | None = PydField(default=None)
    promo_new: int | None = PydField(default=None)
    promo_new_string: str | None = PydField(default=None)


class RetailCardMigrationHistoryGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    card_id: int | None = PydField(default=None)


class RetailCardMigrationHistoryRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCardMigrationHistory] | Error | None = PydField(default=None)


class RetailCardMigrationHistoryType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class RetailCardMigrationSetting(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    task_id: int | None = PydField(default=None)
    type: RetailCardMigrationSettingType | None = PydField(default=None)
    period_type: RetailCardMigrationSettingPeriod | None = PydField(default=None)
    period: int | None = PydField(default=None)
    comparison: RetailCardMigrationSettingComparisonType | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)
    id: int | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)


class RetailCardMigrationSettingBase(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    task_id: int | None = PydField(default=None)
    type: RetailCardMigrationSettingType | None = PydField(default=None)
    period_type: RetailCardMigrationSettingPeriod | None = PydField(default=None)
    period: int | None = PydField(default=None)
    comparison: RetailCardMigrationSettingComparisonType | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)


class RetailCardMigrationSettingComparisonType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class RetailCardMigrationSettingCondition(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    setting_id: int | None = PydField(default=None)
    type: RetailCardMigrationSettingConditionType | None = PydField(default=None)
    value: int | None = PydField(default=None)
    exclude: bool | None = PydField(default=None)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)


class RetailCardMigrationSettingConditionBase(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    setting_id: int | None = PydField(default=None)
    type: RetailCardMigrationSettingConditionType | None = PydField(default=None)
    value: int | None = PydField(default=None)
    exclude: bool | None = PydField(default=None)


class RetailCardMigrationSettingConditionGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    setting_id: int | None = PydField(default=None)


class RetailCardMigrationSettingConditionRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCardMigrationSettingCondition] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailCardMigrationSettingConditionType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class RetailCardMigrationSettingEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    period_type: RetailCardMigrationSettingPeriod | None = PydField(default=None)
    period: int | None = PydField(default=None)
    comparison: RetailCardMigrationSettingComparisonType | None = PydField(default=None)
    value: _Decimal | None = PydField(default=None)
    order: int | None = PydField(default=None)


class RetailCardMigrationSettingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    task_id: int | None = PydField(default=None)


class RetailCardMigrationSettingPeriod(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class RetailCardMigrationSettingRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCardMigrationSetting] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class RetailCardMigrationSettingType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class RetailCardMigrationTask(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    run_period_type: RetailCardMigrationTaskPeriod | None = PydField(default=None)
    run_period: int | None = PydField(default=None)
    order: int | None = PydField(default=None)
    id: int | None = PydField(default=None)
    promo_from: PromoProgram | None = PydField(default=None)
    promo_to: PromoProgram | None = PydField(default=None)
    last_run: int | None = PydField(default=None)


class RetailCardMigrationTaskAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    run_period_type: RetailCardMigrationTaskPeriod | None = PydField(default=None)
    run_period: int | None = PydField(default=None)
    order: int | None = PydField(default=None)
    promo_from_id: int | None = PydField(default=None)
    promo_to_id: int | None = PydField(default=None)


class RetailCardMigrationTaskEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    run_period_type: RetailCardMigrationTaskPeriod | None = PydField(default=None)
    run_period: int | None = PydField(default=None)
    order: int | None = PydField(default=None)
    promo_from_id: int | None = PydField(default=None)
    promo_to_id: int | None = PydField(default=None)
    id: int | None = PydField(default=None)


class RetailCardMigrationTaskGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    promo_from_ids: list[int] | None = PydField(default=None)
    promo_to_ids: list[int] | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailCardMigrationTaskPeriod(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class RetailCardMigrationTaskRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailCardMigrationTask] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseSortColumn, Base_ID, Error, InsertResult, UpdateResult
from schemas.api.references.promo_program import PromoProgram


RetailCardMigrationSettingConditionAddRequest: TypeAlias = RetailCardMigrationSettingConditionBase
RetailCardMigrationSettingConditionAddResponse: TypeAlias = InsertResult
RetailCardMigrationSettingConditionDeleteRequest: TypeAlias = Base_ID
RetailCardMigrationSettingConditionDeleteResponse: TypeAlias = UpdateResult
RetailCardMigrationSettingConditionGetRequest: TypeAlias = RetailCardMigrationSettingConditionGet
RetailCardMigrationSettingConditionGetResponse: TypeAlias = RetailCardMigrationSettingConditionRegosOffsettedArrayResult
RetailCardMigrationSettingsAddRequest: TypeAlias = RetailCardMigrationSettingBase
RetailCardMigrationSettingsAddResponse: TypeAlias = InsertResult
RetailCardMigrationSettingsDeleteRequest: TypeAlias = Base_ID
RetailCardMigrationSettingsDeleteResponse: TypeAlias = UpdateResult
RetailCardMigrationSettingsEditRequest: TypeAlias = RetailCardMigrationSettingEdit
RetailCardMigrationSettingsEditResponse: TypeAlias = UpdateResult
RetailCardMigrationSettingsGetRequest: TypeAlias = RetailCardMigrationSettingGet
RetailCardMigrationSettingsGetResponse: TypeAlias = RetailCardMigrationSettingRegosOffsettedArrayResult
RetailCardMigrationTasksAddRequest: TypeAlias = RetailCardMigrationTaskAdd
RetailCardMigrationTasksAddResponse: TypeAlias = InsertResult
RetailCardMigrationTasksDeleteRequest: TypeAlias = Base_ID
RetailCardMigrationTasksDeleteResponse: TypeAlias = UpdateResult
RetailCardMigrationTasksEditRequest: TypeAlias = RetailCardMigrationTaskEdit
RetailCardMigrationTasksEditResponse: TypeAlias = UpdateResult
RetailCardMigrationTasksGetRequest: TypeAlias = RetailCardMigrationTaskGet
RetailCardMigrationTasksGetResponse: TypeAlias = RetailCardMigrationTaskRegosOffsettedArrayResult


_MODEL_NAMES = ['RetailCardMigrationHistory', 'RetailCardMigrationHistoryGet', 'RetailCardMigrationHistoryRegosArrayResult', 'RetailCardMigrationSetting', 'RetailCardMigrationSettingBase', 'RetailCardMigrationSettingCondition', 'RetailCardMigrationSettingConditionBase', 'RetailCardMigrationSettingConditionGet', 'RetailCardMigrationSettingConditionRegosOffsettedArrayResult', 'RetailCardMigrationSettingEdit', 'RetailCardMigrationSettingGet', 'RetailCardMigrationSettingRegosOffsettedArrayResult', 'RetailCardMigrationTask', 'RetailCardMigrationTaskAdd', 'RetailCardMigrationTaskEdit', 'RetailCardMigrationTaskGet', 'RetailCardMigrationTaskRegosOffsettedArrayResult']


__all__ = [
    'RetailCardMigrationHistory',
    'RetailCardMigrationHistoryGet',
    'RetailCardMigrationHistoryRegosArrayResult',
    'RetailCardMigrationHistoryType',
    'RetailCardMigrationSetting',
    'RetailCardMigrationSettingBase',
    'RetailCardMigrationSettingComparisonType',
    'RetailCardMigrationSettingCondition',
    'RetailCardMigrationSettingConditionBase',
    'RetailCardMigrationSettingConditionGet',
    'RetailCardMigrationSettingConditionRegosOffsettedArrayResult',
    'RetailCardMigrationSettingConditionType',
    'RetailCardMigrationSettingEdit',
    'RetailCardMigrationSettingGet',
    'RetailCardMigrationSettingPeriod',
    'RetailCardMigrationSettingRegosOffsettedArrayResult',
    'RetailCardMigrationSettingType',
    'RetailCardMigrationTask',
    'RetailCardMigrationTaskAdd',
    'RetailCardMigrationTaskEdit',
    'RetailCardMigrationTaskGet',
    'RetailCardMigrationTaskPeriod',
    'RetailCardMigrationTaskRegosOffsettedArrayResult',
    'RetailCardMigrationTasksGetRequest',
    'RetailCardMigrationTasksGetResponse',
    'RetailCardMigrationTasksAddRequest',
    'RetailCardMigrationTasksAddResponse',
    'RetailCardMigrationTasksEditRequest',
    'RetailCardMigrationTasksEditResponse',
    'RetailCardMigrationTasksDeleteRequest',
    'RetailCardMigrationTasksDeleteResponse',
    'RetailCardMigrationSettingsGetRequest',
    'RetailCardMigrationSettingsGetResponse',
    'RetailCardMigrationSettingsAddRequest',
    'RetailCardMigrationSettingsAddResponse',
    'RetailCardMigrationSettingsEditRequest',
    'RetailCardMigrationSettingsEditResponse',
    'RetailCardMigrationSettingsDeleteRequest',
    'RetailCardMigrationSettingsDeleteResponse',
    'RetailCardMigrationSettingConditionGetRequest',
    'RetailCardMigrationSettingConditionGetResponse',
    'RetailCardMigrationSettingConditionAddRequest',
    'RetailCardMigrationSettingConditionAddResponse',
    'RetailCardMigrationSettingConditionDeleteRequest',
    'RetailCardMigrationSettingConditionDeleteResponse'
]

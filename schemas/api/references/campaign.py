"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Campaign(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    type: CampaignTypeEnum | None = PydField(default=None)
    date: int | None = PydField(default=None)
    run_date: int | None = PydField(default=None)
    run_immediately: bool | None = PydField(default=None)
    message: str | None = PydField(default=None)
    file_id: int | None = PydField(default=None)
    image_url: str | None = PydField(default=None)
    recipient_count: int | None = PydField(default=None)
    status: CampaignStatusEnum | None = PydField(default=None)
    scheduler_uuid: str | None = PydField(default=None)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    integration_connected_integration_id: str | None = PydField(default=None)
    recepients_json: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CampaignAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: CampaignTypeEnum | None = PydField(default=None)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    run_date: int | None = PydField(default=None)
    run_immediately: bool | None = PydField(default=None)
    name: str | None = PydField(default=None)
    message: str | None = PydField(default=None)
    file: str | None = PydField(default=None)
    recepients: list[CampaignRecepient] | None = PydField(default=None)


class CampaignColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: CampaignColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class CampaignColumns(IntEnum):
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
    VALUE_12 = 12


class CampaignEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    message: str | None = PydField(default=None)
    file: str | None = PydField(default=None)
    run_date: int | None = PydField(default=None)
    run_immediately: bool | None = PydField(default=None)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)


class CampaignGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    status: CampaignStatusEnum | None = PydField(default=None)
    type: CampaignTypeEnum | None = PydField(default=None)
    search: str | None = PydField(default=None)
    sort_orders: list[CampaignColumn] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class CampaignRecepient(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: CampaignRecipientEntityTypeEnum | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)


class CampaignRecipient(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    campaign_id: int | None = PydField(default=None)
    recipient: str | None = PydField(default=None)
    state: CampaignRecipientState | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CampaignRecipientEntityTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class CampaignRecipientRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CampaignRecipient] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class CampaignRecipientSetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    state: CampaignRecipientState | None = PydField(default=None)


class CampaignRecipientState(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class CampaignRecipientsGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    campaign_id: int | None = PydField(default=None)
    state: CampaignRecipientState | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class CampaignRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Campaign] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class CampaignSetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    status: CampaignStatusEnum | None = PydField(default=None)
    error_message: str | None = PydField(default=None)


class CampaignStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class CampaignTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Base_ID, ColumnSortOrderDirection, Error, InsertResult, SingleObjectResult, UpdateResult
from schemas.api.common.filter import Filter


CampaignAddRequest: TypeAlias = CampaignAdd
CampaignAddResponse: TypeAlias = InsertResult
CampaignDeleteRequest: TypeAlias = Base_ID
CampaignDeleteResponse: TypeAlias = UpdateResult
CampaignEditRequest: TypeAlias = CampaignEdit
CampaignEditResponse: TypeAlias = UpdateResult
CampaignGetRecipientsRequest: TypeAlias = CampaignRecipientsGet
CampaignGetRecipientsResponse: TypeAlias = CampaignRecipientRegosOffsettedArrayResult
CampaignGetRequest: TypeAlias = CampaignGet
CampaignGetResponse: TypeAlias = CampaignRegosOffsettedArrayResult
CampaignSetRecipientsStatusRequest: TypeAlias = list[CampaignRecipientSetStatus]
CampaignSetRecipientsStatusResponse: TypeAlias = SingleObjectResult
CampaignSetStatusRequest: TypeAlias = CampaignSetStatus
CampaignSetStatusResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Campaign', 'CampaignAdd', 'CampaignColumn', 'CampaignEdit', 'CampaignGet', 'CampaignRecepient', 'CampaignRecipient', 'CampaignRecipientRegosOffsettedArrayResult', 'CampaignRecipientSetStatus', 'CampaignRecipientsGet', 'CampaignRegosOffsettedArrayResult', 'CampaignSetStatus']


__all__ = [
    'Campaign',
    'CampaignAdd',
    'CampaignColumn',
    'CampaignColumns',
    'CampaignEdit',
    'CampaignGet',
    'CampaignRecepient',
    'CampaignRecipient',
    'CampaignRecipientEntityTypeEnum',
    'CampaignRecipientRegosOffsettedArrayResult',
    'CampaignRecipientSetStatus',
    'CampaignRecipientState',
    'CampaignRecipientsGet',
    'CampaignRegosOffsettedArrayResult',
    'CampaignSetStatus',
    'CampaignStatusEnum',
    'CampaignTypeEnum',
    'CampaignGetRequest',
    'CampaignGetResponse',
    'CampaignAddRequest',
    'CampaignAddResponse',
    'CampaignEditRequest',
    'CampaignEditResponse',
    'CampaignDeleteRequest',
    'CampaignDeleteResponse',
    'CampaignSetStatusRequest',
    'CampaignSetStatusResponse',
    'CampaignGetRecipientsRequest',
    'CampaignGetRecipientsResponse',
    'CampaignSetRecipientsStatusRequest',
    'CampaignSetRecipientsStatusResponse'
]

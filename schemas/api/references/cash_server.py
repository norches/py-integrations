"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class CashServer(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    last_sync: int | None = PydField(default=None)
    sync_status: CashServers_SyncStatus | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class CashServerAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    name: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class CashServerArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[CashServer] | Error | None = PydField(default=None)


class CashServerEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class CashServerGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    search: str | None = PydField(default=None)


class CashServerOnlyId(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class CashServers_SyncStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class EndSyncDatetime(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    row_affected: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)


class EndSyncDatetimeRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: EndSyncDatetime | Error | None = PydField(default=None)


class StartSyncDatetime(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    row_affected: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)


class StartSyncDatetimeRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: StartSyncDatetime | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.references.firm import Firm


CashServerAddRequest: TypeAlias = CashServerAdd
CashServerAddResponse: TypeAlias = InsertResult
CashServerBeginSyncRequest: TypeAlias = CashServerOnlyId
CashServerBeginSyncResponse: TypeAlias = StartSyncDatetimeRegosObjectResult
CashServerDeleteRequest: TypeAlias = CashServerOnlyId
CashServerDeleteResponse: TypeAlias = UpdateResult
CashServerEditRequest: TypeAlias = CashServerEdit
CashServerEditResponse: TypeAlias = UpdateResult
CashServerEndSyncRequest: TypeAlias = CashServerOnlyId
CashServerEndSyncResponse: TypeAlias = EndSyncDatetimeRegosObjectResult
CashServerGetRequest: TypeAlias = CashServerGet
CashServerGetResponse: TypeAlias = CashServerArrayRegosObjectResult


_MODEL_NAMES = ['CashServer', 'CashServerAdd', 'CashServerArrayRegosObjectResult', 'CashServerEdit', 'CashServerGet', 'CashServerOnlyId', 'EndSyncDatetime', 'EndSyncDatetimeRegosObjectResult', 'StartSyncDatetime', 'StartSyncDatetimeRegosObjectResult']


__all__ = [
    'CashServer',
    'CashServerAdd',
    'CashServerArrayRegosObjectResult',
    'CashServerEdit',
    'CashServerGet',
    'CashServerOnlyId',
    'CashServers_SyncStatus',
    'EndSyncDatetime',
    'EndSyncDatetimeRegosObjectResult',
    'StartSyncDatetime',
    'StartSyncDatetimeRegosObjectResult',
    'CashServerGetRequest',
    'CashServerGetResponse',
    'CashServerAddRequest',
    'CashServerAddResponse',
    'CashServerEditRequest',
    'CashServerEditResponse',
    'CashServerDeleteRequest',
    'CashServerDeleteResponse',
    'CashServerBeginSyncRequest',
    'CashServerBeginSyncResponse',
    'CashServerEndSyncRequest',
    'CashServerEndSyncResponse'
]

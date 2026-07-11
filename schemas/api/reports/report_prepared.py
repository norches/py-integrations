"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ReportPrepared(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    user: User | None = PydField(default=None)
    request_uuid: str | None = PydField(default=None)
    file_url: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    warnings: str | None = PydField(default=None)
    parameters: str | None = PydField(default=None)
    report: Report | None = PydField(default=None)
    data: str | None = PydField(default=None)
    saved: bool | None = PydField(default=None)
    date: int | None = PydField(default=None)


class ReportPreparedArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ReportPrepared] | Error | None = PydField(default=None)


class ReportPreparedGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    report_ids: list[int] | None = PydField(default=None)
    request_uuid: str | None = PydField(default=None)
    user_ids: list[int] | None = PydField(default=None)
    include_data: bool | None = PydField(default=None)


class ReportPreparedRemove(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    request_uuid: str | None = PydField(default=None)


class ReportPreparedSave(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    request_uuid: str | None = PydField(default=None)
    save: bool | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, UpdateResult
from schemas.api.rbac.user import User
from schemas.api.reports.report import Report


ReportPreparedGetRequest: TypeAlias = ReportPreparedGet
ReportPreparedGetResponse: TypeAlias = ReportPreparedArrayRegosObjectResult
ReportPreparedRemoveRequest: TypeAlias = ReportPreparedRemove
ReportPreparedRemoveResponse: TypeAlias = UpdateResult
ReportPreparedSaveRequest: TypeAlias = ReportPreparedSave
ReportPreparedSaveResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['ReportPrepared', 'ReportPreparedArrayRegosObjectResult', 'ReportPreparedGet', 'ReportPreparedRemove', 'ReportPreparedSave']


__all__ = [
    'ReportPrepared',
    'ReportPreparedArrayRegosObjectResult',
    'ReportPreparedGet',
    'ReportPreparedRemove',
    'ReportPreparedSave',
    'ReportPreparedGetRequest',
    'ReportPreparedGetResponse',
    'ReportPreparedSaveRequest',
    'ReportPreparedSaveResponse',
    'ReportPreparedRemoveRequest',
    'ReportPreparedRemoveResponse'
]

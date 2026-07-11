"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Pipeline(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    entity_type: CrmEntityTypeEnum | None = PydField(default=None)
    name: str | None = PydField(default=None)
    is_default: bool | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    stages: list[Stage] | None = PydField(default=None)


class PipelineAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: CrmEntityTypeEnum | None = PydField(default=None)
    name: str | None = PydField(default=None)
    is_default: bool | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class PipelineDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class PipelineEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    is_default: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class PipelineGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    entity_type: CrmEntityTypeEnum | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class PipelineRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Pipeline] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class PipelineSetAccess(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    access_all: bool | None = PydField(default=None)
    access_user_ids: list[int] | None = PydField(default=None)
    access_group_ids: list[int] | None = PydField(default=None)
    replace_mode: bool | None = PydField(default=None)


class PipelineSetStage(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    sort_order: int | None = PydField(default=None)
    is_start: bool | None = PydField(default=None)
    is_terminal: bool | None = PydField(default=None)
    is_success: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)


class PipelineSetStages(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    pipeline_id: int | None = PydField(default=None)
    stages: list[PipelineSetStage] | None = PydField(default=None)


class Stage(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    pipeline_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    code: str | None = PydField(default=None)
    sort_order: int | None = PydField(default=None)
    is_start: bool | None = PydField(default=None)
    is_terminal: bool | None = PydField(default=None)
    is_success: bool | None = PydField(default=None)
    active: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import CrmEntityTypeEnum, Error, InsertResult, UpdateResult


CrmEntityTypeEnum: TypeAlias = CrmEntityTypeEnum
PipelineAddRequest: TypeAlias = PipelineAdd
PipelineAddResponse: TypeAlias = InsertResult
PipelineDeleteRequest: TypeAlias = PipelineDelete
PipelineDeleteResponse: TypeAlias = UpdateResult
PipelineEditRequest: TypeAlias = PipelineEdit
PipelineEditResponse: TypeAlias = UpdateResult
PipelineGetRequest: TypeAlias = PipelineGet
PipelineGetResponse: TypeAlias = PipelineRegosOffsettedArrayResult
PipelineSetAccessRequest: TypeAlias = PipelineSetAccess
PipelineSetAccessResponse: TypeAlias = UpdateResult
PipelineSetStagesRequest: TypeAlias = PipelineSetStages
PipelineSetStagesResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Pipeline', 'PipelineAdd', 'PipelineDelete', 'PipelineEdit', 'PipelineGet', 'PipelineRegosOffsettedArrayResult', 'PipelineSetAccess', 'PipelineSetStage', 'PipelineSetStages', 'Stage']


__all__ = [
    'Pipeline',
    'PipelineAdd',
    'PipelineDelete',
    'PipelineEdit',
    'PipelineGet',
    'PipelineRegosOffsettedArrayResult',
    'PipelineSetAccess',
    'PipelineSetStage',
    'PipelineSetStages',
    'Stage',
    'PipelineGetRequest',
    'PipelineGetResponse',
    'PipelineAddRequest',
    'PipelineAddResponse',
    'PipelineEditRequest',
    'PipelineEditResponse',
    'PipelineSetAccessRequest',
    'PipelineSetAccessResponse',
    'PipelineDeleteRequest',
    'PipelineDeleteResponse',
    'PipelineSetStagesRequest',
    'PipelineSetStagesResponse',
    'CrmEntityTypeEnum'
]

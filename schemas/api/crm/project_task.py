"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class ProjectTask(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    project_id: int | None = PydField(default=None)
    parent_task_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMention] | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    deal_id: int | None = PydField(default=None)
    client: Client | None = PydField(default=None)
    chat_id: str | None = PydField(default=None)
    observer_user_ids: list[int] | None = PydField(default=None)
    status: ProjectTaskStatusEnum | None = PydField(default=None)
    due_date: int | None = PydField(default=None)
    created_date: int | None = PydField(default=None)
    attachment_file_ids: list[int] | None = PydField(default=None)
    inline_file_ids: list[int] | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    closed_user_id: int | None = PydField(default=None)
    closed_date: int | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ProjectTaskAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    project_id: int | None = PydField(default=None)
    parent_task_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    client_id: int | None = PydField(default=None)
    deal_id: int | None = PydField(default=None)
    observer_user_ids: list[int] | None = PydField(default=None)
    due_date: int | None = PydField(default=None)
    attachment_file_ids: list[int] | None = PydField(default=None)
    inline_file_ids: list[int] | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class ProjectTaskDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ProjectTaskEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_task_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    description_mentions: list[CommonMentionInput] | None = PydField(default=None)
    mention_options: CommonMentionOptions | None = PydField(default=None)
    client_id: int | None = PydField(default=None)
    deal_id: int | None = PydField(default=None)
    attachment_file_ids: list[int] | None = PydField(default=None)
    inline_file_ids: list[int] | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class ProjectTaskGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    project_ids: list[int] | None = PydField(default=None)
    parent_task_ids: list[int] | None = PydField(default=None)
    responsible_user_ids: list[int] | None = PydField(default=None)
    client_ids: list[int] | None = PydField(default=None)
    deal_ids: list[int] | None = PydField(default=None)
    observer_user_ids: list[int] | None = PydField(default=None)
    statuses: list[ProjectTaskStatusEnum] | None = PydField(default=None)
    due_from: int | None = PydField(default=None)
    due_to: int | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    include_mentions: bool | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)
    sort_orders: list[BaseSortColumn] | None = PydField(default=None)


class ProjectTaskRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[ProjectTask] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ProjectTaskSetDue(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    due_date: int | None = PydField(default=None)


class ProjectTaskSetObservers(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    observer_user_ids: list[int] | None = PydField(default=None)
    replace_mode: bool | None = PydField(default=None)


class ProjectTaskSetProject(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    project_id: int | None = PydField(default=None)


class ProjectTaskSetResponsible(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)


class ProjectTaskSetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    status: ProjectTaskStatusEnum | None = PydField(default=None)


class ProjectTaskStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import BaseSortColumn, CommonMention, CommonMentionInput, CommonMentionOptions, Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.crm.client import Client
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit


ProjectTaskAddRequest: TypeAlias = ProjectTaskAdd
ProjectTaskAddResponse: TypeAlias = InsertResult
ProjectTaskDeleteRequest: TypeAlias = ProjectTaskDelete
ProjectTaskDeleteResponse: TypeAlias = UpdateResult
ProjectTaskEditRequest: TypeAlias = ProjectTaskEdit
ProjectTaskEditResponse: TypeAlias = UpdateResult
ProjectTaskGetRequest: TypeAlias = ProjectTaskGet
ProjectTaskGetResponse: TypeAlias = ProjectTaskRegosOffsettedArrayResult
ProjectTaskSetDueRequest: TypeAlias = ProjectTaskSetDue
ProjectTaskSetDueResponse: TypeAlias = UpdateResult
ProjectTaskSetObserversRequest: TypeAlias = ProjectTaskSetObservers
ProjectTaskSetObserversResponse: TypeAlias = UpdateResult
ProjectTaskSetProjectRequest: TypeAlias = ProjectTaskSetProject
ProjectTaskSetProjectResponse: TypeAlias = UpdateResult
ProjectTaskSetResponsibleRequest: TypeAlias = ProjectTaskSetResponsible
ProjectTaskSetResponsibleResponse: TypeAlias = UpdateResult
ProjectTaskSetStatusRequest: TypeAlias = ProjectTaskSetStatus
ProjectTaskSetStatusResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['ProjectTask', 'ProjectTaskAdd', 'ProjectTaskDelete', 'ProjectTaskEdit', 'ProjectTaskGet', 'ProjectTaskRegosOffsettedArrayResult', 'ProjectTaskSetDue', 'ProjectTaskSetObservers', 'ProjectTaskSetProject', 'ProjectTaskSetResponsible', 'ProjectTaskSetStatus']


__all__ = [
    'ProjectTask',
    'ProjectTaskAdd',
    'ProjectTaskDelete',
    'ProjectTaskEdit',
    'ProjectTaskGet',
    'ProjectTaskRegosOffsettedArrayResult',
    'ProjectTaskSetDue',
    'ProjectTaskSetObservers',
    'ProjectTaskSetProject',
    'ProjectTaskSetResponsible',
    'ProjectTaskSetStatus',
    'ProjectTaskStatusEnum',
    'ProjectTaskGetRequest',
    'ProjectTaskGetResponse',
    'ProjectTaskAddRequest',
    'ProjectTaskAddResponse',
    'ProjectTaskEditRequest',
    'ProjectTaskEditResponse',
    'ProjectTaskDeleteRequest',
    'ProjectTaskDeleteResponse',
    'ProjectTaskSetStatusRequest',
    'ProjectTaskSetStatusResponse',
    'ProjectTaskSetDueRequest',
    'ProjectTaskSetDueResponse',
    'ProjectTaskSetProjectRequest',
    'ProjectTaskSetProjectResponse',
    'ProjectTaskSetResponsibleRequest',
    'ProjectTaskSetResponsibleResponse',
    'ProjectTaskSetObserversRequest',
    'ProjectTaskSetObserversResponse'
]

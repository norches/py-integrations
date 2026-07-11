"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Client(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    photo_url: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    sentiment_score_avg: _Decimal | None = PydField(default=None)
    sentiment_score_count: int | None = PydField(default=None)
    sentiment_score_rolling_avg: _Decimal | None = PydField(default=None)
    deleted: bool | None = PydField(default=None)
    created_user_id: int | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    fields: list[FieldValue] | None = PydField(default=None)


class ClientAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    external_id: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    photo_url: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    fields: list[FieldValueAdd] | None = PydField(default=None)


class ClientDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class ClientEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    phone: str | None = PydField(default=None)
    email: str | None = PydField(default=None)
    photo_url: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)
    fields: list[FieldValueEdit] | None = PydField(default=None)


class ClientGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    phones: list[str] | None = PydField(default=None)
    external_ids: list[str] | None = PydField(default=None)
    emails: list[str] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    responsible_user_ids: list[int] | None = PydField(default=None)
    filters: list[Filter] | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class ClientMerge(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    source_client_id: int | None = PydField(default=None)
    target_client_id: int | None = PydField(default=None)
    comment: str | None = PydField(default=None)


class ClientRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Client] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class ClientSetResponsible(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    responsible_user_id: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, InsertResult, UpdateResult
from schemas.api.common.filter import Filter
from schemas.api.references.field import FieldValue, FieldValueAdd, FieldValueEdit


ClientAddRequest: TypeAlias = ClientAdd
ClientAddResponse: TypeAlias = InsertResult
ClientDeleteRequest: TypeAlias = ClientDelete
ClientDeleteResponse: TypeAlias = UpdateResult
ClientEditRequest: TypeAlias = ClientEdit
ClientEditResponse: TypeAlias = UpdateResult
ClientGetRequest: TypeAlias = ClientGet
ClientGetResponse: TypeAlias = ClientRegosOffsettedArrayResult
ClientMergeRequest: TypeAlias = ClientMerge
ClientMergeResponse: TypeAlias = UpdateResult
ClientSetResponsibleRequest: TypeAlias = ClientSetResponsible
ClientSetResponsibleResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Client', 'ClientAdd', 'ClientDelete', 'ClientEdit', 'ClientGet', 'ClientMerge', 'ClientRegosOffsettedArrayResult', 'ClientSetResponsible']


__all__ = [
    'Client',
    'ClientAdd',
    'ClientDelete',
    'ClientEdit',
    'ClientGet',
    'ClientMerge',
    'ClientRegosOffsettedArrayResult',
    'ClientSetResponsible',
    'ClientGetRequest',
    'ClientGetResponse',
    'ClientAddRequest',
    'ClientAddResponse',
    'ClientEditRequest',
    'ClientEditResponse',
    'ClientDeleteRequest',
    'ClientDeleteResponse',
    'ClientSetResponsibleRequest',
    'ClientSetResponsibleResponse',
    'ClientMergeRequest',
    'ClientMergeResponse'
]

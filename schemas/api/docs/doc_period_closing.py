"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocPeriodClosing(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    close_date: int | None = PydField(default=None)
    run_date: int | None = PydField(default=None)
    status: str | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    description: str | None = PydField(default=None)
    scheduler_uuid: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)
    status_id: int | None = PydField(default=None)


class DocPeriodClosingAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    close_date: int | None = PydField(default=None)
    run_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)


class DocPeriodClosingCancelClose(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocPeriodClosingCheck(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    cash_servers: list[DocPeriodClosingCheckStageElement] | None = PydField(default=None)
    operating_cashes: list[DocPeriodClosingCheckStageElement] | None = PydField(default=None)
    copy_: bool | None = PydField(default=None, alias="copy")
    aggregation: bool | None = PydField(default=None)
    has_before_docs_in_work: bool | None = PydField(default=None)
    has_after_docs_done: bool | None = PydField(default=None)


class DocPeriodClosingCheckGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    firm_id: int | None = PydField(default=None)
    close_date: int | None = PydField(default=None)


class DocPeriodClosingCheckRegosOffsettedObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: DocPeriodClosingCheck | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocPeriodClosingCheckStageElement(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    name: str | None = PydField(default=None)
    status: bool | None = PydField(default=None)


class DocPeriodClosingColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocPeriodClosingColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocPeriodClosingColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class DocPeriodClosingDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocPeriodClosingEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    close_date: int | None = PydField(default=None)
    run_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    scheduler_uuid: str | None = PydField(default=None)


class DocPeriodClosingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    status_ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    sort_order: list[DocPeriodClosingColumn] | None = PydField(default=None)
    sort_orders: list[DocPeriodClosingColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocPeriodClosingRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocPeriodClosing] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, UpdateResult
from schemas.api.references.firm import Firm


DocPeriodClosingAddRequest: TypeAlias = DocPeriodClosingAdd
DocPeriodClosingAddResponse: TypeAlias = InsertResult
DocPeriodClosingCancelCloseRequest: TypeAlias = DocPeriodClosingCancelClose
DocPeriodClosingCancelCloseResponse: TypeAlias = UpdateResult
DocPeriodClosingDeleteRequest: TypeAlias = DocPeriodClosingDelete
DocPeriodClosingDeleteResponse: TypeAlias = UpdateResult
DocPeriodClosingEditRequest: TypeAlias = DocPeriodClosingEdit
DocPeriodClosingEditResponse: TypeAlias = UpdateResult
DocPeriodClosingGetRequest: TypeAlias = DocPeriodClosingGet
DocPeriodClosingGetResponse: TypeAlias = DocPeriodClosingRegosOffsettedArrayResult
DocPeriodClosingIsCanDoRequest: TypeAlias = DocPeriodClosingCheckGet
DocPeriodClosingIsCanDoResponse: TypeAlias = DocPeriodClosingCheckRegosOffsettedObjectResult


_MODEL_NAMES = ['DocPeriodClosing', 'DocPeriodClosingAdd', 'DocPeriodClosingCancelClose', 'DocPeriodClosingCheck', 'DocPeriodClosingCheckGet', 'DocPeriodClosingCheckRegosOffsettedObjectResult', 'DocPeriodClosingCheckStageElement', 'DocPeriodClosingColumn', 'DocPeriodClosingDelete', 'DocPeriodClosingEdit', 'DocPeriodClosingGet', 'DocPeriodClosingRegosOffsettedArrayResult']


__all__ = [
    'DocPeriodClosing',
    'DocPeriodClosingAdd',
    'DocPeriodClosingCancelClose',
    'DocPeriodClosingCheck',
    'DocPeriodClosingCheckGet',
    'DocPeriodClosingCheckRegosOffsettedObjectResult',
    'DocPeriodClosingCheckStageElement',
    'DocPeriodClosingColumn',
    'DocPeriodClosingColumns',
    'DocPeriodClosingDelete',
    'DocPeriodClosingEdit',
    'DocPeriodClosingGet',
    'DocPeriodClosingRegosOffsettedArrayResult',
    'DocPeriodClosingIsCanDoRequest',
    'DocPeriodClosingIsCanDoResponse',
    'DocPeriodClosingGetRequest',
    'DocPeriodClosingGetResponse',
    'DocPeriodClosingAddRequest',
    'DocPeriodClosingAddResponse',
    'DocPeriodClosingEditRequest',
    'DocPeriodClosingEditResponse',
    'DocPeriodClosingDeleteRequest',
    'DocPeriodClosingDeleteResponse',
    'DocPeriodClosingCancelCloseRequest',
    'DocPeriodClosingCancelCloseResponse'
]

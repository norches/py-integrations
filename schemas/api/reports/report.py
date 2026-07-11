"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Report(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    group: ReportGroup | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class Report0003Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    currency_ids: list[int] | None = PydField(default=None)
    in_base_currency: bool | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class Report0005Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)


class Report0006Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class Report0007Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class Report0009Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class Report0011CostTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0011_PeriodInterval(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class Report0011_Request_Model(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: str | None = PydField(default=None)
    end_date: str | None = PydField(default=None)
    start_date_: _DateTime | None = PydField(default=None, alias="_start_date")
    end_date_: _DateTime | None = PydField(default=None, alias="_end_date")
    start_date_unix: int | None = PydField(default=None)
    end_date_unix: int | None = PydField(default=None)
    item_group_ids: list[int] | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    type: Report0011_Type | None = PydField(default=None)
    period_interval: Report0011_PeriodInterval | None = PydField(default=None)
    cost_type: Report0011CostTypeEnum | None = PydField(default=None)


class Report0011_Type(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0016Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: Report0016_Type | None = PydField(default=None)
    data_type: Report0016_DataType | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    item_group_ids: list[int] | None = PydField(default=None)
    criterion_a: int | None = PydField(default=None)
    criterion_b: int | None = PydField(default=None)


class Report0016_DataType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class Report0016_Type(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0017Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: Report0017_Type | None = PydField(default=None)
    data_type: Report0017_DataType | None = PydField(default=None)
    interval: Report0017_PeriodInterval | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    item_group_ids: list[int] | None = PydField(default=None)
    criterion_x: int | None = PydField(default=None)
    criterion_y: int | None = PydField(default=None)


class Report0017_DataType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class Report0017_PeriodInterval(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class Report0017_Type(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0018Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    type: Report0018_Type | None = PydField(default=None)
    data_type: Report0018_DataType | None = PydField(default=None)
    interval: Report0018_PeriodInterval | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    item_group_ids: list[int] | None = PydField(default=None)
    criterion_x: int | None = PydField(default=None)
    criterion_y: int | None = PydField(default=None)
    criterion_a: int | None = PydField(default=None)
    criterion_b: int | None = PydField(default=None)


class Report0018_DataType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class Report0018_PeriodInterval(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class Report0018_Type(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0020CostTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0020GroupTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0020Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    cost_type: Report0020CostTypeEnum | None = PydField(default=None)
    group_type: Report0020GroupTypeEnum | None = PydField(default=None)


class Report0021CostTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0021GroupTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0021Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    report_type: Report0021TypeEnum | None = PydField(default=None)
    grouping: Report0021GroupTypeEnum | None = PydField(default=None)
    cost_type: Report0021CostTypeEnum | None = PydField(default=None)


class Report0021TypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0022Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    by_partner: bool | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)


class Report0023Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)


class Report0024CostTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0024GroupTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0024Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    sender_stock_id: int | None = PydField(default=None)
    price_type_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    cost_type: Report0024CostTypeEnum | None = PydField(default=None)
    group_type: Report0024GroupTypeEnum | None = PydField(default=None)


class Report0025CostTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0025TypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0025_Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: str | None = PydField(default=None)
    end_date: str | None = PydField(default=None)
    start_date_: _DateTime | None = PydField(default=None, alias="_start_date")
    end_date_: _DateTime | None = PydField(default=None, alias="_end_date")
    start_date_unix: int | None = PydField(default=None)
    end_date_unix: int | None = PydField(default=None)
    item_group_ids: list[int] | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    type: Report0025TypeEnum | None = PydField(default=None)
    cost_type: Report0025CostTypeEnum | None = PydField(default=None)


class Report0026CostTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0026TypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Report0026_Request(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: str | None = PydField(default=None)
    end_date: str | None = PydField(default=None)
    start_date_: _DateTime | None = PydField(default=None, alias="_start_date")
    end_date_: _DateTime | None = PydField(default=None, alias="_end_date")
    start_date_unix: int | None = PydField(default=None)
    end_date_unix: int | None = PydField(default=None)
    item_group_ids: list[int] | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    stock_ids: list[int] | None = PydField(default=None)
    type: Report0026TypeEnum | None = PydField(default=None)
    cost_type: Report0026CostTypeEnum | None = PydField(default=None)


class ReportAddRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    report_id: int | None = PydField(default=None)
    request_data: Any = PydField(default=None)


class ReportArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Report] | Error | None = PydField(default=None)


class ReportGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)
    group_ids: list[int] | None = PydField(default=None)


class ReportGroup(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    parent_id: int | None = PydField(default=None)
    name: str | None = PydField(default=None)
    name_var: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class ReportSetError(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    request_uuid: str | None = PydField(default=None)
    api_login: str | None = PydField(default=None)
    message: str | None = PydField(default=None)


class ReportSetPrepared(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    request_uuid: str | None = PydField(default=None)
    api_login: str | None = PydField(default=None)
    file: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error, Insert_uuid_Result, UpdateResult
from schemas.api.reports.report_prepared import ReportPreparedArrayRegosObjectResult, ReportPreparedGet, ReportPreparedRemove
from schemas.api.reports.report_request import ReportRequestArrayRegosObjectResult, ReportRequestGet


ReportAddRequestRequest: TypeAlias = ReportAddRequest
ReportAddRequestResponse: TypeAlias = Insert_uuid_Result
ReportGetPreparedRequest: TypeAlias = ReportPreparedGet
ReportGetPreparedResponse: TypeAlias = ReportPreparedArrayRegosObjectResult
ReportGetRequest: TypeAlias = ReportGet
ReportGetRequestRequest: TypeAlias = ReportRequestGet
ReportGetRequestResponse: TypeAlias = ReportRequestArrayRegosObjectResult
ReportGetResponse: TypeAlias = ReportArrayRegosObjectResult
ReportRemovePreparedRequest: TypeAlias = ReportPreparedRemove
ReportRemovePreparedResponse: TypeAlias = UpdateResult
ReportSetErrorRequest: TypeAlias = ReportSetError
ReportSetErrorResponse: TypeAlias = UpdateResult
ReportSetPreparedRequest: TypeAlias = ReportSetPrepared
ReportSetPreparedResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['Report', 'Report0003Request', 'Report0005Request', 'Report0006Request', 'Report0007Request', 'Report0009Request', 'Report0011_Request_Model', 'Report0016Request', 'Report0017Request', 'Report0018Request', 'Report0020Request', 'Report0021Request', 'Report0022Request', 'Report0023Request', 'Report0024Request', 'Report0025_Request', 'Report0026_Request', 'ReportAddRequest', 'ReportArrayRegosObjectResult', 'ReportGet', 'ReportGroup', 'ReportSetError', 'ReportSetPrepared']


__all__ = [
    'Report',
    'Report0003Request',
    'Report0005Request',
    'Report0006Request',
    'Report0007Request',
    'Report0009Request',
    'Report0011CostTypeEnum',
    'Report0011_PeriodInterval',
    'Report0011_Request_Model',
    'Report0011_Type',
    'Report0016Request',
    'Report0016_DataType',
    'Report0016_Type',
    'Report0017Request',
    'Report0017_DataType',
    'Report0017_PeriodInterval',
    'Report0017_Type',
    'Report0018Request',
    'Report0018_DataType',
    'Report0018_PeriodInterval',
    'Report0018_Type',
    'Report0020CostTypeEnum',
    'Report0020GroupTypeEnum',
    'Report0020Request',
    'Report0021CostTypeEnum',
    'Report0021GroupTypeEnum',
    'Report0021Request',
    'Report0021TypeEnum',
    'Report0022Request',
    'Report0023Request',
    'Report0024CostTypeEnum',
    'Report0024GroupTypeEnum',
    'Report0024Request',
    'Report0025CostTypeEnum',
    'Report0025TypeEnum',
    'Report0025_Request',
    'Report0026CostTypeEnum',
    'Report0026TypeEnum',
    'Report0026_Request',
    'ReportAddRequest',
    'ReportArrayRegosObjectResult',
    'ReportGet',
    'ReportGroup',
    'ReportSetError',
    'ReportSetPrepared',
    'ReportGetRequest',
    'ReportGetResponse',
    'ReportGetRequestRequest',
    'ReportGetRequestResponse',
    'ReportAddRequestRequest',
    'ReportAddRequestResponse',
    'ReportGetPreparedRequest',
    'ReportGetPreparedResponse',
    'ReportRemovePreparedRequest',
    'ReportRemovePreparedResponse',
    'ReportSetPreparedRequest',
    'ReportSetPreparedResponse',
    'ReportSetErrorRequest',
    'ReportSetErrorResponse'
]

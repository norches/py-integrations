"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class BatchRequest(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    stop_on_error: bool | None = PydField(default=None)
    requests: list[BatchStep] | None = PydField(default=None)


class BatchResponse(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    responses: list[BatchStepResponse] | None = PydField(default=None)


class BatchResponseRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: BatchResponse | Error | None = PydField(default=None)


class BatchStep(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    key: str | None = PydField(default=None)
    path: str | None = PydField(default=None)
    payload: Any = PydField(default=None)


class BatchStepResponse(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    key: str | None = PydField(default=None)
    status: int | None = PydField(default=None)
    response: Any = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error


BatchBatchRequest: TypeAlias = BatchRequest
BatchBatchResponse: TypeAlias = BatchResponseRegosObjectResult


_MODEL_NAMES = ['BatchRequest', 'BatchResponse', 'BatchResponseRegosObjectResult', 'BatchStep', 'BatchStepResponse']


__all__ = [
    'BatchRequest',
    'BatchResponse',
    'BatchResponseRegosObjectResult',
    'BatchStep',
    'BatchStepResponse',
    'BatchBatchRequest',
    'BatchBatchResponse'
]

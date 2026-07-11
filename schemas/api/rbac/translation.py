"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Translation(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    variable: str | None = PydField(default=None)
    variable_value: str | None = PydField(default=None)
    value: str | None = PydField(default=None)
    translate_value: str | None = PydField(default=None)


class TranslationArrayRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Translation] | Error | None = PydField(default=None)


class TranslationGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    language_code: str | None = PydField(default=None)


class TranslationShort(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    variable_value: str | None = PydField(default=None)
    translate_value: str | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.rbac.language import LanguageTranslationDataRegosObjectResult


TranslationGetRequest: TypeAlias = TranslationGet
TranslationGetResponse: TypeAlias = TranslationArrayRegosObjectResult
TranslationGetTranslationPacketRequest: TypeAlias = TranslationGet
TranslationGetTranslationPacketResponse: TypeAlias = LanguageTranslationDataRegosObjectResult


_MODEL_NAMES = ['Translation', 'TranslationArrayRegosObjectResult', 'TranslationGet', 'TranslationShort']


__all__ = [
    'Translation',
    'TranslationArrayRegosObjectResult',
    'TranslationGet',
    'TranslationShort',
    'TranslationGetRequest',
    'TranslationGetResponse',
    'TranslationGetTranslationPacketRequest',
    'TranslationGetTranslationPacketResponse'
]

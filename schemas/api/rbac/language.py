"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class Language(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    code2: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    short_name: str | None = PydField(default=None)
    version: str | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class LanguageRegosArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[Language] | Error | None = PydField(default=None)


class LanguageTranslationData(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    code: str | None = PydField(default=None)
    version: int | None = PydField(default=None)
    data: list[TranslationShort] | None = PydField(default=None)


class LanguageTranslationDataRegosObjectResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: LanguageTranslationData | Error | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import Error
from schemas.api.rbac.translation import TranslationShort


LanguageGetResponse: TypeAlias = LanguageRegosArrayResult


_MODEL_NAMES = ['Language', 'LanguageRegosArrayResult', 'LanguageTranslationData', 'LanguageTranslationDataRegosObjectResult']


__all__ = [
    'Language',
    'LanguageRegosArrayResult',
    'LanguageTranslationData',
    'LanguageTranslationDataRegosObjectResult',
    'LanguageGetResponse'
]

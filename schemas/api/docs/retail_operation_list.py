"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocRetailSaleExt(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    status: DocChequeStatusEnum | None = PydField(default=None)
    session: DocCashSession | None = PydField(default=None)
    cashier: User | None = PydField(default=None)
    is_return: bool | None = PydField(default=None)
    seller: User | None = PydField(default=None)
    return_reason: RetailReturnReason | None = PydField(default=None)
    card: RetailCard | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    agregate_status: AgregateStatusEnum | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailOperationList(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    uuid: str | None = PydField(default=None)
    has_storno: bool | None = PydField(default=None)
    storno_uuid: str | None = PydField(default=None)
    document: DocRetailSaleExt | None = PydField(default=None)
    stock_id: int | None = PydField(default=None)
    item: Item | None = PydField(default=None)
    order: int | None = PydField(default=None)
    quantity: _Decimal | None = PydField(default=None)
    price: _Decimal | None = PydField(default=None)
    price2: _Decimal | None = PydField(default=None)
    promo_id: int | None = PydField(default=None)
    vat_value: _Decimal | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class RetailOperationListGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    operating_cash_ids: list[int] | None = PydField(default=None)
    retail_card_ids: list[int] | None = PydField(default=None)
    customer_ids: list[int] | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class RetailOperationListRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[RetailOperationList] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import AgregateStatusEnum, Error
from schemas.api.docs.doc_cash_session import DocCashSession
from schemas.api.docs.doc_cheque import DocChequeStatusEnum
from schemas.api.rbac.user import User
from schemas.api.references.item import Item
from schemas.api.references.retail_card import RetailCard
from schemas.api.references.retail_return_reason import RetailReturnReason


RetailOperationListGetRequest: TypeAlias = RetailOperationListGet
RetailOperationListGetResponse: TypeAlias = RetailOperationListRegosOffsettedArrayResult


_MODEL_NAMES = ['DocRetailSaleExt', 'RetailOperationList', 'RetailOperationListGet', 'RetailOperationListRegosOffsettedArrayResult']


__all__ = [
    'DocRetailSaleExt',
    'RetailOperationList',
    'RetailOperationListGet',
    'RetailOperationListRegosOffsettedArrayResult',
    'RetailOperationListGetRequest',
    'RetailOperationListGetResponse'
]

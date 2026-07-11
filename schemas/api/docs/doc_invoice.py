"""REGOS API schemas."""
# Generated from REGOS public Swagger by tools/generate_regos_public_api.py.

from __future__ import annotations

from datetime import datetime as _DateTime
from decimal import Decimal as _Decimal
from enum import IntEnum
from typing import Any, TypeAlias

from pydantic import ConfigDict, Field as PydField, RootModel

from schemas.api.common.base import RegosModel


class DocInvoice(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    invoice_type: DocInvoiceTypeEnum | None = PydField(default=None)
    corrected_date: int | None = PydField(default=None)
    corrected_code: str | None = PydField(default=None)
    contract: DocContractShort | None = PydField(default=None)
    firm: Firm | None = PydField(default=None)
    partner: Partner | None = PydField(default=None)
    currency: Currency | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user: User | None = PydField(default=None)
    base_document_id: int | None = PydField(default=None)
    document_type: int | None = PydField(default=None)
    description: str | None = PydField(default=None)
    uuid: str | None = PydField(default=None)
    external_code: str | None = PydField(default=None)
    status: DocInvoiceStatusEnum | None = PydField(default=None)
    error: str | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    current_user_blocked: bool | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    last_update: int | None = PydField(default=None)


class DocInvoiceAdd(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    corrected_date: int | None = PydField(default=None)
    corrected_code: str | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    document_type_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    invoice_type: DocInvoiceTypeEnum | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocInvoiceAddOnBase(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_type_id: int | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    date: int | None = PydField(default=None)
    corrected_date: int | None = PydField(default=None)
    corrected_code: str | None = PydField(default=None)
    description: str | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocInvoiceColumn(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    column: DocInvoiceColumns | None = PydField(default=None)
    direction: ColumnSortOrderDirection | None = PydField(default=None)


class DocInvoiceColumns(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15


class DocInvoiceDelete(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInvoiceDeleteMark(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInvoiceEdit(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)
    date: int | None = PydField(default=None)
    code: str | None = PydField(default=None)
    corrected_date: int | None = PydField(default=None)
    corrected_code: str | None = PydField(default=None)
    document_id: int | None = PydField(default=None)
    document_type_id: int | None = PydField(default=None)
    contract_id: int | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)
    partner_id: int | None = PydField(default=None)
    currency_id: int | None = PydField(default=None)
    exchange_rate: _Decimal | None = PydField(default=None)
    description: str | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    attached_user_id: int | None = PydField(default=None)


class DocInvoiceFromRoaming(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    id: str | None = PydField(default=None)
    roaming_id: str | None = PydField(default=None)
    name: str | None = PydField(default=None)
    partner_name: str | None = PydField(default=None)
    partner_inn: str | None = PydField(default=None)
    contract: str | None = PydField(default=None)
    firm: str | None = PydField(default=None)
    date: _DateTime | None = PydField(default=None)
    create_date: _DateTime | None = PydField(default=None)
    update_date: _DateTime | None = PydField(default=None)
    amount: _Decimal | None = PydField(default=None)


class DocInvoiceFromRoamingGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    firm_id: int | None = PydField(default=None)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocInvoiceFromRoamingImport(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: str | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class DocInvoiceFromRoamingRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocInvoiceFromRoaming] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocInvoiceGet(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    start_date: int | None = PydField(default=None)
    end_date: int | None = PydField(default=None)
    invoice_type: DocInvoiceTypeEnum | None = PydField(default=None)
    ids: list[int] | None = PydField(default=None)
    contract_ids: list[int] | None = PydField(default=None)
    firm_ids: list[int] | None = PydField(default=None)
    partner_ids: list[int] | None = PydField(default=None)
    external_code: str | None = PydField(default=None)
    attached_user_ids: list[int] | None = PydField(default=None)
    performed: bool | None = PydField(default=None)
    blocked: bool | None = PydField(default=None)
    deleted_mark: bool | None = PydField(default=None)
    vat_calculation_type: VatCalculationTypeEnum | None = PydField(default=None)
    sort_orders: list[DocInvoiceColumn] | None = PydField(default=None)
    search: str | None = PydField(default=None)
    limit: int | None = PydField(default=None)
    offset: int | None = PydField(default=None)


class DocInvoiceLockAndUnlock(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    ids: list[int] | None = PydField(default=None)


class DocInvoicePerformAndCancel(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    id: int | None = PydField(default=None)


class DocInvoiceRegosOffsettedArrayResult(RegosModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    ok: bool | None = PydField(default=None)
    result: list[DocInvoice] | Error | None = PydField(default=None)
    next_offset: int | None = PydField(default=None)
    total: int | None = PydField(default=None)


class DocInvoiceSend(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_ids: list[int] | None = PydField(default=None)
    firm_id: int | None = PydField(default=None)


class DocInvoiceSetExternalData(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    integration_key: str | None = PydField(default=None)
    connected_integration_id: str | None = PydField(default=None)
    external_id: str | None = PydField(default=None)
    roaming_id: str | None = PydField(default=None)


class DocInvoiceSetStatus(RegosModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)
    document_id: int | None = PydField(default=None)
    status: DocInvoiceStatusEnum | None = PydField(default=None)
    error_message: str | None = PydField(default=None)


class DocInvoiceStatusEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DocInvoiceTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


# Imports are intentionally placed after model definitions to avoid circular imports.
from schemas.api.common.base import ColumnSortOrderDirection, Error, InsertResult, SingleObjectResult, UpdateResult, VatCalculationTypeEnum
from schemas.api.docs.doc_contract import DocContractShort
from schemas.api.rbac.user import User
from schemas.api.references.currency import Currency
from schemas.api.references.firm import Firm
from schemas.api.references.partner import Partner


DocInvoiceActionResponse: TypeAlias = SingleObjectResult
DocInvoiceAddOnBaseRequest: TypeAlias = DocInvoiceAddOnBase
DocInvoiceAddOnBaseResponse: TypeAlias = InsertResult
DocInvoiceAddRequest: TypeAlias = DocInvoiceAdd
DocInvoiceAddResponse: TypeAlias = InsertResult
DocInvoiceDeleteMarkRequest: TypeAlias = DocInvoiceDeleteMark
DocInvoiceDeleteMarkResponse: TypeAlias = UpdateResult
DocInvoiceDeleteRequest: TypeAlias = DocInvoiceDelete
DocInvoiceDeleteResponse: TypeAlias = UpdateResult
DocInvoiceEditRequest: TypeAlias = DocInvoiceEdit
DocInvoiceEditResponse: TypeAlias = UpdateResult
DocInvoiceGetDocumentsFromRoamingRequest: TypeAlias = DocInvoiceFromRoamingGet
DocInvoiceGetDocumentsFromRoamingResponse: TypeAlias = DocInvoiceFromRoamingRegosOffsettedArrayResult
DocInvoiceGetRequest: TypeAlias = DocInvoiceGet
DocInvoiceGetResponse: TypeAlias = DocInvoiceRegosOffsettedArrayResult
DocInvoiceImportDocumentFromRoamingRequest: TypeAlias = DocInvoiceFromRoamingImport
DocInvoiceImportDocumentFromRoamingResponse: TypeAlias = SingleObjectResult
DocInvoiceLockRequest: TypeAlias = DocInvoiceLockAndUnlock
DocInvoiceLockResponse: TypeAlias = UpdateResult
DocInvoicePerformCancelRequest: TypeAlias = DocInvoicePerformAndCancel
DocInvoicePerformCancelResponse: TypeAlias = UpdateResult
DocInvoicePerformRequest: TypeAlias = DocInvoicePerformAndCancel
DocInvoicePerformResponse: TypeAlias = UpdateResult
DocInvoiceSendRequest: TypeAlias = DocInvoiceSend
DocInvoiceSendResponse: TypeAlias = SingleObjectResult
DocInvoiceSetExternalDataRequest: TypeAlias = DocInvoiceSetExternalData
DocInvoiceSetExternalDataResponse: TypeAlias = SingleObjectResult
DocInvoiceSetStatusRequest: TypeAlias = DocInvoiceSetStatus
DocInvoiceSetStatusResponse: TypeAlias = SingleObjectResult
DocInvoiceStatus: TypeAlias = DocInvoiceStatusEnum
DocInvoiceType: TypeAlias = DocInvoiceTypeEnum
DocInvoiceUnlockRequest: TypeAlias = DocInvoiceLockAndUnlock
DocInvoiceUnlockResponse: TypeAlias = UpdateResult


_MODEL_NAMES = ['DocInvoice', 'DocInvoiceAdd', 'DocInvoiceAddOnBase', 'DocInvoiceColumn', 'DocInvoiceDelete', 'DocInvoiceDeleteMark', 'DocInvoiceEdit', 'DocInvoiceFromRoaming', 'DocInvoiceFromRoamingGet', 'DocInvoiceFromRoamingImport', 'DocInvoiceFromRoamingRegosOffsettedArrayResult', 'DocInvoiceGet', 'DocInvoiceLockAndUnlock', 'DocInvoicePerformAndCancel', 'DocInvoiceRegosOffsettedArrayResult', 'DocInvoiceSend', 'DocInvoiceSetExternalData', 'DocInvoiceSetStatus']


__all__ = [
    'DocInvoice',
    'DocInvoiceAdd',
    'DocInvoiceAddOnBase',
    'DocInvoiceColumn',
    'DocInvoiceColumns',
    'DocInvoiceDelete',
    'DocInvoiceDeleteMark',
    'DocInvoiceEdit',
    'DocInvoiceFromRoaming',
    'DocInvoiceFromRoamingGet',
    'DocInvoiceFromRoamingImport',
    'DocInvoiceFromRoamingRegosOffsettedArrayResult',
    'DocInvoiceGet',
    'DocInvoiceLockAndUnlock',
    'DocInvoicePerformAndCancel',
    'DocInvoiceRegosOffsettedArrayResult',
    'DocInvoiceSend',
    'DocInvoiceSetExternalData',
    'DocInvoiceSetStatus',
    'DocInvoiceStatusEnum',
    'DocInvoiceTypeEnum',
    'DocInvoiceGetRequest',
    'DocInvoiceGetResponse',
    'DocInvoiceAddRequest',
    'DocInvoiceAddResponse',
    'DocInvoiceAddOnBaseRequest',
    'DocInvoiceAddOnBaseResponse',
    'DocInvoiceEditRequest',
    'DocInvoiceEditResponse',
    'DocInvoiceDeleteMarkRequest',
    'DocInvoiceDeleteMarkResponse',
    'DocInvoiceDeleteRequest',
    'DocInvoiceDeleteResponse',
    'DocInvoiceLockRequest',
    'DocInvoiceLockResponse',
    'DocInvoiceUnlockRequest',
    'DocInvoiceUnlockResponse',
    'DocInvoicePerformRequest',
    'DocInvoicePerformResponse',
    'DocInvoicePerformCancelRequest',
    'DocInvoicePerformCancelResponse',
    'DocInvoiceSendRequest',
    'DocInvoiceSendResponse',
    'DocInvoiceImportDocumentFromRoamingRequest',
    'DocInvoiceImportDocumentFromRoamingResponse',
    'DocInvoiceSetStatusRequest',
    'DocInvoiceSetStatusResponse',
    'DocInvoiceSetExternalDataRequest',
    'DocInvoiceSetExternalDataResponse',
    'DocInvoiceGetDocumentsFromRoamingRequest',
    'DocInvoiceGetDocumentsFromRoamingResponse',
    'DocInvoiceActionResponse',
    'DocInvoiceStatus',
    'DocInvoiceType'
]

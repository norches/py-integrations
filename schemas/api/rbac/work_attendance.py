from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field as PydField

from schemas.api.base import APIBaseResponse, BaseSchema


class WorkAttendanceStatusRequest(BaseSchema):
    """Параметры запроса текущего статуса посещаемости сотрудника."""

    model_config = ConfigDict(extra="forbid")

    user_id: int = PydField(..., ge=1, description="ID пользователя (сотрудника).")


class WorkUserAvailability(BaseSchema):
    """Доступность сотрудника по данным учёта рабочего времени (WorkAttendance/Status).

    Признак "на смене и доступен" определяется булевыми флагами is_checked_in /
    is_in_shift / is_on_break. Целочисленный ``status`` оставлен как есть, потому что
    публичный Swagger не раскрывает его именованные значения.
    """

    model_config = ConfigDict(extra="ignore")

    # Optional on purpose: the response body is undocumented in the public Swagger,
    # so a present-but-partial 200 must still parse and fall through to the boolean
    # availability check rather than raising and being swallowed as "available".
    user_id: Optional[int] = PydField(default=None, ge=1, description="ID пользователя.")
    status: Optional[int] = PydField(
        default=None, description="Код статуса доступности (значения не документированы)."
    )
    is_in_shift: Optional[bool] = PydField(
        default=None, description="Сотрудник находится в пределах рабочей смены."
    )
    is_checked_in: Optional[bool] = PydField(
        default=None, description="Сотрудник отметился о приходе (открыта смена)."
    )
    is_on_break: Optional[bool] = PydField(
        default=None, description="Сотрудник сейчас на перерыве."
    )
    active_session_id: Optional[int] = PydField(
        default=None, description="ID активной сессии посещаемости."
    )
    active_break_id: Optional[int] = PydField(
        default=None, description="ID активного перерыва."
    )
    next_shift_start_date: Optional[int] = PydField(
        default=None, description="Начало ближайшей смены (unixtime, сек)."
    )
    next_shift_end_date: Optional[int] = PydField(
        default=None, description="Окончание ближайшей смены (unixtime, сек)."
    )
    last_update: Optional[int] = PydField(
        default=None, description="Метка последнего обновления (unixtime, сек)."
    )


class WorkAttendanceStatusResponse(APIBaseResponse[WorkUserAvailability]):
    """Ответ WorkAttendance/Status."""

    model_config = ConfigDict(extra="ignore")


__all__ = [
    "WorkAttendanceStatusRequest",
    "WorkUserAvailability",
    "WorkAttendanceStatusResponse",
]

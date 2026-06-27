from __future__ import annotations

from core.logger import setup_logger
from schemas.api.rbac.work_attendance import (
    WorkAttendanceStatusRequest,
    WorkAttendanceStatusResponse,
)

logger = setup_logger("rbac.WorkAttendance")


class WorkAttendanceService:
    """Сервис учёта рабочего времени (статус посещаемости/смены сотрудника)."""

    PATH_STATUS = "WorkAttendance/Status"

    def __init__(self, api):
        self.api = api

    async def status(
        self, req: WorkAttendanceStatusRequest
    ) -> WorkAttendanceStatusResponse:
        """Возвращает текущий статус посещаемости пользователя."""

        return await self.api.call(self.PATH_STATUS, req, WorkAttendanceStatusResponse)

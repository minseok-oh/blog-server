from datetime import datetime

from pydantic import BaseModel


class SchedulesReadDTO(BaseModel):
    scheduleId: int
    title: str
    started_at: datetime
    ended_at: datetime
    color: str

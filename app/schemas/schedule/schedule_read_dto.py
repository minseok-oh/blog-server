from datetime import datetime

from pydantic import BaseModel


class ScheduleReadDTO(BaseModel):
    title: str
    content: str
    started_at: datetime
    ended_at: datetime

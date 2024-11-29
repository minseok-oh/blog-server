from pydantic import BaseModel


class ScheduleCreateDTO(BaseModel):
    title: str
    content: str
    started_at: str
    ended_at: str
    color: str

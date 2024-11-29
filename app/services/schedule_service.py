from datetime import datetime

from sqlalchemy.orm import Session

from app.crud import schedule_crud
from app.domains.schedule import Schedule


def create_schedule(db: Session, title: str, content: str, started_at: datetime, ended_at: datetime, color: str,
                    user_id: int) -> None:
    schedule = Schedule(
        title=title,
        content=content,
        member_id=user_id,
        started_at=started_at,
        ended_at=ended_at,
        color=color
    )
    schedule_crud.create_schedule(db=db, schedule=schedule)

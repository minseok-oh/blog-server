from sqlalchemy.orm import Session

from app.domains.schedule import Schedule
from app.models.schedule_entity import ScheduleEntity


def create_schedule(db: Session, schedule: Schedule) -> None:
    schedule_entity = ScheduleEntity(
        title=schedule.title,
        content=schedule.content,
        member_id=schedule.member_id,
        started_at=schedule.started_at,
        ended_at=schedule.ended_at,
        color=schedule.color
    )
    db.add(schedule_entity)
    db.commit()

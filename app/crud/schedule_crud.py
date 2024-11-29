from sqlalchemy.orm import Session

from app.domains.schedule import Schedule
from app.mapper import convert_to_schedule
from app.models.schedule_entity import ScheduleEntity
from app.models.user_entity import UserEntity


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


def get_schedules(db: Session) -> list:
    schedule_entities = db.query(ScheduleEntity).all()
    return [convert_to_schedule(schedule_entity) for schedule_entity in schedule_entities]


def get_schedule_by_id(db: Session, schedule_id: int) -> Schedule:
    schedule_entity = (
        db.query(ScheduleEntity, UserEntity.nickname.label("nickname"))
        .join(UserEntity, ScheduleEntity.member_id == UserEntity.id)
        .filter(ScheduleEntity.id == schedule_id)
        .first()
    )

    schedule, member_name = schedule_entity
    return convert_to_schedule(
        Schedule(
            schedule.id,
            schedule.title,
            schedule.content,
            member_name,
            schedule.started_at,
            schedule.ended_at,
            schedule.color
        )
    )

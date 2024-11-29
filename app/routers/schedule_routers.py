from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.schemas.schedule.schedule_create_dto import ScheduleCreateDTO
from app.schemas.schedule.schedules_read_dto import SchedulesReadDTO
from app.services import schedule_service
from databases import get_db

router = APIRouter(prefix='/api/schedules')


@router.post('/')
def create_schedule(request: Request, schedule: ScheduleCreateDTO, db: Session = Depends(get_db)) -> None:
    user = request.state.user
    schedule_service.create_schedule(db=db, title=schedule.title, content=schedule.content,
                                     started_at=schedule.started_at, ended_at=schedule.ended_at, color=schedule.color,
                                     user_id=user['user_id'])


@router.get('/')
def get_schedules(db: Session = Depends(get_db)) -> list:
    schedules = schedule_service.get_schedules(db=db)
    return [SchedulesReadDTO(scheduleId=schedule.id, title=schedule.title, started_at=schedule.started_at,
                             ended_at=schedule.ended_at, color=schedule.color) for schedule in schedules]

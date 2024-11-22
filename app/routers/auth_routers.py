from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_create_dto import UserCreateDTO
from app.services.user_service import create_user
from databases import get_db

router = APIRouter(prefix='/api/auth')


@router.post('/sign-up')
def sign_up(request: UserCreateDTO, db: Session = Depends(get_db)):
    create_user(db, request.userId, request.password, request.email,
                request.username, request.birth, request.phone)

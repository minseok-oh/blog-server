from uuid import uuid4

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.schemas.sign_in_dto import SignInDTO
from app.schemas.user_create_dto import UserCreateDTO
from app.services import auth_service
from app.services.user_service import create_user
from app.util.session_store import SessionStore
from databases import get_db

router = APIRouter(prefix='/api/auth')


@router.post('/sign-up')
def sign_up(request: UserCreateDTO, db: Session = Depends(get_db)) -> None:
    create_user(db, request.userId, request.password, request.email,
                request.username, request.birth, request.phone)


@router.post('/sign-in')
def sign_in(request: SignInDTO, response: Response, db: Session = Depends(get_db)) -> None:
    user_id = auth_service.sign_in(request.userId, request.password, db)
    session_id = str(uuid4())

    SessionStore.save(session_id, user_id)
    response.set_cookie(
        key="sid",
        value=session_id,
        max_age=3600,
        httponly=True,
        samesite="Strict"
    )

import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import user_crud
from app.schemas.sign_in_info_dto import SignInInfoDTO


def sign_in(user_id: str, password: str, db: Session) -> SignInInfoDTO:
    user = user_crud.get_user_by_member_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="존재하지 않는 사용자입니다."
        )

    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(
            status_code=401,
            detail="비밀번호가 일치하지 않습니다."
        )

    return SignInInfoDTO(user_id=user.id, username=user.name, role=user.role)

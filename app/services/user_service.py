import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.user_crud import get_user_by_student_number
from app.domains.user import User


def validate_duplicate_user(db: Session, student_number: str) -> None:
    """
    중복된 회원이 있는지 확인하는 함수.
    """
    existing_user = get_user_by_student_number(db, student_number)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="이미 가입된 회원입니다."
        )


def encrypt_password(user: User):
    """
    암호화된 비밀번호를 갖는 UserEntity 리턴하는 함수.
    솔트는 중간 중간에 랜덤으로 문자열을 넣는 것이다.
    """
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    return user

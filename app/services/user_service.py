from datetime import datetime

import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import user_crud
from app.crud.user_crud import delete_user_by_id, get_user_by_member_id
from app.domains.user import User


def create_user(db: Session, userId: str, nickname: str, password: str, email: str, username: str, birth: datetime,
                phone: str) -> None:
    """
    사용자를 생성하는 함수.
    """
    validate_duplicate_user(db, userId)
    validate_duplicate_nickname(db, nickname)
    user = User(
        id=userId,
        name=username,
        nickname=nickname,
        member_id=userId,
        password=password,
        role="guest",
        avatar="",
        phone_number=phone,
        student_number=userId,
        birth=birth,
        email=email
    )
    encrypted_user = encrypt_password(user=user)
    user_crud.create_user(db, encrypted_user)


def validate_duplicate_user(db: Session, user_id: str) -> None:
    """
    중복된 회원이 있는지 확인하는 함수.
    """
    existing_user = get_user_by_member_id(db, user_id)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="이미 가입된 회원입니다."
        )


def validate_duplicate_nickname(db: Session, nickname: str) -> None:
    """
    중복된 닉네임이 있는지 확인하는 함수.
    """
    existing_user = user_crud.get_user_by_nickname(db, nickname)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="이미 존재하는 닉네임입니다."
        )

def encrypt_password(user: User):
    """
    암호화된 비밀번호를 갖는 UserEntity 리턴하는 함수.
    솔트는 중간 중간에 랜덤으로 문자열을 넣는 것이다.
    """
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    return user


def withdraw_user(db: Session, user_id: int) -> None:
    """
    회원 탈퇴를 진행하는 메서드

    @:param db: 데이터베이스 세션
    @:param user_id: 탈퇴할 사용자의 ID
    """
    delete_user_by_id(db, user_id)

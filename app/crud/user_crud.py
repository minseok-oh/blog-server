from sqlalchemy.orm import Session

from app.domains.user import User
from app.mapper import convert_to_user
from app.models.user_entity import UserEntity


def get_user_by_student_number(db: Session, student_number: str) -> User:
    user_entity = db.query(UserEntity).filter(UserEntity.student_number == student_number).first()
    return convert_to_user(user_entity) if user_entity else None


def create_user(db: Session, user: User) -> None:
    user_entity = UserEntity(name=user.name, member_id=user.member_id, password=user.password,
                             role=user.role, avatar=user.avatar, phone_number=user.phone_number,
                             student_number=user.student_number, birth=user.birth, email=user.email)
    db.add(user_entity)
    db.commit()


def get_user_by_id(db: Session, id: int) -> User:
    """
    id를 이용하여 id에 해당하는 User를 찾습니다.
    """
    user_entity = db.query(UserEntity).filter(UserEntity.id == id).first()
    return convert_to_user(user_entity) if user_entity else None


def get_user_by_member_id(db: Session, member_id: str) -> User:
    """
    email을 이용하여 member_id에 해당하는 User를 찾습니다.
    """
    user_entity = db.query(UserEntity).filter(UserEntity.member_id == member_id).first()
    return convert_to_user(user_entity) if user_entity else None


def delete_user_by_id(db: Session, id: int) -> None:
    user = db.query(UserEntity).filter(UserEntity.id == id).first()
    if user:
        db.delete(user)
        db.commit()

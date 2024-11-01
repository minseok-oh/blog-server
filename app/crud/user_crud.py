import bcrypt
from sqlalchemy.orm import Session

from app.domains.user import User
from app.mapper import convert_to_user
from app.models.user_entity import UserEntity


def create_user(db: Session, user: User):
    user_entity = UserEntity(name=user.name, member_id=user.member_id, password=user.password,
                             role=user.role, avatar=user.avatar, phone_number=user.phone_number,
                             student_number=user.student_number, birth=user.birth, email=user.email)
    return db.add(user_entity)


def get_user_by_id(db: Session, id: int) -> User:
    """
    id를 이용하여 id에 해당하는 User를 찾습니다.
    """
    user_entity = db.query(UserEntity).filter(UserEntity.id == id).first()
    return convert_to_user(user_entity) if user_entity else None

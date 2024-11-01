import bcrypt
from sqlalchemy.orm import Session

from app.domains.user import User
from app.mapper import convert_to_user
from app.models.user_entity import UserEntity


def get_user_by_id(db: Session, id: int) -> User:
    """
    id를 이용하여 id에 해당하는 User를 찾습니다.
    """
    user_entity = db.query(UserEntity).filter(UserEntity.id == id).first()
    return convert_to_user(user_entity) if user_entity else None

def encrypt_password(user : UserEntity):
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    return user

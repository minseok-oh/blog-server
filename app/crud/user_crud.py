from sqlalchemy.orm import Session

from app.entity.user_entity import UserEntity


def get_user_by_id(db: Session, id):
    return db.query(UserEntity).filter(UserEntity.id == id).first()
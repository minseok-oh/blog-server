from config.db_config import SessionLocal, Base, engine

from app.entity.comment_entity import CommentEntity
from app.entity.post_entity import PostEntity
from app.entity.user_entity import UserEntity


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)

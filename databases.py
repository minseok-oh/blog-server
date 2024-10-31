from config.db_config import SessionLocal, Base, engine

from app.models.comment_entity import CommentEntity
from app.models.post_entity import PostEntity
from app.models.user_entity import UserEntity


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)

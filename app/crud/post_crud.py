from datetime import datetime

from sqlalchemy.orm import Session

from app.domains.post import Post
from app.mapper import convert_to_post
from app.models.post_entity import PostEntity


def create_post(db: Session, post: Post) -> Post:
    post_entity = PostEntity(
        title=post.title,
        content=post.content,
        member_id=post.member_id,
        board_id=post.board_id,
        created_at=post.created_at,
    )
    db.add(post_entity)
    db.commit()


def get_post_by_id(db: Session, post_id: int) -> Post:
    post_entity = db.query(PostEntity).filter(PostEntity.id == post_id).first()
    return convert_to_post(post_entity)


def get_posts_by_board_id(db: Session, board_id: int, page: int = 1) -> list[Post]:
    # TODO: 추후 User, Board이 완료되면 테스트 코드 작성
    offset = (page - 1) * 10
    post_entities = (
        db.query(PostEntity)
        .filter(PostEntity.board_id == board_id)
        .order_by(PostEntity.created_at.desc())
        .offset(offset)
        .limit(10)
        .all()
    )
    return [convert_to_post(post_entity) for post_entity in post_entities]


def update_post(db: Session, title: str, content: str, post_id: int) -> None:
    post_entity = db.query(PostEntity).filter(PostEntity.id == post_id).first()
    post_entity.title = title
    post_entity.content = content
    post_entity.created_at = datetime.now()
    db.commit()

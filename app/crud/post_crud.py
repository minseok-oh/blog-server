from sqlalchemy.orm import Session

from app.domains.post import Post
from app.mapper import convert_to_post
from app.models.post_entity import PostEntity


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

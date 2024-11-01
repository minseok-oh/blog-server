from sqlalchemy.orm import Session

from app.domains.comment import Comment
from app.mapper import convert_to_comment
from app.models.comment_entity import CommentEntity


def get_comments_by_post_id(db: Session, post_id: int, page: int = 1) -> list[Comment]:
    # TODO: 추후 User, Board, Post이 완료되면 테스트 코드 작성
    offset = (page - 1) * 10
    comment_entities = (
        db.query(CommentEntity)
        .filter(CommentEntity.post_id == post_id)
        .order_by(CommentEntity.created_at.asc())
        .offset(offset)
        .limit(10)
        .all()
    )
    return [convert_to_comment(comment_entity) for comment_entity in comment_entities]

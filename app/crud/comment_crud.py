from sqlalchemy.orm import Session

from app.models.comment_entity import CommentEntity
from app.schemas.comments_read_dto import CommentsReadDTO


def get_comments_by_post_id(db: Session, post_id: int, page: int = 1) -> list[CommentsReadDTO]:
    # TODO: 추후 User, Board, Post이 완료되면 테스트 코드 작성
    offset = (page - 1) * 10
    comments = (
        db.query(CommentEntity)
        .filter(CommentEntity.post_id == post_id)
        .order_by(CommentEntity.created_at.asc())
        .offset(offset)
        .limit(10)
        .all()
    )

    comments_read_dto = [CommentsReadDTO(comment) for comment in comments]
    return comments_read_dto
from sqlalchemy.orm import Session

from app.domains.comment import Comment
from app.mapper import convert_to_comment
from app.models.comment_entity import CommentEntity


def create_comment(db: Session, comment: Comment):
    comment_entity = CommentEntity(
        user_id=comment.user_id,
        post_id=comment.post_id,
        content=comment.content,
        parent_id=comment.parent_id,
        created_at=comment.created_at,
    )
    db.add(comment_entity)
    db.commit()


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


def get_comments_by_id(comment_id: int, db: Session) -> Comment:
    comment_entity = db.query(CommentEntity).get(comment_id)
    return convert_to_comment(comment_entity)


def update_comment(db: Session, comment: Comment):
    comment_entity = db.query(CommentEntity).get(comment.id)
    comment_entity.content = comment.content
    comment_entity.created_at = comment.created_at
    db.commit()

from sqlalchemy.orm import Session

from app.domains.comment import Comment
from app.mapper import convert_to_comment
from app.models.comment_entity import CommentEntity
from app.models.user_entity import UserEntity


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


def get_comments_by_post_id(db: Session, post_id: int) -> list[Comment]:
    saved_comment_entities = (
        db.query(CommentEntity, UserEntity.name.label("member_name"))
        .join(UserEntity, CommentEntity.user_id == UserEntity.id)
        .filter(CommentEntity.post_id == post_id)
        .order_by(CommentEntity.created_at.asc())
        .all()
    )

    comment_entities = []
    for comment_entity, member_name in saved_comment_entities:  # 튜플 언패킹
        comment_entities.append(
            Comment(
                id=comment_entity.id,
                user_id=member_name,
                post_id=comment_entity.post_id,
                content=comment_entity.content,
                parent_id=comment_entity.parent_id,
                created_at=comment_entity.created_at,
            )
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


def delete_comment(db: Session, comment_id: int):
    comment_entity = db.query(CommentEntity).get(comment_id)
    db.delete(comment_entity)
    db.commit()

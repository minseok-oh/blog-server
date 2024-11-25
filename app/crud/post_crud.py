from datetime import datetime

from sqlalchemy.orm import Session

from app.domains.post import Post
from app.mapper import convert_to_post
from app.models.post_entity import PostEntity
from app.models.user_entity import UserEntity


def create_post(db: Session, post: Post) -> Post:
    post_entity = PostEntity(
        title=post.title,
        content=post.content,
        member_id=post.member_id,
        board_id=post.board_id,
        created_at=post.created_at,
        hits=post.hits,
    )
    db.add(post_entity)
    db.commit()


def get_post_by_id(db: Session, post_id: int) -> Post:
    post_entity = (
        db.query(PostEntity, UserEntity.name.label("member_name"))
        .join(UserEntity, PostEntity.member_id == UserEntity.id)
        .filter(PostEntity.id == post_id)
        .first()
    )

    if not post_entity:
        return None

    post, member_name = post_entity
    return convert_to_post(
        Post(
            post.id,
            post.title,
            post.content,
            member_name,
            post.board_id,
            post.created_at,
            post.hits
        )
    )


def get_posts_by_board_id(db: Session, board_id: str, page: int = 1) -> list[Post]:
    offset = (page - 1) * 10

    saved_post_entities = (
        db.query(PostEntity, UserEntity.name.label("member_id"))
        .join(UserEntity, PostEntity.member_id == UserEntity.id)
        .filter(PostEntity.board_id == board_id)
        .order_by(PostEntity.created_at.desc())
        .offset(offset)
        .limit(10)
        .all()
    )

    post_entities = []
    for post_entity, member_name in saved_post_entities:
        post_entities.append(
            Post(post_entity.id, post_entity.title, post_entity.content, member_name, post_entity.board_id,
                 post_entity.created_at, post_entity.hits))

    return [convert_to_post(post_entity) for post_entity in post_entities]


def update_post(db: Session, title: str, content: str, post_id: int) -> None:
    post_entity = db.query(PostEntity).filter(PostEntity.id == post_id).first()
    post_entity.title = title
    post_entity.content = content
    post_entity.created_at = datetime.now()
    db.commit()


def delete_post(db: Session, post_id: int) -> None:
    post_entity = db.query(PostEntity).filter(PostEntity.id == post_id).first()
    db.delete(post_entity)
    db.commit()


def update_post_hits(db: Session, post_id: int) -> None:
    post_entity = db.query(PostEntity).filter(PostEntity.id == post_id).first()
    post_entity.hits += 1
    db.commit()

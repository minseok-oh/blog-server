from app.domains.comment import Comment
from app.domains.post import Post
from app.domains.user import User
from app.models.comment_entity import CommentEntity
from app.models.post_entity import PostEntity
from app.models.user_entity import UserEntity


def convert_to_user(user_entity: UserEntity) -> User:
    return User(
        user_entity.id,
        user_entity.name,
        user_entity.member_id,
        user_entity.nickname,
        user_entity.password,
        user_entity.role,
        user_entity.avatar,
        user_entity.phone_number,
        user_entity.student_number,
        user_entity.birth,
        user_entity.email
    )


def convert_to_post(post_entity: PostEntity) -> Post:
    return Post(
        post_entity.id,
        post_entity.title,
        post_entity.content,
        post_entity.member_id,
        post_entity.board_id,
        post_entity.created_at,
        post_entity.hits
    )


def convert_to_comment(comment_entity: CommentEntity) -> Comment:
    return Comment(
        comment_entity.id,
        comment_entity.user_id,
        comment_entity.content,
        comment_entity.post_id,
        comment_entity.parent_id,
        comment_entity.created_at,
    )

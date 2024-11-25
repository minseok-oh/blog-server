from datetime import datetime

from sqlalchemy.orm import Session

from app.crud import comment_crud
from app.domains.comment import Comment


def create_comment(user_id: int, post_id: int, content: str, db: Session) -> None:
    """
    댓글을 생성합니다.
    TODO:
    """
    comment = Comment(id=None, user_id=user_id, post_id=post_id, content=content, parent_id=None,
                      created_at=datetime.now())
    comment_crud.create_comment(db=db, comment=comment)


def update_comment(user_id: int, comment_id: int, content: str, db: Session) -> Comment:
    """
    댓글을 수정합니다.
    """
    comment = comment_crud.get_comments_by_id(comment_id=comment_id, db=db)
    if comment.user_id != user_id:
        raise ValueError("수정 권한이 없습니다.")
    saved_comment = Comment(
        id=comment.id,
        user_id=comment.user_id,
        content=content,
        post_id=comment.post_id,
        parent_id=comment.parent_id,
        created_at=datetime.now(),
    )
    comment_crud.update_comment(db=db, comment=saved_comment)

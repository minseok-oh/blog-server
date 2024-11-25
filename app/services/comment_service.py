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


def update_comment(comment: Comment) -> Comment:
    """
    댓글을 수정합니다.
    TODO: Controller에서 호출 시에는 comment_id를 인자로 받아서 해당 댓글을 조회한 후에 댓글을 수정합니다.
    TODO: 추후에 content를 인자로 받아서 댓글을 수정할 수 있도록 수정합니다.
    """
    return comment.update_comment_date()

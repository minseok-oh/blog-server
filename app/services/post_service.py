from datetime import datetime

from sqlalchemy.orm import Session

from app.crud import post_crud
from app.domains.post import Post


def create_post(user_id: int, title: str, content: str, board_id: str, db: Session) -> Post:
    """
    게시글을 작성합니다.

    @:param title 게시글의 제목
    @:param content 게시글의 내용
    @:param member_id 작성자의 식별자
    @:param board_id 게시판의 식별자
    @:return created_post 저장된 게시글
    """
    post = Post(id=None, title=title, content=content, member_id=user_id, board_id=board_id, created_at=datetime.now())
    post_crud.create_post(db=db, post=post)


def update_post(user_id: int, post_id: int, title: str, content: str, db: Session) -> None:
    """
    게시글을 수정합니다.
    """
    post = post_crud.get_post_by_id(db=db, post_id=post_id)
    if post and post.member_id == user_id:
        post_crud.update_post(db=db, title=title, content=content, post_id=post_id)
    else:
        raise ValueError("게시글을 수정할 수 없습니다.")


def delete_post(user_id: int, post_id: int, db: Session) -> None:
    """
    게시글을 삭제합니다.
    """
    post = post_crud.get_post_by_id(db=db, post_id=post_id)
    if post and post.member_id == user_id:
        post_crud.delete_post(db=db, post_id=post_id)
    else:
        raise ValueError("게시글을 삭제할 수 없습니다.")

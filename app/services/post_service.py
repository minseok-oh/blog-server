from datetime import datetime

from app.schemas.post_create_dto import PostCreateDTO


def create_post(title: str, content: str, member_id: int, board_id: int) -> PostCreateDTO:
    """
    게시글을 작성합니다.

    @:param title 게시글의 제목
    @:param content 게시글의 내용
    @:param member_id 작성자의 식별자
    @:param board_id 게시판의 식별자
    @:return created_post 저장된 게시글
    """
    post = PostCreateDTO(id=None, title=title, content=content, member_id=member_id, board_id=board_id, created_at=datetime.now())
    # created_post = 게시글 저장
    # return created_post
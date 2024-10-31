from sqlalchemy.orm import Session

from app.schemas.post_create_dto import PostCreateDTO
from app.schemas.posts_read_dto import PostsReadDTO


def get_posts_by_board_id(db: Session, board_id: int, page: int = 1) -> list[PostsReadDTO]:
    # TODO: 추후 User, Board이 완료되면 테스트 코드 작성
    offset = (page - 1) * 10
    posts = (
        db.query(PostCreateDTO)
        .filter(PostCreateDTO.board_id == board_id)
        .order_by(PostCreateDTO.created_at.desc())
        .offset(offset)
        .limit(10)
        .all()
    )

    posts_read_dto = [PostsReadDTO(post) for post in posts]
    return posts_read_dto
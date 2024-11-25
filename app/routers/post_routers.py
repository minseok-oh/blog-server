from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.schemas.post.post_create_dto import PostCreateDTO
from app.schemas.post.post_read_dto import PostReadDTO
from app.schemas.post.post_update_dto import PostUpdateDTO
from app.schemas.post.posts_read_dto import PostsReadDTO
from app.services import post_service
from databases import get_db

router = APIRouter(prefix='/api/posts')


@router.get('/')
def get_posts(boardId: str, page: int = 1, db: Session = Depends(get_db)) -> list:
    posts = post_service.get_posts_by_board_id(board_id=boardId, page=page, db=db)
    print(posts)
    return [PostsReadDTO(post_id=post.id, title=post.title, author=post.member_id, date=post.created_at, hits=post.hits)
            for post in posts]


@router.get('/{postId}')
def get_post(postId: int, db: Session = Depends(get_db)):
    post = post_service.get_post_by_id(post_id=postId, db=db)
    return PostReadDTO(title=post.title, content=post.content, author=post.member_id, date=post.created_at,
                       hits=post.hits)


@router.post('/')
def create_post(request: Request, post_create_dto: PostCreateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    return post_service.create_post(user_id=user['user_id'], title=post_create_dto.title,
                                    content=post_create_dto.content,
                                    board_id=post_create_dto.board_id, db=db)


@router.put('/{postId}')
def update_post(request: Request, postId: int, post_update_dto: PostUpdateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    return post_service.update_post(user_id=user['user_id'], post_id=postId, title=post_update_dto.title,
                                    content=post_update_dto.content, db=db)


@router.delete('/{postId}')
def delete_post(request: Request, postId: int, db: Session = Depends(get_db)):
    user = request.state.user
    return post_service.delete_post(user_id=user['user_id'], post_id=postId, db=db)

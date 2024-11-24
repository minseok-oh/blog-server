from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.schemas.post.post_create_dto import PostCreateDTO
from app.schemas.post.post_update_dto import PostUpdateDTO
from app.services import post_service
from databases import get_db

router = APIRouter(prefix='/api/posts')


@router.post('/')
def create_post(request: Request, post_create_dto: PostCreateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    return post_service.create_post(user_id=user['user_id'], title=post_create_dto.title,
                                    content=post_create_dto.content,
                                    board_id=post_create_dto.board_id, db=db)


@router.post('/{postId}')
def update_post(request: Request, postId: int, post_update_dto: PostUpdateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    return post_service.update_post(user_id=user['user_id'], post_id=postId, title=post_update_dto.title,
                                    content=post_update_dto.content, db=db)

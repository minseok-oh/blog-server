from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.schemas.comment.comment_create_dto import CommentCreateDTO
from app.schemas.comment.comment_update_dto import CommentUpdateDTO
from app.services import comment_service
from databases import get_db

router = APIRouter(prefix="/api/comments")


@router.post("/")
def create_comment(request: Request, comment: CommentCreateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    comment_service.create_comment(user_id=user['user_id'], post_id=comment.post_id, content=comment.content, db=db)


@router.put("/{commentId}")
def update_comment(request: Request, commentId: int, comment: CommentUpdateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    comment_service.update_comment(user_id=user['user_id'], comment_id=commentId, content=comment.content,
                                   db=db)

@router.delete("/{commentId}")
def delete_comment(request: Request, commentId: int, db: Session = Depends(get_db)):
    user = request.state.user
    comment_service.delete_comment(user_id=user['user_id'], comment_id=commentId, db=db)

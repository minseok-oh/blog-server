from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.schemas.comment.comment_create_dto import CommentCreateDTO
from app.services import comment_service
from databases import get_db

router = APIRouter(prefix="/api/comments")


@router.post("/")
def create_comment(request: Request, comment: CommentCreateDTO, db: Session = Depends(get_db)):
    user = request.state.user
    comment_service.create_comment(user_id=user['user_id'], post_id=comment.post_id, content=comment.content, db=db)

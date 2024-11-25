from pydantic import BaseModel


class CommentCreateDTO(BaseModel):
    post_id: int
    content: str

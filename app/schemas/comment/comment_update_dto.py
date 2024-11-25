from pydantic import BaseModel


class CommentUpdateDTO(BaseModel):
    content: str

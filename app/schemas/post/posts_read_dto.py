from datetime import datetime

from pydantic import BaseModel


class PostsReadDTO(BaseModel):
    post_id: int
    title: str
    author: str
    date: datetime
    hits: int
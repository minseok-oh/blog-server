from datetime import datetime

from pydantic import BaseModel


class PostReadDTO(BaseModel):
    title: str
    content: str
    author: str
    date: datetime
    hits: int

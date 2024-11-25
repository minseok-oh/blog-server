from datetime import datetime

from pydantic import BaseModel


class CommentsReadDTO(BaseModel):
    author: str
    content: str
    date: datetime

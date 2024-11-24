from pydantic import BaseModel


class PostUpdateDTO(BaseModel):
    title: str
    content: str

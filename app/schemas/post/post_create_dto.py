from pydantic import BaseModel


class PostCreateDTO(BaseModel):
    title: str
    content: str
    board_id: str

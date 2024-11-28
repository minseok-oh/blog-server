from datetime import datetime

from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    userId: str
    nickname: str
    password: str
    email: str
    username: str
    birth: datetime
    phone: str

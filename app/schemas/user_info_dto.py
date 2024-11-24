from pydantic import BaseModel


class UserInfoDTO(BaseModel):
    username: str
    role: str

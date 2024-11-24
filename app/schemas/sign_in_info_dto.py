from pydantic import BaseModel


class SignInInfoDTO(BaseModel):
    user_id: int
    username: str
    role: str

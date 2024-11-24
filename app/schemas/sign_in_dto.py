from pydantic import BaseModel


class SignInDTO(BaseModel):
    userId: str
    password: str

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_driver: bool


class UserLogin(BaseModel):
    email: EmailStr
    password: str


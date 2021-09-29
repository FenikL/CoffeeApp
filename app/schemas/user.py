from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    name: str
    last_name: str


class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True

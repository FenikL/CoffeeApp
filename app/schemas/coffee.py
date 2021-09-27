from pydantic import BaseModel
from uuid import UUID


class CoffeeBase(BaseModel):
    name: str


class CoffeeAdd(CoffeeBase):
    strength: str
    img: str
    cost: float


class Coffee(CoffeeBase):
    id: UUID

    class Config:
        orm_mode = True

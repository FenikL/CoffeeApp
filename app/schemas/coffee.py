from pydantic import BaseModel


class CoffeeBase(BaseModel):
    name: str


class CoffeeAdd(CoffeeBase):
    strength: str
    img: str
    cost: float


class Coffee(CoffeeBase):
    id: int

    class Config:
        orm_mode = True

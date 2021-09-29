from pydantic import BaseModel
<<<<<<< HEAD


class OrderBase(BaseModel):
=======
from datetime import datetime
from uuid import UUID


class OrderBase(BaseModel):
    user_id: UUID


class CreateOrder(OrderBase):
    date: datetime


class Order(OrderBase):
    id: UUID

    class Config:
        orm_mode = True


class OrderItemsBase(BaseModel):
    order_id: UUID


class AddOrderItems(BaseModel):
    coffee_id: UUID
    count: int


class GetItems(AddOrderItems):
    class Config:
        orm_mode = True


class OrderItems(OrderItemsBase):
    id: UUID

    class Config:
        orm_mode = True

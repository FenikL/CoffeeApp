from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.crud import user as user_crud
from app.crud import coffee as coffee_crud
from app.crud import order as order_crud
from app.model import user as user_model
from app.model import order as order_model
from app.model import balance as balance_model
from app.model import order_items as order_items_model
from app.model import balance_items as balance_items_model
from app.model import coffee as coffee_model
from app.model import database
from app.schemas import user as user_schema
from app.schemas import coffee as coffee_schema
from app.schemas import order as order_schema
from app.model.database import SessionLocal, engine

database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/coffee/", response_model=coffee_schema.Coffee)
def add_coffee(coffee: coffee_schema.CoffeeAdd, db: Session = Depends(get_db)):
    db_coffee = coffee_crud.get_coffee_by_name(db, name=coffee.name)
    if db_coffee:
        raise HTTPException(status_code=400, detail="Coffee already added")
    return coffee_crud.add_coffee(db=db, coffee=coffee)


@app.post("/orders/", response_model=order_schema.Order)
def create_order(order: order_schema.CreateOrder, db: Session = Depends(get_db)):
    return order_crud.create_order(db=db, order=order)


@app.get("/users/{user_id}/orders/", response_model=List[order_schema.Order])
def get_orders_for_this_user(user_id: UUID, db: Session = Depends(get_db)):
    orders = order_crud.get_orders_for_current_user(db=db, user_id=user_id)
    return orders


@app.post("/orders/{order_id}/items/", response_model=order_schema.OrderItems)
def add_order_items(order_id: UUID, item: order_schema.AddOrderItems, db: Session = Depends(get_db)):
    return order_crud.add_order_items(db=db, order_items=item, order_id=order_id)


@app.get("/orders/{order_id}/items/", response_model=List[order_schema.GetItems])
def get_order_items(order_id: UUID, db: Session = Depends(get_db)):
    items = order_crud.get_order_items(db=db, order_id=order_id)
    return items

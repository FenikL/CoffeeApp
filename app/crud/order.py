from sqlalchemy.orm import Session
from uuid import UUID

from app.model import order as order_model
from app.model import order_items as items_model
from app.schemas import order as order_schema


def create_order(db: Session, order: order_schema.CreateOrder):
    db_order = order_model.Order(user_id=order.user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: UUID):
    return db.query(order_model.Order).filter(order_model.Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(order_model.Order).offset(skip).limit(limit).all()


def get_orders_for_current_user(db: Session, user_id: UUID):
    return db.query(order_model.Order).filter(order_model.Order.user_id == user_id).all()


def add_order_items(db: Session, order_items: order_schema.AddOrderItems, order_id: UUID):
    db_items = items_model.OrderItems(**order_items.dict(), order_id=order_id)
    db.add(db_items)
    db.commit()
    db.refresh(db_items)
    return db_items


def get_order_items(db: Session, order_id: UUID):
    return db.query(items_model.OrderItems).filter(items_model.OrderItems.order_id == order_id).all()

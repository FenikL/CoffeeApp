from sqlalchemy.orm import Session
from uuid import UUID

from app.model import coffee as coffee_model
from app.schemas import coffee as coffee_schema


def add_coffee(db: Session, coffee: coffee_schema.CoffeeAdd):
    db_coffee = coffee_model.Coffee(name=coffee.name, strength=coffee.strength, img=coffee.img, cost=coffee.cost)
    db.add(db_coffee)
    db.commit()
    db.refresh(db_coffee)
    return db_coffee


def get_coffee(db: Session, coffee_id: UUID):
    return db.query(coffee_model.Coffee).filter(coffee_model.Coffee.id == coffee_id).first()


def get_some_coffee(db: Session, skip: int = 0, limit: int = 100):
    return db.query(coffee_model.Coffee).offset(skip).limit(limit).all()


def get_coffee_by_name(db: Session, name: str):
    return db.query(coffee_model.Coffee).filter(coffee_model.Coffee.name == name).first()

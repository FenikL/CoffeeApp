from sqlalchemy.orm import Session
from uuid import UUID

from app.model import user as user_model
from app.schemas import user as user_schema


def create_user(db: Session, user: user_schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_model.User(email=user.email, name=user.name, last_name=user.last_name, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: UUID):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

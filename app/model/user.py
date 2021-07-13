from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.model.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    orders = relationship('Order', back_populates="user", cascade="all, delete")
    balance = relationship('Balance', back_populates="user", uselist=False, cascade="all, delete")

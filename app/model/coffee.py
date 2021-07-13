from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from app.model.database import Base


class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    strength = Column(String(), nullable=False)
    img = Column(String(), nullable=True)
    cost = Column(Float, nullable=False)

    balance_items = relationship('BalanceItems', back_populates="coffee", cascade="all, delete")
    order_items = relationship('BalanceItems', back_populates="coffee", cascade="all, delete")

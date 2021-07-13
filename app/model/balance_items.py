from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Base


class BalanceItems(Base):
    __tablename__ = 'balance_items'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)

    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    balance_id = Column(Integer, ForeignKey('balance.id'))
    coffee = relationship('Coffee', back_populates="balance_items")
    balance = relationship('Balance', back_populates="balance_items")

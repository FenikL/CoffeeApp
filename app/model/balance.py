from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Base


class Balance(Base):
    __tablename__ = 'balance'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates="balance")

    balance_items = relationship('BalanceItems', back_populates="balance", cascade="all, delete")

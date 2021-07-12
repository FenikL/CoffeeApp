from sqlalchemy import Column, ForeignKey

from app.model import Base

class BalanceItems(Base):
    __tablename__ = 'balance_items'
    id = Column(Integer, primary_key=True) 
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    balance_id = Column(Integer, ForeignKey('balance.id'))
    count = Column(Integer, nullable=False)

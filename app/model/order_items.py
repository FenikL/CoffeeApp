from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Base


class OrderItems(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)

    order_id = Column(Integer, ForeignKey('orders.id'))
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    order = relationship('Order', back_populates="items")
    coffee = relationship('Coffee', back_populates="order_items")
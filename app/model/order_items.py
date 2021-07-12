from sqlalchemy import Column, ForeignKey

from app.model import Base

class OrderItems(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    count = Column(Integer, nullable=False)

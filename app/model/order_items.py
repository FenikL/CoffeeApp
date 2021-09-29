from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.model.database import Base


class OrderItems(Base):
    __tablename__ = 'order_items'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id = Column(UUID(True), ForeignKey("orders.id"), nullable=False)
    coffee_id = Column(UUID(True), ForeignKey("coffee.id"), nullable=False)
    count = Column(Integer, nullable=False)

    order = relationship('Order', back_populates="items", lazy=True)
    coffee = relationship('Coffee', back_populates="order_items", lazy=True)

from sqlalchemy import Column, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime

from app.model.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date = Column(TIMESTAMP(timezone=True), default=datetime.now)

    user_id = Column(UUID(True), ForeignKey("users.id"), nullable=False)
    user = relationship('User', back_populates="orders", lazy=True)

    items = relationship('OrderItems', back_populates="order", cascade="all, delete", lazy=True)

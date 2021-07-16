from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.model.database import Base


class BalanceItems(Base):
    __tablename__ = 'balance_items'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    count = Column(Integer, nullable=False)

    coffee_id = Column(UUID(True), ForeignKey("coffee.id"), nullable=False)
    coffee = relationship('Coffee', back_populates="balance_items", lazy=True)
    balance_id = Column(UUID(True), ForeignKey("balance.id"), nullable=False)
    balance = relationship('Balance', back_populates="balance_items", lazy=True)

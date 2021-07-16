from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.model.database import Base


class Coffee(Base):
    __tablename__ = 'coffee'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(), nullable=False)
    strength = Column(String(), nullable=False)
    img = Column(String(), nullable=True)
    cost = Column(Float, nullable=False)

    balance_items = relationship('BalanceItems', back_populates="coffee", cascade="all, delete", lazy=True)
    order_items = relationship('BalanceItems', back_populates="coffee", cascade="all, delete", lazy=True)

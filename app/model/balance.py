from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.model.database import Base


class Balance(Base):
    __tablename__ = 'balance'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    user_id = Column(UUID(True), ForeignKey("users.id"), nullable=False)
    user = relationship('User', back_populates="balance", lazy=True)

    balance_items = relationship('BalanceItems', back_populates="balance", cascade="all, delete", lazy=True)

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.model.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    #orders = relationship('Order', back_populates="user", cascade="all, delete", lazy=True)
    #balance = relationship('Balance', back_populates="user", uselist=False, cascade="all, delete", lazy=True)

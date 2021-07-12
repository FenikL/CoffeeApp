from sqlalchemy import Column, TIMESTAMP, ForeignKey

from app.model import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date  = Column(TIMESTAMP(timezone=True), nullable=False)

from sqlalchemy import Column, String

from app.model import Base

class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    strength = Column(String(), nullable=False)
    img = Column(String(), nullable=True)
    cost = Column(Float, nullable=False)

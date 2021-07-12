from sqlalchemy import Column, ForeignKey

from app.model import Base

class Balance(Base):
    __tablename__ = 'balance'
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('users.id'))

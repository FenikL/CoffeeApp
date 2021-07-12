from sqlalchemy import Column, String

from app.model import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

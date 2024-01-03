from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BusinessModel(Base):
    __tablename__ = 'business'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
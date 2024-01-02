from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    email = Column(String)
    password = Column(String)
    type_business = Column(Integer)
    created_at = Column(Date)
    is_active = Column(Integer)
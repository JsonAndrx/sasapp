from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ClientModel(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, index=True)
    id_username = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    type_document = Column(Integer)
    num_document = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    dob = Column(Date)
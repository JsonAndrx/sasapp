from pydantic import BaseModel, EmailStr
from datetime import date

class ClientSchema(BaseModel):
    id_username: int
    first_name: str
    last_name: str
    dob: date
    type_document: int
    num_document: str
    phone: str
    email: EmailStr
    address: str

class ClientSchemaOutput(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: date
    type_document: int
    num_document: str
    phone: str
    email: EmailStr
    address: str

    
from pydantic import BaseModel, EmailStr, Field
from datetime import date

class RegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    password: str
    type_business: int
    created_at: date = None
    is_active: int   = None

    class Config:
        schema_extra = {
            "exclude": ["created_at", "is_active"]
        }

class RegisterSchemaOutput(BaseModel):
    username: str
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    password: str
    type_business: int




class LoginSchema(BaseModel):
    username: str
    password: str

class LoginSchemaOut(BaseModel):
    username: str
    token: str
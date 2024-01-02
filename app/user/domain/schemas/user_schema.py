from pydantic import BaseModel, EmailStr
from datetime import date

class UserSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    password: str
    type_business: int
    created_at: date
    is_active: int

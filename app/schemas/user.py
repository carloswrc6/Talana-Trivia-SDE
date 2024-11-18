from pydantic import BaseModel, EmailStr
from typing import List

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # Permite serializar modelos SQLAlchemy

from pydantic import BaseModel
from typing import Optional

from datetime import datetime as DateTime


class UserBase(BaseModel):
    email: str


class UserCreate(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int
    email: str
    is_active: bool
    created_at: DateTime

    class Config:
        from_attributes = True


class TokenData(BaseModel):
    email: Optional[str] = None

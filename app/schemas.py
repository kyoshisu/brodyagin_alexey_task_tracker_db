from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


# Схемы задач
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "new"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    title: Optional[str] = None
    status: Optional[str] = None


class Task(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Позволяет Pydantic читать данные из SQLAlchemy


# Схемы пользователей
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
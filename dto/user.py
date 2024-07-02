from enum import Enum
from pydantic import BaseModel, EmailStr, Field
import uuid

class RoleEnum(str, Enum):
    User = 'user'
    Admin = 'admin'

class UserBase(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=30)

class User(UserBase):
    id: uuid.uuid4
    nickname: str = Field(min_length=3, max_length=25)
    bio: str | None = Field(default=None, max_length=300)
    role: RoleEnum = RoleEnum.User

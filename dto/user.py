from enum import Enum
from pydantic import BaseModel, EmailStr, Field
import uuid

class RoleEnum(str, Enum):
    User = 'user'
    Admin = 'admin'

class User(BaseModel):
    id: uuid.uuid4
    login: str
    email: EmailStr
    nickname: str = Field(min_length=3, max_length=25)
    password: str
    bio: str | None = Field(default=None, max_length=300)
    role: RoleEnum = RoleEnum.User

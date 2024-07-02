from typing import List
from pydantic import BaseModel, Field
import uuid
from decimal import Decimal

class ServerPage(BaseModel):
    id: uuid.uuid4
    owner_id: uuid.uuid4
    name: str
    ip: str
    version: str = Field(default='1.20.1')
    description: str | None = Field(default=None,
                                    max_length=300)
    image: str | None = Field(default=None)
    rating: Decimal | None = Field(default=0.0,
                                   max_digits=3,
                                   decimal_places=2,
                                   ge=0.0, le=5.0)
    plugins: List[str] | None = Field(default=None)
    tags: List[str] | None = Field(default=None)
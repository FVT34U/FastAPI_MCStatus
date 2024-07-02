from pydantic import BaseModel, Field
from uuid import uuid

class Comment(BaseModel):
    id: uuid
    owner_id: uuid
    server_page_id: uuid
    like_count: int = Field(default=0)
    dislike_count: int = Field(default=0)
    text: str | None = Field(default=None,
                             max_length=300)
from pydantic import BaseModel, Field
import uuid

class Comment(BaseModel):
    id: uuid.uuid4
    owner_id: uuid.uuid4
    server_page_id: uuid.uuid4
    like_count: int = Field(default=0)
    dislike_count: int = Field(default=0)
    text: str | None = Field(default=None,
                             max_length=300)
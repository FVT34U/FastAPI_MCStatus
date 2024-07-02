from pydantic import BaseModel, Field
from uuid import uuid

class CommentRate(BaseModel):
    row_id: uuid
    comment_id: uuid
    user_id: uuid
    rate_number: int = Field(default=0,
                             ge=-1, le=1)
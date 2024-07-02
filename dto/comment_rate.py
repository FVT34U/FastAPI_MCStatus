from pydantic import BaseModel, Field
import uuid

class CommentRate(BaseModel):
    row_id: uuid.uuid4
    comment_id: uuid.uuid4
    user_id: uuid.uuid4
    rate_number: int = Field(default=0,
                             ge=-1, le=1)
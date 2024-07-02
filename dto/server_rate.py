from pydantic import BaseModel, Field
import uuid

class ServerRate(BaseModel):
    row_id: uuid.uuid4
    server_page_id: uuid.uuid4
    user_id: uuid.uuid4
    rate_number: int = Field(default=0,
                             ge=-1, le=1)
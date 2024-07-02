from pydantic import BaseModel, Field
from uuid import uuid

class ServerRate(BaseModel):
    row_id: uuid
    server_page_id: uuid
    user_id: uuid
    rate_number: int = Field(default=0,
                             ge=-1, le=1)
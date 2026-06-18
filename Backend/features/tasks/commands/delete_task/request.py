from pydantic import BaseModel

class DeleteTaskRequest(BaseModel):
    id: int
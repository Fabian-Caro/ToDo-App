from pydantic import BaseModel

class UpdateTaskPayload(BaseModel):
    title: str

class UpdateTaskRequest(BaseModel):
    id: int
    title: str

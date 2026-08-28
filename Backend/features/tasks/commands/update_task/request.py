from pydantic import BaseModel, Field


class UpdateTaskPayload(BaseModel):
    title: str = Field(min_length=1)
    is_completed: bool


class UpdateTaskRequest(BaseModel):
    id: int
    title: str
    is_completed: bool

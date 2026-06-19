from pydantic import BaseModel


class UpdateTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool

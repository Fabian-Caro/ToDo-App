from pydantic import BaseModel


class GetTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool

from pydantic import BaseModel

class DeleteTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool
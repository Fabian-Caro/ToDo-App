from pydantic import BaseModel


class ToggleTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool

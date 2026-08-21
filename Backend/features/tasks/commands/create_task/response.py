from pydantic import BaseModel

from features.tasks.shared.links import TaskLinks


class CreateTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool
    links: TaskLinks

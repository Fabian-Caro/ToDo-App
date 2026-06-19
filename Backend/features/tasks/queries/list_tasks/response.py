from pydantic import BaseModel


class TaskItem(BaseModel):
    id: int
    title: str
    is_completed: bool


class ListTasksResponse(BaseModel):
    tasks: list[TaskItem]

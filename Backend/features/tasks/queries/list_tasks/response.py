from pydantic import BaseModel

class TaskItem(BaseModel):
    id: int
    title: str

class ListTasksResponse(BaseModel):
    tasks: list[TaskItem]

from pydantic import BaseModel

class TaskItem(BaseModel):
    id: int
    title: str
    is_completed: bool

class Pagination(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_previous: bool
    next_page: int | None
    previous_page: int | None

class ListTasksResponse(BaseModel):
    tasks: list[TaskItem]
    pagination: Pagination

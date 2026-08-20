from pydantic import BaseModel

class TaskLinks(BaseModel):
    self: str

class TaskItem(BaseModel):
    id: int
    title: str
    is_completed: bool
    links: TaskLinks
    
class PaginationLinks(BaseModel):
    self: str
    first: str
    previous: str | None
    next: str | None
    last: str

class Pagination(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_previous: bool
    next_page: int | None
    previous_page: int | None
    links: PaginationLinks

class ListTasksResponse(BaseModel):
    tasks: list[TaskItem]
    pagination: Pagination

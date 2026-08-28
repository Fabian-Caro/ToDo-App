from pydantic import BaseModel


class Link(BaseModel):
    href: str
    method: str


class TaskLinks(BaseModel):
    self: Link
    collection: Link
    update: Link
    toggle_completation: Link
    delete: Link


class GetTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool
    links: TaskLinks

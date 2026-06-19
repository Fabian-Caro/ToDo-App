from pydantic import BaseModel


class SearchTaskItem(BaseModel):
    id: int
    title: str
    is_completed: bool


class SearchTaskResponse(BaseModel):
    results: list[SearchTaskItem]
    total_results: int

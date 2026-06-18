from pydantic import BaseModel


class SearchTaskItem(BaseModel):
    id: int
    title: str


class SearchTaskResponse(BaseModel):
    results: list[SearchTaskItem]
    total_results: int

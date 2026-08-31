from typing import Literal

from pydantic import BaseModel, Field


class SearchTaskRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Texto a buscar en el título")
    page: int
    page_size: int
    is_completed: bool | None
    sort_by: Literal["id", "title"]
    sort_order: Literal["asc", "desc"]
    
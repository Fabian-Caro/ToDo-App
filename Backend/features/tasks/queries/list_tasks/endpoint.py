from fastapi import APIRouter, Query

from features.tasks.queries.list_tasks.handler import execute
from features.tasks.queries.list_tasks.response import ListTasksResponse
router = APIRouter()

@router.get("/")
def list_tasks(
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Total tasks by page"), 
    is_completed: bool | None = None,   
) -> ListTasksResponse:
    return execute(
        page=page,
        page_size=page_size,
        is_completed=is_completed,
    )

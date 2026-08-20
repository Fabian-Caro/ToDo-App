from typing import Literal

from fastapi import APIRouter, Query, Request

from features.tasks.queries.list_tasks.handler import execute
from features.tasks.queries.list_tasks.response import ListTasksResponse

router = APIRouter()

@router.get("/")
def list_tasks(
    request: Request,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Total tasks by page"), 
    is_completed: bool | None = None,   
    sort_by: Literal["id", "title"] = Query(
        default="id",
        description="Field used to sort tasks",
    ),
    sort_order: Literal["asc", "desc"] = Query(
        default="asc",
        description="Sort direction",    
    ),
) -> ListTasksResponse:
    return execute(
        request=request,
        page=page,
        page_size=page_size,
        is_completed=is_completed,
        sort_by=sort_by,
        sort_order=sort_order,
    )

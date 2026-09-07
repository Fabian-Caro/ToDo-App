from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Query, Request
from features.tasks.queries.list_tasks.handler import execute
from features.tasks.queries.list_tasks.response import ListTasksResponse
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.get("/", name="list_tasks")
def list_tasks(
    request: Request,
    uow: Annotated[UnitOfWork, Depends(get_uow)],
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
        uow=uow,
        page=page,
        page_size=page_size,
        is_completed=is_completed,
        sort_by=sort_by,
        sort_order=sort_order,
    )

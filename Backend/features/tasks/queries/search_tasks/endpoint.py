from typing import Literal, Annotated

from fastapi import APIRouter, Query, Request, Depends
from features.tasks.queries.search_tasks.handler import execute
from features.tasks.queries.search_tasks.request import SearchTaskRequest
from features.tasks.queries.search_tasks.response import SearchTaskResponse
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.get("/search", response_model=SearchTaskResponse, name="search_tasks")
def search_tasks(
    request: Request,
    uow: Annotated[UnitOfWork, Depends(get_uow)],
    q: str = Query(..., description="Término de búsqueda"),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    is_completed: bool | None = None,
    sort_by: Literal["id", "title"] = Query(default="id"),
    sort_order: Literal["asc", "desc"] = Query(default="asc"),
) -> SearchTaskResponse:
    search_request = SearchTaskRequest(
        query=q,
        page=page,
        page_size=page_size,
        is_completed=is_completed,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    return execute(request, search_request, uow)

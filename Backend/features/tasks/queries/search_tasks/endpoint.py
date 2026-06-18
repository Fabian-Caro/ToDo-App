from fastapi import APIRouter, Query

from features.tasks.queries.search_tasks.request import SearchTaskRequest
from features.tasks.queries.search_tasks.response import SearchTaskResponse
from features.tasks.queries.search_tasks.handler import execute

router = APIRouter()


@router.get("/search", response_model=SearchTaskResponse)
def search_tasks(q: str = Query(..., description="Término de búsqueda")):
    request = SearchTaskRequest(query=q)
    response = execute(request)

    return response

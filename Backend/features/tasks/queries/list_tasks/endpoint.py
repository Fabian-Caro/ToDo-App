from fastapi import APIRouter

from features.tasks.queries.list_tasks.handler import execute
from features.tasks.queries.list_tasks.response import ListTasksResponse

router = APIRouter()


@router.get("/")
def list_tasks() -> ListTasksResponse:
    response = execute()
    return response

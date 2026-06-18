from fastapi import APIRouter

from features.tasks.queries.list_tasks.response import ListTasksResponse
from features.tasks.queries.list_tasks.handler import execute

router = APIRouter()


@router.get("/")
def list_tasks() -> ListTasksResponse:
    return execute()

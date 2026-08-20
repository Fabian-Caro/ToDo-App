from fastapi import APIRouter, HTTPException

from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse
from features.tasks.queries.get_task.handler import execute

router = APIRouter()


@router.get("/{task_id}", response_model=GetTaskResponse, name="get_task")
def get_task(task_id: int) -> GetTaskResponse | None:
    request = GetTaskRequest(id=task_id)
    response = execute(request)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

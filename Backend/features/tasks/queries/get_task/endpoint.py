from fastapi import APIRouter, HTTPException, Request
from features.tasks.queries.get_task.handler import execute
from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse

router = APIRouter()


@router.get("/{task_id}", response_model=GetTaskResponse, name="get_task")
def get_task(request: Request, task_id: int) -> GetTaskResponse:
    get_task_request = GetTaskRequest(id=task_id)
    response = execute(request, get_task_request)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

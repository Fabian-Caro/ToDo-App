from fastapi import APIRouter, HTTPException, Request

from features.tasks.commands.update_task.handler import execute
from features.tasks.commands.update_task.request import (
    UpdateTaskPayload,
    UpdateTaskRequest,
)
from features.tasks.commands.update_task.response import UpdateTaskResponse

router = APIRouter()


@router.put("/{task_id}", response_model=UpdateTaskResponse, name="update_task")
def update_task(
    request:Request,
    task_id: int,
    payload: UpdateTaskPayload
) -> UpdateTaskResponse | None:
    update_task_request = UpdateTaskRequest(
        id=task_id,
        title=payload.title,
        is_completed=payload.is_completed,
    )
    
    response = execute(request, update_task_request)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

from fastapi import APIRouter, HTTPException

from features.tasks.commands.update_task.handler import execute
from features.tasks.commands.update_task.request import (
    UpdateTaskPayload,
    UpdateTaskRequest,
)
from features.tasks.commands.update_task.response import UpdateTaskResponse

router = APIRouter()


@router.put("/{task_id}", response_model=UpdateTaskResponse, name="update_task")
def update_task(task_id: int, payload: UpdateTaskPayload) -> UpdateTaskResponse | None:
    request = UpdateTaskRequest(id=task_id, title=payload.title)
    response = execute(request)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

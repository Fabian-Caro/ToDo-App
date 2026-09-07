from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from features.tasks.commands.update_task.handler import execute
from features.tasks.commands.update_task.request import (
    UpdateTaskPayload,
    UpdateTaskRequest,
)
from features.tasks.commands.update_task.response import UpdateTaskResponse
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.put("/{task_id}", response_model=UpdateTaskResponse, name="update_task")
def update_task(
    request: Request,
    task_id: int,
    payload: UpdateTaskPayload,
    uow: Annotated[UnitOfWork, Depends(get_uow)],
) -> UpdateTaskResponse | None:
    update_task_request = UpdateTaskRequest(
        id=task_id,
        title=payload.title,
        is_completed=payload.is_completed,
    )

    response = execute(request, update_task_request, uow)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

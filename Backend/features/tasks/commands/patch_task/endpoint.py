from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from features.tasks.commands.patch_task.handler import execute
from features.tasks.commands.patch_task.request import (
    PatchTaskPayload,
    PatchTaskRequest,
)
from features.tasks.commands.patch_task.response import PatchTaskResponse
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.patch(
    "/{task_id}",
    response_model=PatchTaskResponse,
    name="patch_task",
)
def patch_task(
    request: Request,
    task_id: int,
    payload: PatchTaskPayload,
    uow: Annotated[UnitOfWork, Depends(get_uow)],
) -> PatchTaskResponse:
    patch_task_request = PatchTaskRequest(
        id=task_id,
        **payload.model_dump(exclude_unset=True),
    )

    response = execute(request, patch_task_request, uow)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

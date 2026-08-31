from fastapi import APIRouter, Request, HTTPException

from features.tasks.commands.patch_task.response import PatchTaskResponse
from features.tasks.commands.patch_task.request import (
    PatchTaskPayload,
    PatchTaskRequest,
)
from features.tasks.commands.patch_task.handler import execute

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
) -> PatchTaskResponse:
    patch_task_request = PatchTaskRequest(
        id=task_id,
        **payload.model_dump(exclude_unset=True),
    )

    response = execute(request, patch_task_request)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

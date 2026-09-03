from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from features.tasks.queries.get_task.handler import execute
from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.get("/{task_id}", response_model=GetTaskResponse, name="get_task")
def get_task(
    request: Request, task_id: int, uow: Annotated[UnitOfWork, Depends(get_uow)]
) -> GetTaskResponse:
    get_task_request = GetTaskRequest(id=task_id)
    response = execute(request, get_task_request, uow)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

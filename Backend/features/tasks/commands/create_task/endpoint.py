from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response, status
from features.tasks.commands.create_task.handler import execute
from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.post(
    "/",
    response_model=CreateTaskResponse,
    status_code=status.HTTP_201_CREATED,
    name="create_task",
)
def create_task(
    request: Request,
    response: Response,
    create_task_request: CreateTaskRequest,
    uow: Annotated[UnitOfWork, Depends(get_uow)],
) -> CreateTaskResponse:
    created_task = execute(request, create_task_request, uow)

    response.headers["Location"] = str(
        request.url_for("get_task", task_id=created_task.id)
    )

    return created_task

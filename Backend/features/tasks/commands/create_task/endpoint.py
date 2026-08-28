from fastapi import APIRouter, Request, Response, status

from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from features.tasks.commands.create_task.handler import execute

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
) -> CreateTaskResponse:
    created_task = execute(request, create_task_request)

    response.headers["Location"] = str(
        request.url_for("get_task", task_id=created_task.id)
    )

    return created_task

from fastapi import APIRouter

from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from features.tasks.commands.create_task.handler import execute

router = APIRouter()


@router.post("/", response_model=CreateTaskResponse, name="create_task")
def create_task(
    request: CreateTaskRequest,
) -> CreateTaskResponse:
    response = execute(request)
    return response

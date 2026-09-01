from fastapi import Request

from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from features.tasks.shared.links import build_task_links
from features.tasks.shared.repository import TaskRepository
from infrastructure.fake_db import FAKE_DB, get_next_id

repository = TaskRepository()


def execute(
    request: Request,
    create_task_request: CreateTaskRequest,
) -> CreateTaskResponse:
    task = repository.create(create_task_request.title)

    return CreateTaskResponse(
        id=task["id"],
        title=task["title"],
        is_completed=task["is_completed"],
        links=build_task_links(request, task["id"]),
    )

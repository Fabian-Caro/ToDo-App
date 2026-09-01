from fastapi import Request
from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse
from features.tasks.shared.links import build_task_links
from features.tasks.shared.repository import TaskRepository
from infrastructure.database.fake_db import FAKE_DB

repository = TaskRepository()


def execute(
    request: Request,
    get_task_request: GetTaskRequest,
) -> GetTaskResponse | None:
    task = repository.get_by_id(get_task_request.id)

    if task is None:
        return None

    return GetTaskResponse(
        id=task["id"],
        title=task["title"],
        is_completed=task["is_completed"],
        links=build_task_links(request, task["id"]),
    )

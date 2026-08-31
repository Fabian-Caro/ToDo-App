from fastapi import Request
from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse
from features.tasks.shared.links import build_task_links

from infrastructure.fake_db import FAKE_DB


def execute(
    request: Request,
    get_task_request: GetTaskRequest,
) -> GetTaskResponse | None:
    task = next(
        (task for task in FAKE_DB["tasks"] if task["id"] == get_task_request.id),
        None,
    )

    if task is None:
        return None

    return GetTaskResponse(
        id=task["id"],
        title=task["title"],
        is_completed=task["is_completed"],
        links=build_task_links(request, task["id"]),
    )

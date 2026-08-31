from fastapi import Request

from features.tasks.commands.update_task.request import UpdateTaskRequest
from features.tasks.commands.update_task.response import UpdateTaskResponse
from features.tasks.shared.links import build_task_links

from infrastructure.fake_db import FAKE_DB


def execute(
    request: Request,
    update_task_request: UpdateTaskRequest
) -> UpdateTaskResponse | None:
    task = next(
        (
            task
            for task in FAKE_DB["tasks"]
            if task["id"] == update_task_request.id
        ),
        None,
    )

    if task is None:
        return None

    task["title"] = update_task_request.title
    task["is_completed"] = update_task_request.is_completed

    return UpdateTaskResponse(
        id=task["id"],
        title=task["title"],
        is_completed=task["is_completed"],
        links=build_task_links(request, task["id"]),
    )

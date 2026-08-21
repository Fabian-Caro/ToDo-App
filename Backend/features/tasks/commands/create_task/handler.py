from fastapi import Request

from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from features.tasks.shared.links import build_task_links
from infrastructure.fake_db import FAKE_DB, get_next_id


def execute(
    request: Request,
    create_task_request: CreateTaskRequest,
) -> CreateTaskResponse:
    new_id = get_next_id("tasks")

    task = {
        "id": new_id,
        "title": create_task_request.title,
        "is_completed": False,
    }

    FAKE_DB["tasks"].append(task)

    return CreateTaskResponse(
        id=task["id"],
        title=task["title"],
        is_completed=task["is_completed"],
        links=build_task_links(request, task["id"]),
    )

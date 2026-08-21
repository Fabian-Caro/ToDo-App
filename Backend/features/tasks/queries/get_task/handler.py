from fastapi import Request
from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse, Link, TaskLinks
from infrastructure.fake_db import FAKE_DB


def execute(
    request: Request,
    get_task_request: GetTaskRequest,
) -> GetTaskResponse | None:
    task = next(
        (
            task 
            for task in FAKE_DB["tasks"] 
            if task["id"] == get_task_request.id
        ), 
        None,
    )

    if task is None:
        return None

    task_id = task["id"]

    links = TaskLinks(
        self=Link(
            href=str(request.url_for("get_task", task_id=task_id)),
            method="GET",
        ),
        collection=Link(
            href=str(request.url_for("list_tasks")),
            method="GET",
        ),
        update=Link(
            href=str(request.url_for("update_task", task_id=task_id)),
            method="PUT",
        ),
        toggle_completation=Link(
            href=str(request.url_for("toggle_task", task_id=task_id)),
            method="PATCH",
        ),
        delete=Link(
            href=str(request.url_for("delete_task", task_id=task_id)),
            method="DELETE",
        ),
    )

    return GetTaskResponse(
        id=task_id,
        title=task["title"],
        is_completed=task["is_completed"],
        links=links,
    )

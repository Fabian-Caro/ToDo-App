from typing import Literal

from fastapi import Request
from pydantic import BaseModel


class Link(BaseModel):
    href: str
    method: Literal["GET", "PUT", "PATCH", "DELETE"]


class TaskLinks(BaseModel):
    self: Link
    collection: Link
    update: Link
    toggle_completation: Link
    delete: Link


def build_task_links(request: Request, task_id: int) -> TaskLinks:
    return TaskLinks(
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

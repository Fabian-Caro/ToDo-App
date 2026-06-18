from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from infrastructure.fake_db import FAKE_DB, get_next_id


def execute(request: CreateTaskRequest) -> CreateTaskResponse:
    new_id = get_next_id("tasks")

    task = {
        "id": new_id,
        "title": request.title,
    }

    FAKE_DB["tasks"].append(task)

    return CreateTaskResponse(
        id=task["id"],  # type: ignore
        title=task["title"],  # type: ignore
    )

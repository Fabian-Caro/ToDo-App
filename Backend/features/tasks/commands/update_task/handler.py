from features.tasks.commands.update_task.request import UpdateTaskRequest
from features.tasks.commands.update_task.response import UpdateTaskResponse
from infrastructure.fake_db import FAKE_DB


def execute(request: UpdateTaskRequest) -> UpdateTaskResponse | None:
    task = next((task for task in FAKE_DB["tasks"] if task["id"] == request.id), None)

    if task is None:
        return None

    task["title"] = request.title

    return UpdateTaskResponse(
        id=task["id"], title=task["title"], is_completed=task["is_completed"]
    )

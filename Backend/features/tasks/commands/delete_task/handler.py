from features.tasks.commands.delete_task.request import DeleteTaskRequest
from features.tasks.commands.delete_task.response import DeleteTaskResponse
from infrastructure.fake_db import FAKE_DB


def execute(request: DeleteTaskRequest) -> DeleteTaskResponse | None:
    task = next((task for task in FAKE_DB["tasks"] if task["id"] == request.id), None)

    if task is None:
        return None

    response = DeleteTaskResponse(
        id=task["id"], title=task["title"], is_completed=task["is_completed"]
    )

    FAKE_DB["tasks"].remove(task)

    return response

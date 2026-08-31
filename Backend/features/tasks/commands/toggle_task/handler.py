from features.tasks.commands.toggle_task.request import ToggleTaskRequest
from features.tasks.commands.toggle_task.response import ToggleTaskResponse
from infrastructure.fake_db import FAKE_DB


def execute(request: ToggleTaskRequest) -> ToggleTaskResponse | None:
    task = next((task for task in FAKE_DB["tasks"] if task["id"] == request.id), None)

    if task is None:
        return None

    task["is_completed"] = not task["is_completed"]

    response = ToggleTaskResponse(
        id=task["id"], title=task["title"], is_completed=task["is_completed"]
    )

    return response

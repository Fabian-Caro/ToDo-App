from features.tasks.commands.delete_task.request import DeleteTaskRequest
from infrastructure.fake_db import FAKE_DB


def execute(delete_task_request: DeleteTaskRequest) -> bool:
    task = next(
        (task for task in FAKE_DB["tasks"] if task["id"] == delete_task_request.id),
        None,
    )

    if task is None:
        return False

    FAKE_DB["tasks"].remove(task)

    return True

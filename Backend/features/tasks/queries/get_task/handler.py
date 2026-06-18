from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse
from infrastructure.fake_db import FAKE_DB


def execute(request: GetTaskRequest) -> GetTaskResponse | None:
    task = next((task for task in FAKE_DB["tasks"] if task["id"] == request.id), None)

    if task is None:
        return None

    return GetTaskResponse(id=task["id"], title=task["title"])

from features.tasks.commands.delete_task.request import DeleteTaskRequest
from features.tasks.shared.repository import TaskRepository
from infrastructure.fake_db import FAKE_DB


repository = TaskRepository()


def execute(delete_task_request: DeleteTaskRequest) -> bool:
    task = repository.get_by_id(delete_task_request.id)

    if task is None:
        return False

    repository.delete(task)

    return True

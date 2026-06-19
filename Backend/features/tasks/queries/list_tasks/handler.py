from features.tasks.queries.list_tasks.response import ListTasksResponse, TaskItem
from infrastructure.fake_db import FAKE_DB


def execute() -> ListTasksResponse:
    raw_tasks = FAKE_DB["tasks"]

    task_items = [TaskItem(**task) for task in raw_tasks]

    return ListTasksResponse(tasks=task_items)

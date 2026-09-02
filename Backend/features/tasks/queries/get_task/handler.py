from fastapi import Request
from features.tasks.queries.get_task.request import GetTaskRequest
from features.tasks.queries.get_task.response import GetTaskResponse
from features.tasks.shared.links import build_task_links
from infrastructure.database.unit_of_work import UnitOfWork


def execute(
    request: Request,
    get_task_request: GetTaskRequest,
) -> GetTaskResponse | None:

    with UnitOfWork() as uow:
        task = uow.tasks.get_by_id(get_task_request.id)

        if task is None:
            return None

        assert task.id is not None

        return GetTaskResponse(
            id=task.id,
            title=task.title,
            is_completed=task.is_completed,
            links=build_task_links(request, task.id),
        )

from fastapi import Request
from features.tasks.commands.update_task.request import UpdateTaskRequest
from features.tasks.commands.update_task.response import UpdateTaskResponse
from features.tasks.shared.links import build_task_links
from infrastructure.database.unit_of_work import UnitOfWork


def execute(
    request: Request,
    update_task_request: UpdateTaskRequest,
    uow: UnitOfWork,
) -> UpdateTaskResponse | None:

    task = uow.tasks.get_by_id(update_task_request.id)

    if task is None:
        return None

    task.title = update_task_request.title
    task.is_completed = update_task_request.is_completed

    uow.tasks.save(task)
    uow.commit()

    assert task.id is not None

    return UpdateTaskResponse(
        id=task.id,
        title=task.title,
        is_completed=task.is_completed,
        links=build_task_links(request, task.id),
    )

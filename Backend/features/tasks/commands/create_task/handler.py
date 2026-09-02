from fastapi import Request
from features.tasks.commands.create_task.request import CreateTaskRequest
from features.tasks.commands.create_task.response import CreateTaskResponse
from features.tasks.shared.links import build_task_links
from infrastructure.database.unit_of_work import UnitOfWork


def execute(
    request: Request,
    create_task_request: CreateTaskRequest,
) -> CreateTaskResponse:

    with UnitOfWork() as uow:
        task = uow.tasks.create(create_task_request.title)
        uow.commit()

        assert task.id is not None

        return CreateTaskResponse(
            id=task.id,
            title=task.title,
            is_completed=task.is_completed,
            links=build_task_links(request, task.id),
        )

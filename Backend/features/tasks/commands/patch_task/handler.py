from fastapi import Request

from features.tasks.commands.patch_task.request import PatchTaskRequest
from features.tasks.commands.patch_task.response import PatchTaskResponse
from features.tasks.shared.links import build_task_links
from infrastructure.database.unit_of_work import UnitOfWork


def execute(
    request: Request,
    patch_task_request: PatchTaskRequest,
) -> PatchTaskResponse | None:

    with UnitOfWork() as uow:
        task = uow.tasks.get_by_id(patch_task_request.id)

        if task is None:
            return None

        if patch_task_request.title is not None:
            task.title = patch_task_request.title

        if patch_task_request.is_completed is not None:
            task.is_completed = patch_task_request.is_completed

        uow.tasks.save(task)
        uow.commit()

        assert task.id is not None

        return PatchTaskResponse(
            id=task.id,
            title=task.title,
            is_completed=task.is_completed,
            links=build_task_links(request, task.id),
        )

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from features.tasks.commands.delete_task.handler import execute
from features.tasks.commands.delete_task.request import DeleteTaskRequest
from infrastructure.database.dependencies import get_uow
from infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter()


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="delete_task",
)
def delete_task(task_id: int, uow: Annotated[UnitOfWork, Depends(get_uow)]) -> Response:
    delete_task_request = DeleteTaskRequest(id=task_id)
    was_deleted = execute(delete_task_request, uow)

    if not was_deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

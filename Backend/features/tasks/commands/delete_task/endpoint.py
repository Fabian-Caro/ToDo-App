from fastapi import APIRouter, HTTPException, status, Response

from features.tasks.commands.delete_task.handler import execute
from features.tasks.commands.delete_task.request import DeleteTaskRequest


router = APIRouter()


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="delete_task",
)
def delete_task(task_id: int) -> Response:
    delete_task_request = DeleteTaskRequest(id=task_id)
    was_deleted = execute(delete_task_request)

    if not was_deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

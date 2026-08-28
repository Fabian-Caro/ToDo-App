from fastapi import APIRouter, HTTPException

from features.tasks.commands.delete_task.handler import execute
from features.tasks.commands.delete_task.request import DeleteTaskRequest
from features.tasks.commands.delete_task.response import DeleteTaskResponse

router = APIRouter()


@router.delete("/{task_id}", response_model=DeleteTaskResponse, name="delete_task")
def delete_task(task_id: int) -> DeleteTaskResponse | None:
    request = DeleteTaskRequest(id=task_id)
    response = execute(request)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

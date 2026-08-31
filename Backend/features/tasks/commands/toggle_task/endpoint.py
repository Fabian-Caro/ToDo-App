from fastapi import APIRouter, HTTPException

from features.tasks.commands.toggle_task.handler import execute
from features.tasks.commands.toggle_task.request import ToggleTaskRequest
from features.tasks.commands.toggle_task.response import ToggleTaskResponse

router = APIRouter()


@router.patch(
    "/{task_id}/toggle", response_model=ToggleTaskResponse, name="toggle_task"
)
def toggle_task(task_id: int):
    request = ToggleTaskRequest(id=task_id)
    response = execute(request)

    if response is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return response

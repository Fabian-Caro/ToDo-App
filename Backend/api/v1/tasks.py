from fastapi import APIRouter

from features.tasks.commands.create_task.endpoint import router as create_task_router
from features.tasks.commands.delete_task.endpoint import router as delete_task_router
from features.tasks.commands.toggle_task.endpoint import router as toggle_task_router
from features.tasks.commands.update_task.endpoint import router as update_task_router
from features.tasks.queries.get_task.endpoint import router as get_task_router
from features.tasks.queries.list_tasks.endpoint import router as list_tasks_router
from features.tasks.queries.search_tasks.endpoint import router as search_tasks_router

router = APIRouter(prefix="/tasks", tags=["TASKS"])

router.include_router(create_task_router)
router.include_router(update_task_router)
router.include_router(toggle_task_router)
router.include_router(delete_task_router)
router.include_router(search_tasks_router)
router.include_router(get_task_router)
router.include_router(list_tasks_router)

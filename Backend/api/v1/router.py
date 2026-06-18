from fastapi import APIRouter

from api.v1.tasks import router as tasks_router

router = APIRouter(prefix="/v1")

router.include_router(tasks_router)

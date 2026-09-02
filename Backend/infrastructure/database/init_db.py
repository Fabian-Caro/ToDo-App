from sqlmodel import SQLModel
from infrastructure.database.engine import engine
from infrastructure.database.models.task import Task


def init_db() -> None:
    SQLModel.metadata.create_all(engine)

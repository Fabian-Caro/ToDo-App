from infrastructure.database.models.task import Task
from sqlmodel import Session, select


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, title: str) -> Task:
        task = Task(title=title)

        self.session.add(task)
        self.session.flush()
        self.session.refresh(task)

        return task

    def get_by_id(self, task_id: int) -> Task | None:
        return self.session.get(Task, task_id)

    def list(self) -> list[Task]:
        statement = select(Task)
        return list(self.session.exec(statement))

    def save(self, task: Task) -> Task:
        self.session.add(task)
        self.session.flush()
        self.session.refresh(task)

        return task

    def delete(self, task: Task) -> None:
        self.session.delete(task)

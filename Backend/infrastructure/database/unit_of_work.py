from sqlmodel import Session
from infrastructure.database.engine import engine
from features.tasks.shared.repository import TaskRepository


class UnitOfWork:
    def __init__(self):
        self.session = Session(engine)
        self.tasks = TaskRepository(self.session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            self.rollback()
        self.close()
        return False

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()

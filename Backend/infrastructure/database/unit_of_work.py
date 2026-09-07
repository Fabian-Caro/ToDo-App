from features.tasks.shared.repository import TaskRepository
from sqlmodel import Session


class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.tasks = TaskRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()

from features.tasks.shared.repository import TaskRepository


class UnitOfWork:
    def __init__(self):
        self.tasks = TaskRepository()

    def commit(self):
        pass

    def rollback(self):
        pass

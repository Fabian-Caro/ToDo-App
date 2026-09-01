from infrastructure.database.fake_db import FAKE_DB, get_next_id


class TaskRepository:
    def create(self, title: str) -> dict:
        task = {
            "id": get_next_id("tasks"),
            "title": title,
            "is_completed": False,
        }

        FAKE_DB["tasks"].append(task)

        return task

    def get_by_id(self, task_id: int) -> dict | None:
        return next(
            (task for task in FAKE_DB["tasks"] if task["id"] == task_id),
            None,
        )

    def list(self) -> list[dict]:
        return FAKE_DB["tasks"].copy()

    def save(self, task: dict) -> dict:
        for index, current_task in enumerate(FAKE_DB["tasks"]):
            if current_task["id"] == task["id"]:
                FAKE_DB["tasks"][index] = task
                return task

        raise ValueError(f"Task with id {task['id']} not found.")

    def delete(self, task: dict) -> None:
        FAKE_DB["tasks"].remove(task)
        
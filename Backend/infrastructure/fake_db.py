from typing import Dict, List, Any

def gen_tasks(amount: int) -> List[Dict[str, Any]]:
    return [
        {
            "id": task_id,
            "title": f"Aprender concepto {task_id}",
            "is_completed": task_id % 3 == 0
        }
        for task_id in range(1, amount + 1)
    ]

FAKE_DB: Dict[str, List[Dict[str, Any]]] = {
    "tasks": gen_tasks(50)
}

_counters: Dict[str, int] = {
    "tasks": 51
}

def get_next_id(table_name: str) -> int:
    current_id = _counters[table_name]
    _counters[table_name] += 1
    return current_id
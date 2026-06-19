from typing import Dict, List, Any

FAKE_DB: Dict[str, List[Dict[str, Any]]] = {
    "tasks": [
        {"id": 1, "title": "Aprender VSA", "is_completed": False},
        {"id": 2, "title": "Aprender CQRS", "is_completed": False},
    ]
}

_counters: Dict[str, int] = {
    "tasks": 3
}

def get_next_id(table_name: str) -> int:
    current_id = _counters[table_name]
    _counters[table_name] += 1
    return current_id
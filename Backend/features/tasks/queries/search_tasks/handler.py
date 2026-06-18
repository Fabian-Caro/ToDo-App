from infrastructure.fake_db import FAKE_DB
from features.tasks.queries.search_tasks.request import SearchTaskRequest
from features.tasks.queries.search_tasks.response import SearchTaskResponse, SearchTaskItem

def execute(request: SearchTaskRequest) -> SearchTaskResponse:
    search_term = request.query.lower()
    filtered_tasks = [
        task for task in FAKE_DB["tasks"]
        if search_term in task["title"].lower()
    ]

    results = [
        SearchTaskItem(id=task["id"], title=task["title"])
        for task in filtered_tasks
    ]

    return SearchTaskResponse(
        results=results,
        total_results=len(results)
    )


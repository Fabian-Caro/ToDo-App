from features.tasks.queries.list_tasks.response import ListTasksResponse, TaskItem, Pagination

from infrastructure.fake_db import FAKE_DB


def execute(page: int, page_size: int) -> ListTasksResponse:
    raw_tasks = FAKE_DB["tasks"]
    
    total = len(raw_tasks)
    
    start = (page - 1) * page_size
    end = start + page_size
    
    paginated_tasks = raw_tasks[start:end]

    task_items = [
        TaskItem(**task)
        for task in paginated_tasks
    ]
    
    total_pages = (total + page_size - 1) // page_size
    
    has_next = page < total_pages
    has_previous = page > 1
    
    next_page = page + 1 if has_next else None
    previous_page = page - 1 if has_previous else None

    return ListTasksResponse(
        tasks=task_items,
        pagination=Pagination(
            page=page,
            page_size=page_size,
            total=total,
            total_pages=total_pages,
            has_next=has_next,
            has_previous=has_previous,
            next_page=next_page,
            previous_page=previous_page,
        ),
    )
from typing import Literal

from fastapi import Request

from features.tasks.queries.list_tasks.response import (
    ListTasksResponse, 
    TaskItem, 
    Pagination, 
    PaginationLinks,
    TaskLinks,
)

from infrastructure.fake_db import FAKE_DB


def build_task_url(request: Request, task_id: int) -> str:
    return str(request.url_for("get_task", task_id=task_id))

def build_page_url(request: Request, page: int) -> str:
    return str(request.url.include_query_params(page=page))


def execute(
    request: Request,
    page: int, 
    page_size: int,
    is_completed: bool | None,
    sort_by: Literal["id", "title"],
    sort_order: Literal["asc", "desc"],
) -> ListTasksResponse:
    raw_tasks = FAKE_DB["tasks"]
    
    if is_completed is not None:
        raw_tasks = [
            task
            for task in raw_tasks
            if task["is_completed"] == is_completed
        ]
        
    raw_tasks = sorted(
        raw_tasks,
        key=lambda task: (task[sort_by], task["id"]),
        reverse=sort_order == "desc",
    )
    
    total = len(raw_tasks)
    
    offset = (page - 1) * page_size
    
    paginated_tasks = raw_tasks[offset:offset + page_size]

    task_items = [
        TaskItem(
            **task,
            links=TaskLinks(
                self=build_task_url(request, task["id"]),
            ),
        )
        for task in paginated_tasks
    ]
    
    total_pages = (total + page_size - 1) // page_size
    
    has_next = page < total_pages
    has_previous = page > 1
    
    next_page = page + 1 if has_next else None
    previous_page = page - 1 if has_previous else None
    
    links = PaginationLinks(
        self=build_page_url(request, page),
        first=build_page_url(request, 1),
        previous=(
            build_page_url(request, previous_page)
            if previous_page is not None
            else None
        ),
        next=(
            build_page_url(request, next_page)
            if next_page is not None
            else None
        ),
        last=build_page_url(request, total_pages or 1),
    )

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
            links=links,
        ),
    )

from fastapi import Request
from features.tasks.queries.search_tasks.request import SearchTaskRequest
from features.tasks.queries.search_tasks.response import (
    Pagination,
    PaginationLinks,
    SearchTaskItem,
    SearchTaskResponse,
    TaskLinks,
)
from infrastructure.database.unit_of_work import UnitOfWork


def build_page_url(request: Request, page: int) -> str:
    return str(request.url.include_query_params(page=page))


def build_task_url(request: Request, task_id: int) -> str:
    return str(request.url_for("get_task", task_id=task_id))


def execute(
    request: Request,
    search_request: SearchTaskRequest,
    uow: UnitOfWork,
) -> SearchTaskResponse:

    search_term = search_request.query.lower()

    filtered_tasks = [
        task for task in uow.tasks.list() if search_term in task.title.lower()
    ]

    if search_request.is_completed is not None:
        filtered_tasks = [
            task
            for task in filtered_tasks
            if task.is_completed == search_request.is_completed
        ]

    filtered_tasks = sorted(
        filtered_tasks,
        key=lambda task: (getattr(task, search_request.sort_by), task.id),
        reverse=search_request.sort_order == "desc",
    )

    total = len(filtered_tasks)
    offset = (search_request.page - 1) * search_request.page_size
    paginated_task = filtered_tasks[offset : offset + search_request.page_size]

    total_page = (total + search_request.page_size - 1) // search_request.page_size

    has_next = search_request.page < total_page
    has_previous = search_request.page > 1

    next_page = search_request.page + 1 if has_next else None
    previous_page = search_request.page - 1 if has_previous else None

    results = [
        SearchTaskItem(
            id=task.id,
            title=task.title,
            is_completed=task.is_completed,
            links=TaskLinks(
                self=build_task_url(request, task.id),
            ),
        )
        for task in paginated_task
        if task.id is not None
    ]

    links = PaginationLinks(
        self=build_page_url(request, search_request.page),
        first=build_page_url(request, 1),
        previous=(
            build_page_url(request, previous_page)
            if previous_page is not None
            else None
        ),
        next=(build_page_url(request, next_page) if next_page is not None else None),
        last=build_page_url(request, total_page or 1),
    )

    return SearchTaskResponse(
        results=results,
        pagination=Pagination(
            page=search_request.page,
            page_size=search_request.page_size,
            total=total,
            total_pages=total_page,
            has_next=has_next,
            has_previous=has_previous,
            next_page=next_page,
            previous_page=previous_page,
            links=links,
        ),
    )

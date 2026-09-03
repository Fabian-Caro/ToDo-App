from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from infrastructure.database.session import get_session
from infrastructure.database.unit_of_work import UnitOfWork
from sqlmodel import Session


def get_uow(
    session: Annotated[Session, Depends(get_session)],
) -> Generator[UnitOfWork, None, None]:
    uow = UnitOfWork(session)
    try:
        yield uow
    except Exception:
        uow.rollback()
        raise
        
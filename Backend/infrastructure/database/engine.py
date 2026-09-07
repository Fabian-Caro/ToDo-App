from core.settings import settings
from sqlmodel import create_engine

connect_args = {}

if settings.database_url.startswith("sqlite"):
    connect_args["check_same_thread"] = False


engine = create_engine(
    settings.database_url,
    echo=True,
    connect_args=connect_args,
)

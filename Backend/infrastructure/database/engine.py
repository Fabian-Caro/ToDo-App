from core.settings import settings
from sqlmodel import create_engine

database_url = settings.database_url

connect_args = {}

if database_url.startswith("sqlite"):
    connect_args["check_same_thread"] = False

elif database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1,
    )


engine = create_engine(
    database_url,
    echo=True,
    connect_args=connect_args,
)

from core.settings import settings
from sqlmodel import create_engine

engine = create_engine(
    settings.database_url,
    echo=True,
    connect_args={"check_same_thread": False},
)

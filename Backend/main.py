from api.v1.router import router as v1_router
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from infrastructure.database.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api")


@app.get("/")
def root(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "Hello": "World!",
        "message": "API",
        "links": {
            "tasks": f"{base_url}/api/v1/tasks/",
        },
    }


def main():
    print("Hello from backend!")


if __name__ == "__main__":
    main()

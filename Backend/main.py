from api.v1.router import router as v1_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api")

BASE_URL = "http://127.0.0.1:8000"


@app.get("/")
def root():
    return {"Hello": "World!", "links": {"tasks": f"{BASE_URL}/api/v1/tasks/"}}


def main():
    print("Hello from backend!")


if __name__ == "__main__":
    main()

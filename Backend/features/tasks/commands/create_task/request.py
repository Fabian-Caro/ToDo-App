from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    title: str
    
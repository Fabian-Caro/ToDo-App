from pydantic import BaseModel


class GetTaskRequest(BaseModel):
    id: int

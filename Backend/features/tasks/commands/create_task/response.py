from pydantic import BaseModel

class CreateTaskResponse(BaseModel):
    id: int
    title: str
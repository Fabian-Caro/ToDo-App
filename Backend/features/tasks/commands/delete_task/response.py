from pydantic import BaseModel

class DeleteTaskResponse(BaseModel):
    id: int
    title: str
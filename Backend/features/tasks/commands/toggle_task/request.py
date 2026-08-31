from pydantic import BaseModel

class ToggleTaskRequest(BaseModel):
    id: int
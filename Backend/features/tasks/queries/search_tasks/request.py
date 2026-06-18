from pydantic import BaseModel, Field

class SearchTaskRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Texto a buscar en el título")
    
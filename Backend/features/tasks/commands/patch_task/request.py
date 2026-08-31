from pydantic import BaseModel, Field, model_validator


class PatchTaskPayload(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    is_completed: bool | None = None

    @model_validator(mode="after")
    def validate_at_least_one_field(self):
        if self.title is None and self.is_completed is None:
            raise ValueError("At least one field must be provided")

        if "title" in self.model_fields_set and self.title is None:
            raise ValueError("title cannot be null")

        if "is_completed" in self.model_fields_set and self.is_completed is None:
            raise ValueError("is_completed cannot be null")

        return self


class PatchTaskRequest(BaseModel):
    id: int
    title: str | None = None
    is_completed: bool | None = None

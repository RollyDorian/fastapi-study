from pydantic import BaseModel, Field


class MLModel(BaseModel):
    name: str
    accuracy: float = Field(ge=0, le=1, description="Accuracy of the model between 0 and 1")


class ModelUpdate(BaseModel):
    name: str | None = None
    accuracy: float | None = Field(default=None, ge=0, le=1, description="Accuracy of the model between 0 and 1")


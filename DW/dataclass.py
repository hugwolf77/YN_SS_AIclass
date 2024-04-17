from pydantic import BaseModel, Field


class DataInput(BaseModel):
    model_id : str = Field(min_length=4, max_length=10)

class PredictOutput(BaseModel):
    prediction : int

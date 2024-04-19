<<<<<<< HEAD
from pydantic import BaseModel, Field


class DataInput(BaseModel):
    NM : str = Field(min_length=4, max_length=10)
    x : list[float] = Field()

class PredictOutput(BaseModel):
    prediction : int
=======

# DataInput, PredictOutput

class DataInput:
    pass

class PredictOutput:
    pass
>>>>>>> 3cd6eb6bb7eb525c69047d742d55caede138e7dd

import uuid
from pydantic import BaseModel, Field

""" DB model connect sqlalchemy """

class Base_model(BaseModel):
    """Base_model"""
    pk: uuid.UUID
    name: str
    
    class Config:
        from_attributes = True


""" model Input Data specify """

class DataInput(BaseModel):
    NM : str = Field(min_length=4, max_length=10)
    x : list[float] = Field()

class PredictOutput(BaseModel):
    prediction : int

""" 
data name : CSCIDS2017
target file count : 8 -> table 8
columns count  : 79 * 8  = 632
total row count : ??    

sample => balance data file : 1

"""

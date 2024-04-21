from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from DW.db.session import Base


class Test_Table(Base):
    __tablename__ = "test_Table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    
# #- app dataclass

# from pydantic import BaseModel, Field

# class DataInput(BaseModel):
#     NM : str = Field(min_length=4, max_length=10)
#     x : list[float] = Field()

# class PredictOutput(BaseModel):
#     prediction : int
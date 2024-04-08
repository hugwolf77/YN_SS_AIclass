from typing import Optional, List
from fastapi import APIRouter, Depends

# from DW.db.preprocessor import preprocess
from DW.dataclass import DataInput, PredictOutput

from core.config import Config
from ML_BASE.ML_main import ML_runway


NN01 = APIRouter(
    prefix="/NN01", # url 앞에 고정적으로 붙는 prefix path 추가
) # root에서 분리된 경로


@NN01.get("/") # Route Path
async def NN01_branch():
    return {'msg' : 'this is model NN01'}

@NN01.post("/predict", tags=['NN01'], response_model=PredictOutput)
async def NN01_predict(request_input: DataInput):
    model_id = request_input.model_id
    model = ML_runway(model_id)
    result =  model.predict()
    return {'prediction' : result}
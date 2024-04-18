from typing import Optional, List

import datetime, psutil
import asyncio

from easycharts import ChartServer
from easyschedule import EasyScheduler

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



# from DW.db.preprocessor import preprocess
from API_app.model.dataclass import DataInput, PredictOutput

from core.config import Config
from ML_BASE.ML_main import ML_runway

templates = Jinja2Templates(directory="API_app/templates")

NN01 = APIRouter(
    prefix="/NN01", # url 앞에 고정적으로 붙는 prefix path 추가
    tags=['NN01'],
    responses={404:{"description":"Not found"}}
) # root에서 분리된 경로

@NN01.get("/", response_class=HTMLResponse) # Route Path
async def NN01_branch_home(request: Request):
   # return {'msg' : 'this is model NN01'}
   return templates.TemplateResponse("NN01_home.html",{"request":request})

@NN01.post("/predict", tags=['NN01'], response_model=PredictOutput)
async def NN01_predict(request_input: DataInput):
    NM = request_input.NM
    model = ML_runway(NM)
    result =  model.predict()
    return {'prediction' : result}
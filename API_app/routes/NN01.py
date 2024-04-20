import sys
import json
import logging
import random
from datetime import datetime
from typing import Iterator

import psutil

import asyncio

from contextlib import asynccontextmanager

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# from DW.db.preprocessor import preprocess
from API_app.model.dataclass import DataInput, PredictOutput

from core.config import Config
from ML_BASE.ML_main import ML_runway

# logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


templates = Jinja2Templates(directory="API_app/templates")

ml_models = {}


@asynccontextmanager
async def lifespan(app: APIRouter, NM):
    # Load the ML model
    model = ML_runway(NM)
    ml_models["NN01"] = model.predict
    # ml_models["chart"] = charts_setup
    yield
    ml_models.clear()

NN01 = APIRouter(
    prefix="/NN01", # url 앞에 고정적으로 붙는 prefix path 추가
    tags=['NN01'],
    responses={404:{"description":"Not found"}},
    lifespan=lifespan
) # root에서 분리된 경로
NN01.mount("/static", StaticFiles(directory="API_app/static"), name="static")

random.seed()

@NN01.get("/", response_class=HTMLResponse) # Route Path
async def NN01_branch_home(request: Request):
   # return {'msg' : 'this is model NN01'}
   return templates.TemplateResponse("NN01_home.html",{"request":request})

### model
async def generate_random_data(request: Request):
    """
    Generates random value between 0 and 100
    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host
    logger.info("Client %s connected", client_ip)
    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": random.random() * 100,
            }
        )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

@NN01.get("/chart-data")
async def chart_data(request: Request):
    response = StreamingResponse(generate_random_data(request), media_type="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"

    # time_label = []
    # value_list = []
    # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # value = random.random() * 100
    # time_label.pop().append(time)
    # value_list.pop().append(value)

    # data = { "data" : 
    #             { 
    #                 "time" : time,
    #                 "value": value
    #                 },
    #         }
    # data_json = json.dumps(data, ensure_ascii=False)
    return templates.TemplateResponse("charts_example_01.html",{"request":request, "response":data_json})

@NN01.post("/predict", tags=['NN01'], response_model=PredictOutput)
async def NN01_predict(request_input: DataInput):
   result =  ml_models["NN01"](request_input.x)
   return {'prediction' : result}
from fastapi import APIRouter
import torch

from API_app.model.dataclass import DataInput, PredictOutput
from core.config import Config

from ML_BASE.ML_operate.operator import prediction, validation, training
from ML_BASE.ML_models.LSTM_ex01 import RNN
from ML_BASE.ML_main import ML_runway

modelConfig = Config("NN01",0, 16)

hidden_sizes = [288, 192, 144, 96, 32]
max_learning_rate = 0.001
epochs = 41

input_size = 0
seq_len = 0

model = RNN(input_size, hidden_sizes, seq_len, dropout=0.5, output_size=1)

model.eval()

test = APIRouter(prefix='/test')

@test.get('/', tags=['test'])
async def start_test():
    return {'msg' : 'this is test'}

@test.post('/predict', tags=['test'], response_model=PredictOutput)
async def start_test(request_Input:DataInput):
    NM = request_Input.NM
    model = ML_runway(NM)
    result =  model.predict()
    return {'prediction' : result}    
from fastapi import APIRouter
import torch

from DW.dataclass import DataInput, PredictOutput
from core.config import Config

from ML_BASE.ML_operate.operator import prediction, validation, training
from ML_BASE.ML_models.LSTM_ex01 import RNN

modelConfig = Config("NN01",0, 16)

hidden_sizes = [288, 192, 144, 96, 32]
max_learning_rate = 0.001
epochs = 41

model = RNN(input_size, hidden_sizes, seq_len, dropout=0.5, output_size=1)

model.eval()

test = APIRouter(prefix='/test')

@test.get('/', tags=['test'])
async def start_test():
    return {'msg' : 'this is test'}

@test.post('/predict', tags=['test'], response_model=PredictOutput)
async def start_test(request_Input:DataInput):
    
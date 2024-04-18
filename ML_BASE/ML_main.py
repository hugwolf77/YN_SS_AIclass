from ML_BASE.ML_operate.operator import prediction, validation, training
from ML_BASE.ML_models.LSTM_ex01 import RNN
from ML_BASE.ML_dataloader import dataloader

model_class = { 
            "NN01" : {
                        "model" : RNN,
                        "loader" : dataloader,
                        "trainer" : training,
                        "validater" : validation,
                        "predicter" : prediction,
                     }
            }

class ML_runway:
    def __init__(self, NM, device="cpu") -> None:
       self.model = model_class[NM]["model"]
       self.loader = model_class[NM]["loader"] 
       self.device = device
       self.predicter = model_class[NM]["predicter"]
    
    def predict(self):
        return self.predicter(self.model, self.loader, self.device)
        



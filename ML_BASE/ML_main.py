from ML_BASE.ML_operate.operator import prediction, validation, training
from ML_BASE.ML_models.LSTM_ex01 import RNN
from ML_BASE.ML_data_provider.data_factory import data_provider

class ML_runway:
   def __init__(self, NM, device="cpu") -> None:
      self.device = device
      self.model = MODEL_CLASS[NM]["model"]
      self.loader = MODEL_CLASS[NM]["loader"] 
      self.predicter = MODEL_CLASS[NM]["predicter"]
      self.agg = MODEL_CONFIG[NM]
       
   def train(self):
      pass
   
   def validation(self):
      pass
    
   def predict(self):
      return self.predicter(self.model, self.loader, self.device)
        

MODEL_CLASS = { 
            "NN01" : {
                        "model" : RNN,
                        "loader" : data_provider,
                        "trainer" : training,
                        "validater" : validation,
                        "predicter" : prediction,
                     },
            
            "NN01" : {
                        "model" : RNN,
                        "loader" : data_provider,
                        "trainer" : training,
                        "validater" : validation,
                        "predicter" : prediction,
                     }
            
            }

MODEL_CONFIG = {
                        "NN01" : {
                                    "batch_size" : 16,
                                    "hidden_sizes" : [288, 192, 144, 96, 32],
                                    "max_learning_rate" : 0.001,
                                    "epochs" : 100,
                                    "input_size" : 0,
                                    "seq_len" : 0,
                                    "dropout" : 0.5,
                                    "output_size" : 1,
                                    "save_path" : "./",
                                }
                   }     


import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    DB_USERNAME : str = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST : str = os.getenv("DB_HOST","localhost")
    DB_PORT : str = os.getenv("DB_PORT",3306)
    DB_DATABASE : str = os.getenv("DB_DATABASE")
	
    DATABASE_URL = 'sqlite:///./Items.db'
    # DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

class Config:
    def __init__(self, model_id, gpu_id, batch_size):
    	# model full name. 모델 저장 경로
        self.model_id = model_id
        # cuda 사용 시, gpu id
        self.gpu_id = gpu_id
        self.batch_size = batch_size


settings = Settings()
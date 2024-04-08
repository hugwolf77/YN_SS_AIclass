# main.py

import os
from typing import Optional
from fastapi import FastAPI
import uvicorn

from API_app.routes.NN01 import NN01 


app = FastAPI() # FastAPI 모듈

app.include_router(NN01) # 다른 route파일들을 불러와 포함시킴

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework",
    }
    
if __name__ == "__main__":
    uvicorn.run("yn_ss_aiclass:app", host='0.0.0.0', port=8000, reload=True)
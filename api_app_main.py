# api_app_main.py
import sys
import os
# from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from API_app.routes.NN01 import NN01 

app = FastAPI() # FastAPI 모듈 docs_url="/documentation", redoc_url=None)
print(f"pwd: {os.getcwd()}")
app.mount("/static", StaticFiles(directory="./API_app/static"), name="static")

templates = Jinja2Templates(directory="./API_app/templates")

app.include_router(NN01) # 다른 route파일들을 불러와 포함시킴

@app.get("/", response_class=HTMLResponse) # Route root Path
def root_index(request: Request):
    # return {"Python": "Framework",}
    return templates.TemplateResponse(
        request=request, name="root_index.html")
    
if __name__ == "__main__":
    uvicorn.run("api_app_main:app", host='127.0.0.1', port=8000, reload=True)
   # uvicorn.run("api_app_main:app", host='127.0.0.1', port=8000, log_level="debug", reload=True)
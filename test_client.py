import json
from datetime import datetime
from pytz import timezone

import aiohttp
import asyncio

import requests


URL = 'http://127.0.0.1:8000/NN01/service-data'

with requests.get(url=URL, stream=True) as r:
    for chunk in r.iter_content(100):
        print(f"Time: {datetime.now(timezone('Asia/Seoul'))}, data: {chunk}")

# async def get_json_events(url=URL):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url) as resp:
#             while True:
#                 chunk = await resp.content.readline()
#                 await asyncio.sleep(1)
                
#                 if not chunk:
#                     break
#                 yield json.loads(chunk.decode("utf-8"))
                
# async def main():
#     async for event in get_json_events(URL):
#         print(event)
        
# if __name__=="__main__":
#     asyncio.run(main())
import time
import json
import matplotlib.pyplot as plt
import asyncio
from requests import Session

class realTime_Graph:
    def __init__(self, url):
        self.url = url
        self.time = list(range(100))
        self.value = list(range(100))

    async def receive_data(self):
        session = Session()
        with session.get(self.url, headers=None, stream=True) as res:
            for data in res.iter_lines():
                event = json.loads(data)
                # print(f"time : {event["time"]},  value : {event["value"]}")
                graph_data = dict(event)
                time.sleep(0.9)
                await self.update_graph(graph_data)
            
    async def update_graph(self, graph_data):
        
        self.time = self.time[1:]
        self.time.append(self.time[-1]+1)
        self.value = self.value[1:]
        self.value.append(graph_data['value'])
        plt.clf()
        plt.plot(self.time, self.value)
        plt.xlabel('step')
        plt.ylabel('value')
        plt.title('fake-Stream data graph')
        plt.pause(0.1)

    def start(self):
        asyncio.run(self.receive_data())

if __name__ == '__main__':
    url = "http://127.0.0.1:8000/NN01/fakeStream"
    realtime = realTime_Graph(url)
    realtime.start()
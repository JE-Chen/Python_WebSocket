import asyncio
import websockets

class WebSocket_Client:

    def __init__(self,Uri):
        asyncio.get_event_loop().run_until_complete(self.Hello_Server(Uri))

    async def Hello_Server(self,Uri):
        async with websockets.connect(Uri) as websocket:
            await websocket.send("Hello Server")
            print(await websocket.recv())


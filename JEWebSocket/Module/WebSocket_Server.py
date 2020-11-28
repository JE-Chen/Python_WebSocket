import asyncio

import websockets


class WebSocket_Server:

    def __init__(self, Address, Port):
        self.Server = websockets.serve(self.Message, Address, Port)
        asyncio.get_event_loop().run_until_complete(self.Server)
        asyncio.get_event_loop().run_forever()

    async def Message(self, websocket, path):
        async for message in websocket:
            print(message)
            message = input()
            await websocket.send(message)

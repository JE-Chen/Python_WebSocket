import os

os.chdir("/home/circleci/project/")

from JEWebSocket.Module.WebSocket_Client import WebSocket_Client

Client = WebSocket_Client('ws://localhost:5555')

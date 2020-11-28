import os

os.chdir("/home/circleci/project/")

from JEWebSocket.Module.WebSocket_Server import WebSocket_Server

Server = WebSocket_Server("localhost", 5555)

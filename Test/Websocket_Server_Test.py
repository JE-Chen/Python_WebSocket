import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"Python_WebSocket"))
from Python_WebSocket import WebSocket_Server

Server = WebSocket_Server("localhost", 5555)


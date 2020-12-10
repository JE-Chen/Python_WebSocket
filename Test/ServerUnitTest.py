import unittest
import JEWebSocket

class TestServer(unittest.TestCase):

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def testServer(self):
        websocket = JEWebSocket.Module.WebsocketServer.WebsocketServer("localhost", 5555)


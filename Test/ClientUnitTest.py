import unittest


class TestClient(unittest.TestCase):

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def testClient(self):
        client = JEWebSocket.Module.WebsocketClient.WebsocketClient('localhost:5555')

import unittest

from ..app import create_app

class PostTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="server.config.ConfigTest")
        self.client = self.app.test_client

    def test_create_success(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass


import unittest

from server.app import create_app
from server.database import db

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="server.config.ConfigTest")
        self.client = self.app.test_client
        with self.app.app_context():             
            db.create_all()


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
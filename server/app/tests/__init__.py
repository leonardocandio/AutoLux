import unittest

from flask_login import FlaskLoginClient

from server.app.blueprints.shop.models.car import Car
from server.app.blueprints.users.models.role import Role
from server.app import create_app
from server.database import db


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config="server.config.ConfigTest")
        self.client = self.app.test_client
        with self.app.app_context():
            db.create_all()
            Car.create_first_car()
            Role.insert_roles()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

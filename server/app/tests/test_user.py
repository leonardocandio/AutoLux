import json

from flask import request
from flask_login import FlaskLoginClient
from . import BaseTestClass


class UserTest(BaseTestClass):

    def setUp(self):
        super().setUp()
        self.app.test_login_client = FlaskLoginClient
        self.new_user = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

    def test_get_user_profile_success(self):
        self.client().post('/users/', json=self.new_user)
        res = self.client().get('/users/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['user'])

    def test_get_user_profile_failed_404(self):
        self.client().post('/users/', json=self.new_user)
        self.client().post('/users/session', json=self.new_user)
        res = self.client().get('/users/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['title'], "Página no encontrada")



    def test_log_in_failed(self):
        res = self.client().post('/users/session', json=self.new_user)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_log_out_success(self):
        self.client().post('/users/', json=self.new_user)
        self.client().post('/users/session', json=self.new_user)
        res = self.client().delete('/users/session')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'], 'logout success')
from . import BaseTestClass
import json

class CarTest(BaseTestClass):

   #---------------Carros---------------
    def test_get_cars_success(self):
        res = self.client().get('/cars/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_cars'])
        self.assertTrue(len(data['cars']))

    def test_get_cars_sent_requesting_beyond_valid_page_404(self):
        res = self.client().get('/cars/?page=10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['title'], 'Página no encontrada')

    def test_search_cars_by_nombre_success(self):
        res = self.client().post('/cars/?search=toyota')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cars']))

    def test_search_cars_by_nombre_failed_404(self):
        res = self.client().post('/cars/?search=WAAA')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['title'], 'Página no encontrada')


    def test_filter_cars_success(self):
        res = self.client().post('/cars/', json={'year': '2022'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_cars'])


    def test_filter_cars_failed_404(self):
        res = self.client().post('/cars/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['title'], 'Página no encontrada')


new_user = {
    'username': 'test',
    'email': 'test@test.com',
    'password': 'test'
}


class UserTest(BaseTestClass):

    def get_user_profile_success(self):
        self.client().post('/users/', json=new_user)
        res = self.client().get('/users/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['user'])

    def get_user_profile_failed_404(self):
        res = self.client().get('/users/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['title'], "Página no encontrada")

    def log_in_success(self):
        self.client().post('/users/', json=new_user)
        self.client().delete('/users/session/')
        res = self.client().post('/users/session/', json=new_user)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['user']['username'], 'test')

    def log_in_failed_401(self):
        res = self.client().post('/users/session', json=new_user)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def log_out_success(self):
        self.client().post('/users/', json=new_user)
        self.client().post('/users/session', json=new_user)
        res = self.client().delete('/users/session')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'], 'logout success')

    def log_out_failed_401(self):
        res = self.client().delete('/users/session')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

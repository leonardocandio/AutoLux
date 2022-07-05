from . import BaseTestClass
import json

class CarTest(BaseTestClass):

   #---------------Carros---------------
    def test_get_cars_success(self):
        res = self.client().get('/cars')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_cars'])
        self.assertTrue(len(data['cars']))

    def test_get_cars_sent_requesting_beyond_valid_page_404(self):
        res = self.client().get('/cars?page=10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_search_cars_by_nombre_success(self):
        res = self.client().post('/cars', json={'search': 'new'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['cars'])
        self.assertTrue(data['total_cars'])

    def test_search_cars_by_nombre_failed_404(self):
        res = self.client().post('/cars', json={'search': 'new'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    def test_filter_pelicula_success(self):
        res = self.client().post('/peliculas/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '1')
        self.assertTrue(len(data['cars']) == 0)
        self.assertTrue(data['total_cars'] == 0)

    def test_filter_pelicula_failed_404(self):
        res = self.client().post('/peliculas/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


from rest_framework.test import APITestCase


class HelloViewTests(APITestCase):
    def test_returns_greeting(self):
        response = self.client.get('/api/hello/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, you.', 'status': 'nuh uh.'})

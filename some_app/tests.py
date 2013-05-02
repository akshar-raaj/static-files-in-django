from django.test import TestCase, Client

class SomeAppTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_home(self):
        resp = self.c.get('/some_app/home')
        self.assertEqual(resp.status_code, 200)

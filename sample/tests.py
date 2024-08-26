from django.test import TestCase
from django.urls import reverse_lazy


class HealthTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_health(self):
        url = reverse_lazy("api-1.0.0:health")
        self.assertEqual(url, '/sample/health/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

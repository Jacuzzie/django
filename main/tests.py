from django.test import TestCase
from django.urls import reverse

class TestHome(TestCase):
    def test_status(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response, 200)

from django.test import TestCase
from django.urls import reverse_lazy


class IndexTest(TestCase):
    def test_get_index(self):
        response = self.client.get(reverse_lazy('index'))

        self.assertContains(
            response,
            "Under Construction",
            status_code=200
        )

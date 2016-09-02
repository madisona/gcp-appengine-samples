
from django import test
from django.core.urlresolvers import reverse


class SampleTest(test.TestCase):

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(200, response.status_code)

    def test_class_view(self):
        response = self.client.get(reverse("class"))
        self.assertEqual(200, response.status_code)

    def test_error_view(self):
        with self.assertRaises(Exception):
            self.client.get(reverse("error"))

    def test_health_check_view(self):
        response = self.client.get(reverse("health_check"))
        self.assertEqual(200, response.status_code)

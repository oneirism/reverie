from django.test import TestCase

from reverie import wsgi


class WSGITest(TestCase):
    def test_create_application(self):
        application = wsgi.application
        self.assertIsNotNone(application)

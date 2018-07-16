from django.apps import apps
from django.test import TestCase

from splash.apps import SplashConfig


class SplashConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(SplashConfig.name, 'splash')
        self.assertEqual(apps.get_app_config('splash').name, 'splash')

from django.apps import apps
from django.test import TestCase

from campaign.apps import CampaignConfig


class CampaignConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(CampaignConfig.name, 'campaign')
        self.assertEqual(apps.get_app_config('campaign').name, 'campaign')

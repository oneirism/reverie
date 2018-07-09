from django.test import TestCase

from campaign.models import Campaign


class CampaignTest(TestCase):
    def test_create_campaign(self):
        name = "Test Campaign"

        campaign = {
            'game_master_id': 1,
            'name': name,
            'description': 'Test description.',
        }

        campaign = Campaign.objects.create(**campaign)

        self.assertTrue(isinstance(campaign, Campaign))
        self.assertEqual(campaign.name, name)

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase

from campaign.admin import CampaignAdmin
from campaign.models import Campaign


class CampaignAdminTest(TestCase):
    def test_admin_model(self):
        name = "Test Campaign"

        gm = {
            'username': 'testgm',
            'password': 'testpw',
        }
        gm = User.objects.create_user(**gm)

        campaign = {
            'game_master_id': gm.id,
            'name': name,
            'description': 'Test description.',
        }

        campaign = Campaign.objects.create(**campaign)

        self.assertTrue(isinstance(campaign, Campaign))
        self.assertEqual(campaign.name, name)

        ca = CampaignAdmin(campaign, AdminSite())

        self.assertTrue(isinstance(ca, CampaignAdmin))

        self.assertEqual(ca.list_display, ['name'])
        self.assertEqual(ca.list_display_links, ['name'])
        self.assertEqual(ca.search_fields, ['name'])

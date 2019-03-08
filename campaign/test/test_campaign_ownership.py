import json

from campaign.models import Campaign
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.urls import reverse

GM_USER = 'gm'
PLAYER_USER = 'player'
NOT_PLAYER_USER = 'not_player'

TEST_PASSWORD = 'password'
TEST_USERS = [GM_USER, PLAYER_USER, NOT_PLAYER_USER]

TEST_CAMPAIGNS = [
    {
        'name': 'Private Campaign',
        'gm_id': TEST_USERS.index(GM_USER),
        'tagline': 'Test Tagline',
        'description': 'Test Description',
        'players': [TEST_USERS.index(PLAYER_USER)],
        'public': False,
    },
    {
        'name': 'Public Campaign',
        'gm_id': TEST_USERS.index(GM_USER),
        'tagline': 'Test Tagline',
        'description': 'Test Description',
        'players': [TEST_USERS.index(PLAYER_USER)],
        'public': True,
    }

]

class CampaignOwnershipTest(TestCase):
    def create_campaign(self, name, gm_id, description, players, public=False):
        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        form_data = {
            'name': name,
            'description': description,
            'tagline': 'Test Tagline',
            'players': players,
            'public': public,
        }

        response = self.client.post(reverse('campaign:campaign_entry'), form_data)
        campaign = Campaign.objects.get(name=name)
        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(campaign.name)}))

        self.client.logout()

        return campaign


    def setUp(self):
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

        for campaign in TEST_CAMPAIGNS:
            self.create_campaign(campaign['name'], campaign['gm_id'], campaign['description'], campaign['players'], campaign['public'])

    def test_anonymous_index(self):
        response = self.client.get(reverse('campaign:campaign_index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Public Campaign')

    def test_player_index(self):
        self.client.login(
            username=PLAYER_USER,
            password=TEST_PASSWORD,
        )

        response = self.client.get(reverse('campaign:campaign_index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Public Campaign')
        self.assertContains(response, 'Private Campaign')
        self.assertContains(response, 'Campaigns You Play')

    def test_protected_campaign(self):
        resp = self.client.login(
            username=NOT_PLAYER_USER,
            password=TEST_PASSWORD,
        )

        # FIXME(devenney): This smells.
        response = self.client.get(reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGNS[0].get("name"))}))

        self.assertEqual(response.status_code, 403)

    def test_public_campaign(self):
        resp = self.client.login(
            username=NOT_PLAYER_USER,
            password=TEST_PASSWORD,
        )

        # FIXME(devenney): This smells.
        response = self.client.get(reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGNS[1].get("name"))}))

        self.assertEqual(response.status_code, 200)

    def test_gm_edit_campaign(self):
        campaign = Campaign.objects.get(id=1)

        form_data = {
            'name': 'New Name',
            'description': 'New Description',
            'tagline': 'Test Tagline',
            'players': [2],
            'public': campaign.public,
        }

        resp = self.client.login(
            username=GM_USER,
            password=TEST_PASSWORD,
        )

        response = self.client.post(reverse('campaign:campaign_edit', kwargs={"campaign_slug": campaign.slug}), form_data)

        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={"campaign_slug": slugify(campaign.name)}))

        new_campaign = Campaign.objects.get(id=1)
        self.assertEqual(new_campaign.name, 'New Name')

    def test_player_cannot_edit_campaign(self):
        campaign = Campaign.objects.get(id=1)

        form_data = {
            'name': 'New Name',
            'description': 'New Description',
            'tagline': 'Test Tagline',
            'players': [2],
            'public': campaign.public,
        }

        resp = self.client.login(
            username=PLAYER_USER,
            password=TEST_PASSWORD,
        )

        response = self.client.post(reverse('campaign:campaign_edit', kwargs={"campaign_slug": campaign.slug}), form_data)

        self.assertEqual(response.status_code, 403)

        new_campaign = Campaign.objects.get(id=1)
        self.assertNotEqual(new_campaign.name, 'New Name')

    def test_gm_sees_campaign(self):
        gm_id = 1

        players = [2]

        campaign = self.create_campaign("Test", gm_id, "Test Description", players)

        self.assertTrue(isinstance(campaign, Campaign))

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.get(reverse('campaign:campaign_edit', args=[slugify(campaign.name)]))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('campaign:campaign_detail', args=[slugify(campaign.name)]))
        self.assertEqual(response.status_code, 200)

    def test_player_autocomplete(self):
        prefix = 'test'

        # Unauthenticated

        response = self.client.get(reverse('campaign:player_autocomplete'), args=prefix)

        body = json.loads(response.content)

        for user in TEST_USERS:
            if str.startswith(user, prefix):
                self.assertTrue(any(result['text'] == user for result in body['results']))

        # Authenticated

        for user in TEST_USERS:
            self.client.login(username=user, password=TEST_PASSWORD)

            response = self.client.get(reverse('campaign:player_autocomplete'), args=prefix)
            body = json.loads(response.content)

            self.assertTrue(not any(result['text'] == user for result in body['results']))

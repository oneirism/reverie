from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.urls import reverse

from campaign.models import Campaign, Character, Faction, Item, Location, Log

GM_USER = 'gm'
PLAYER_USER = 'player'
NOT_PLAYER_USER = 'not_player'

TEST_PASSWORD = 'password'
TEST_USERS = [GM_USER, PLAYER_USER, NOT_PLAYER_USER]

TEST_CAMPAIGN = {
    'name': 'Public Campaign',
    'gm_id': TEST_USERS.index(GM_USER),
    'tagline': 'Test Tagline',
    'description': 'Test Description',
    'players': [TEST_USERS.index(PLAYER_USER)],
    'public': True,
}

TEST_PLAYER_CHARACTER = {
    'name': 'Test Player Character',
    'tagline': 'Test Tagline',
    'description': 'Test Description',
    'player': TEST_USERS.index(PLAYER_USER),
    'campaign_slug': 1,
    'is_pc': True,
}

TEST_NON_PLAYER_CHARACTER = {
    'name': 'Test Non-Player Character',
    'tagline': 'Test Tagline',
    'description': 'Test Description',
    'player': TEST_USERS.index(PLAYER_USER),
    'campaign_slug': 1,
    'is_pc': False,
}

TEST_FACTION = {
    'name': 'Test Faction',
    'tagline': 'Test Tagline',
    'description': 'Test Description',
    'campaign_slug': 1,
}

TEST_ITEM = {
    'name': 'Test Item',
    'tagline': 'Test Tagline',
    'description': 'Test Description',
    'campaign_slug': 1,
}

TEST_LOCATION = {
    'name': 'Test Location',
    'tagline': 'Test Tagline',
    'description': 'Test Description',
    'campaign_slug': 1,
}

TEST_LOG = {
    'name': 'Test Log',
    'description': 'Test Description',
    'date': '01/01/2001',
    'campaign_slug': 1,
}


class CampaignViewTest(TestCase):
    """ Test cases related to the Character view. """

    def setUp(self):
        # Create Users
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

    def test_create_campaign(self):
        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        # Create Campaigns
        response = self.client.post(reverse('campaign:campaign_entry'), TEST_CAMPAIGN)
        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGN.get("name"))}))
        self.campaign = Campaign.objects.get(name = 'Public Campaign')

        # Logout
        self.client.logout()


    def test_invalid_campaign_entry(self):
        # Missing name
        bad_campaign_form = {
            'gm_id': TEST_USERS.index(GM_USER),
            'tagline': 'Test Tagline',
            'description': 'Test Description',
            'players': [TEST_USERS.index(PLAYER_USER)],
            'public': True,
        }

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:campaign_entry'), bad_campaign_form)
        self.assertEqual(response.status_code, 200)

        self.client.logout()


class CharacterViewTest(TestCase):
    """ Test cases related to the Character view. """

    def setUp(self):
        # Create Users
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        # Create Campaigns
        response = self.client.post(reverse('campaign:campaign_entry'), TEST_CAMPAIGN)
        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGN.get("name"))}))
        self.campaign = Campaign.objects.get(name = 'Public Campaign')

        # Create Characters
        response = self.client.post(reverse('campaign:character_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), TEST_PLAYER_CHARACTER)
        self.assertRedirects(response, reverse('campaign:character_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(TEST_PLAYER_CHARACTER.get("name"))}))
        self.player_character = Character.objects.get(name = 'Test Player Character')

        response = self.client.post(reverse('campaign:character_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), TEST_NON_PLAYER_CHARACTER)
        self.assertRedirects(response, reverse('campaign:character_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(TEST_NON_PLAYER_CHARACTER.get("name"))}))
        self.non_player_character = Character.objects.get(name = 'Test Non-Player Character')

        # Ensure character is visible
        response = self.client.get(reverse('campaign:character_list', kwargs={'campaign_slug': slugify(self.campaign.name)}))
        self.assertContains(response, 'Test Player Character', status_code=200)
        self.assertContains(response, 'Test Non-Player Character', status_code=200)

        # Logout
        self.client.logout()


    def test_invalid_character_entry(self):
        # Missing name
        bad_character_form = {
            'tagline': 'Test tagline.',
            'description': 'Test description',
            'player': TEST_USERS.index(PLAYER_USER),
            'campaign_slug': 1,
        }

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:character_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), bad_character_form)
        self.assertEqual(response.status_code, 200)

        self.client.logout()

    def test_gm_edit_character(self):
        new_character = TEST_NON_PLAYER_CHARACTER
        new_character['tagline'] = 'New tagline!'

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:character_edit', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(self.non_player_character.name)}), new_character)
        self.assertRedirects(response, reverse('campaign:character_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(self.non_player_character.name)}))

        character = Character.objects.get(slug=slugify(self.non_player_character.name))

        self.assertEqual(character.tagline, 'New tagline!')

        self.client.logout()


    def test_player_edit_character(self):
        new_character = TEST_PLAYER_CHARACTER
        new_character['tagline'] = 'New tagline!'

        self.client.login(username=PLAYER_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:character_edit', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(self.player_character.name)}), new_character)
        self.assertRedirects(response, reverse('campaign:character_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(self.player_character.name)}))

        character = Character.objects.get(slug=slugify(self.player_character.name))

        self.assertEqual(character.tagline, 'New tagline!')

        self.client.logout()


    def test_not_player_edit_character(self):
        new_character = TEST_PLAYER_CHARACTER
        new_character['tagline'] = 'New tagline!'

        self.client.login(username=NOT_PLAYER_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:character_edit', kwargs={'campaign_slug': slugify(self.campaign.name), 'character_slug': slugify(self.player_character.name)}), new_character)
        self.assertEqual(response.status_code, 403)

        self.client.logout()


class FactionViewTest(TestCase):
    """ Test cases related to the Faction view. """

    def setUp(self):
        # Create Users
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        # Create Campaigns
        response = self.client.post(reverse('campaign:campaign_entry'), TEST_CAMPAIGN)
        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGN.get("name"))}))
        self.campaign = Campaign.objects.get(name = 'Public Campaign')

        # Create Factions
        response = self.client.post(reverse('campaign:faction_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), TEST_FACTION)
        self.assertRedirects(response, reverse('campaign:faction_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'faction_slug': slugify(TEST_FACTION.get("name"))}))
        self.faction = Faction.objects.get(name = 'Test Faction')

        # Ensure faction is visible
        response = self.client.get(reverse('campaign:faction_list', kwargs={'campaign_slug': slugify(self.campaign.name)}))
        self.assertContains(response, 'Test Faction', status_code=200)

        # Logout
        self.client.logout()


    def test_invalid_faction_entry(self):
        # Missing name
        bad_faction_form = {
            'tagline': 'Test tagline.',
            'description': 'Test description',
            'campaign_slug': 1,
        }

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:faction_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), bad_faction_form)
        self.assertEqual(response.status_code, 200)

        self.client.logout()


    def test_edit_faction(self):
        new_faction = TEST_FACTION
        new_faction['tagline'] = 'New tagline!'

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:faction_edit', kwargs={'campaign_slug': slugify(self.campaign.name), 'faction_slug': slugify(self.faction.name)}), new_faction)
        self.assertRedirects(response, reverse('campaign:faction_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'faction_slug': slugify(self.faction.name)}))

        faction = Faction.objects.get(slug=slugify(self.faction.name))

        self.assertEqual(faction.tagline, 'New tagline!')

        self.client.logout()


class ItemViewTest(TestCase):
    """ Test cases related to the Item view. """

    def setUp(self):
        # Create Users
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        # Create Campaigns
        response = self.client.post(reverse('campaign:campaign_entry'), TEST_CAMPAIGN)
        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGN.get("name"))}))
        self.campaign = Campaign.objects.get(name = 'Public Campaign')

        # Create Items
        response = self.client.post(reverse('campaign:item_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), TEST_ITEM)
        self.assertRedirects(response, reverse('campaign:item_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'item_slug': slugify(TEST_ITEM.get("name"))}))
        self.item = Item.objects.get(name = 'Test Item')

        # Ensure item is visible
        response = self.client.get(reverse('campaign:item_list', kwargs={'campaign_slug': slugify(self.campaign.name)}))
        self.assertContains(response, 'Test Item', status_code=200)

        # Logout
        self.client.logout()


    def test_invalid_item_entry(self):
        # Missing name
        bad_item_form = {
            'tagline': 'Test tagline.',
            'description': 'Test description',
            'campaign_slug': 1,
        }

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:item_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), bad_item_form)
        self.assertEqual(response.status_code, 200)

        self.client.logout()


    def test_edit_item(self):
        new_item = TEST_ITEM
        new_item['tagline'] = 'New tagline!'

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:item_edit', kwargs={'campaign_slug': slugify(self.campaign.name), 'item_slug': slugify(self.item.name)}), new_item)
        self.assertRedirects(response, reverse('campaign:item_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'item_slug': slugify(self.item.name)}))

        item = Item.objects.get(slug=slugify(self.item.name))

        self.assertEqual(item.tagline, 'New tagline!')

        self.client.logout()


class LocationViewTest(TestCase):
    """ Test cases related to the Location view. """

    def setUp(self):
        # Create Users
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        # Create Campaigns
        response = self.client.post(reverse('campaign:campaign_entry'), TEST_CAMPAIGN)

        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGN.get("name"))}))
        self.campaign = Campaign.objects.get(name = 'Public Campaign')

        # Create Locations
        response = self.client.post(reverse('campaign:location_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), TEST_LOCATION)
        self.assertRedirects(response, reverse('campaign:location_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'location_slug': slugify(TEST_LOCATION.get("name"))}))
        self.location = Location.objects.get(name = 'Test Location')

        # Ensure location is visible
        response = self.client.get(reverse('campaign:location_list', kwargs={'campaign_slug': slugify(self.campaign.name)}))
        self.assertContains(response, 'Test Location', status_code=200)

        # Logout
        self.client.logout()


    def test_invalid_location_entry(self):
        # Missing name
        bad_location_form = {
            'tagline': 'Test tagline.',
            'description': 'Test description',
            'campaign_slug': 1,
        }

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:location_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), bad_location_form)
        self.assertEqual(response.status_code, 200)

        self.client.logout()


    def test_edit_location(self):
        new_location = TEST_LOCATION
        new_location['tagline'] = 'New tagline!'

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:location_edit', kwargs={'campaign_slug': slugify(self.campaign.name), 'location_slug': slugify(self.location.name)}), new_location)
        self.assertRedirects(response, reverse('campaign:location_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'location_slug': slugify(self.location.name)}))

        location = Location.objects.get(slug=slugify(self.location.name))

        self.assertEqual(location.tagline, 'New tagline!')

        self.client.logout()


class LogViewTest(TestCase):
    """ Test cases related to the Log view. """

    def setUp(self):
        # Create Users
        for idx, user in enumerate(TEST_USERS):
            User.objects.create_user(
                id=TEST_USERS.index(user),
                password=TEST_PASSWORD,
                username=user,
            )

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        # Create Campaigns
        response = self.client.post(reverse('campaign:campaign_entry'), TEST_CAMPAIGN)
        self.assertRedirects(response, reverse('campaign:campaign_detail', kwargs={'campaign_slug': slugify(TEST_CAMPAIGN.get("name"))}))
        self.campaign = Campaign.objects.get(name = 'Public Campaign')

        # Create Logs
        response = self.client.post(reverse('campaign:log_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), TEST_LOG)
        self.assertRedirects(response, reverse('campaign:log_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'log_slug': slugify(TEST_LOG.get("name"))}))
        self.log = Log.objects.get(name = 'Test Log')

        # Ensure log is visible
        response = self.client.get(reverse('campaign:log_list', kwargs={'campaign_slug': slugify(self.campaign.name)}))
        self.assertContains(response, 'Test Log', status_code=200)

        # Logout
        self.client.logout()


    def test_invalid_log_entry(self):
        # Missing description
        bad_log_form = {
            'name': 'Test Log',
            'description': '',
        }

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:log_entry', kwargs={'campaign_slug': slugify(self.campaign.name)}), bad_log_form)
        self.assertEqual(response.status_code, 200)

        self.client.logout()


    def test_edit_log(self):
        new_log = TEST_LOG
        new_log['description'] = 'New description!'

        self.client.login(username=GM_USER, password=TEST_PASSWORD)

        response = self.client.post(reverse('campaign:log_edit', kwargs={'campaign_slug': slugify(self.campaign.slug), 'log_slug': slugify(self.log.slug)}), new_log)
        self.assertRedirects(response, reverse('campaign:log_detail', kwargs={'campaign_slug': slugify(self.campaign.name), 'log_slug': slugify(self.log.name)}))

        log = Log.objects.get(slug=slugify(self.log.name))

        self.assertEqual(log.description, 'New description!')

        self.client.logout()

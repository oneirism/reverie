""" Campaign model test cases. """

from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from campaign.models import Campaign, Character, Faction, Item, Location, Log


class CampaignTest(TestCase):
    """ Test cases related to the Campaign model. """
    def setUp(self):
        """ Set up models required for testing. """

        name = "Test Campaign"

        campaign = {
            'game_master_id': 1,
            'name': name,
            'description': 'Test description.',
        }

        player = {
            'username': 'testuser',
            'password': 'testpw',
        }

        self.campaign = Campaign.objects.create(**campaign)
        self.player = User.objects.create_user(**player)


    def test_create_campaign(self):
        """ Test Campaign model creation. """
        campaign = self.campaign

        self.assertTrue(isinstance(campaign, Campaign))
        self.assertEqual(campaign.name, "Test Campaign")


    def test_add_players(self):
        """ Test Campaign player addition. """
        campaign = self.campaign

        campaign.players.add(1)

        self.assertQuerysetEqual(campaign.players.all(), [self.player], transform=lambda x: x)


class CharacterTest(TestCase):
    """ Test cases related to the Character model.

    TODO: Test player ownership.

    """
    def setUp(self):
        self.character_raw = {
            'name': 'Test Character',
            'tagline': 'Test tagline.',
            'player_id': 1,
            'campaign_id': 1,
        }

        self.character = Character.objects.create(**self.character_raw)


    def test_create_character(self):
        """ Test Character model creation. """
        character = self.character

        self.assertTrue(isinstance(character, Character))
        self.assertEqual(character.name, "Test Character")


    def test_str(self):
        """ Test informal printable string representation. """
        character = self.character

        self.assertEqual(str(character), self.character_raw['name'])


class FactionTest(TestCase):
    """ Test cases related to the Faction model. """
    def setUp(self):
        self.faction_raw = {
            'name': 'Test Faction',
            'tagline': 'Test tagline.',
            'campaign_id': 1,
        }

        self.faction = Faction.objects.create(**self.faction_raw)


    def test_create_faction(self):
        """ Test Faction model creation. """
        faction = self.faction

        self.assertTrue(isinstance(faction, Faction))
        self.assertEqual(faction.name, "Test Faction")


    def test_str(self):
        """ Test informal printable string representation. """
        faction = self.faction

        self.assertEqual(str(faction), self.faction_raw['name'])


class ItemTest(TestCase):
    """ Test cases related to the Item model. """
    def setUp(self):
        self.item_raw = {
            'name': 'Test Item',
            'campaign_id': 1,
        }

        self.item = Item.objects.create(**self.item_raw)


    def test_create_item(self):
        """ Test Item model creation. """
        item = self.item

        self.assertTrue(isinstance(item, Item))
        self.assertEqual(item.name, "Test Item")


    def test_str(self):
        """ Test informal printable string representation. """
        item = self.item

        self.assertEqual(str(item), self.item_raw['name'])


class LocationTest(TestCase):
    """ Test cases related to the Location model. """
    def setUp(self):
        self.location_raw = {
            'name': 'Test Location',
            'campaign_id': 1,
        }

        self.location = Location.objects.create(**self.location_raw)


    def test_create_location(self):
        """ Test Location model creation. """
        location = self.location

        self.assertTrue(isinstance(location, Location))
        self.assertEqual(location.name, "Test Location")


    def test_str(self):
        """ Test informal printable string representation. """
        location = self.location

        self.assertEqual(str(location), self.location_raw['name'])


class LogTest(TestCase):
    """ Test cases related to the Log model. """
    def setUp(self):
        self.log_raw = {
            'title': 'Test Log',
            'description': 'Test Description',
            'date': datetime(2010, 9, 12),
            'campaign_id': 1,
        }

        self.log = Log.objects.create(**self.log_raw)


    def test_create_log(self):
        """ Test Log model creation. """
        log = self.log

        self.assertTrue(isinstance(log, Log))
        self.assertEqual(log.title, "Test Log")


    def test_str(self):
        """ Test informal printable string representation. """
        log = self.log

        self.assertEqual(str(log), self.log_raw['title'])

from django.test import TestCase
from campaign.models import Campaign, Character, Faction, Location

from .utils import *


class CampaignTest(TestCase):
    def test_create_campaign(self):
        campaign_name="Test Campaign"

        campaign = create_campaign(campaign_name)

        self.assertTrue(isinstance(campaign, Campaign))
        self.assertEqual(campaign.__str__(), "Test Campaign")


class CharacterTest(TestCase):
    def test_create_character(self):
        campaign_name = "Test Campaign"
        character_name = "Test Character"
        faction_name = "Test Faction"
        location_name = "Test Location"

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)
        location = create_location(campaign, location_name)

        character = create_character(campaign, faction, location, character_name)

        self.assertTrue(isinstance(character, Character))
        self.assertEqual(character.__str__(), "Test Character")
        self.assertEqual(character.campaign, campaign)
        self.assertEqual(character.faction, faction)
        self.assertEqual(character.location, location)


class FactionTest(TestCase):
    def test_create_faction(self):
        campaign_name="Test Campaign"
        faction_name="Test Faction"

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)

        self.assertTrue(isinstance(faction, Faction))
        self.assertEqual(faction.__str__(), "Test Faction")


class LocationTest(TestCase):
    def test_create_location(self):
        campaign_name="Test Campaign"
        location_name="Test Location"

        campaign = create_campaign(campaign_name)
        location = create_location(campaign, location_name)

        self.assertTrue(isinstance(location, Location))
        self.assertEqual(location.__str__(), "Test Location")

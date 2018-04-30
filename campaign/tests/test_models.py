import datetime

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
        self.assertEqual(character.__str__(), character_name)
        self.assertEqual(character.campaign, campaign)
        self.assertEqual(character.faction, faction)
        self.assertEqual(character.location, location)


    def test_create_character_slug(self):
        campaign_name = "Test Campaign"
        character_name = "Test Character"
        faction_name = "Test Faction"
        location_name = "Test Location"

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)
        location = create_location(campaign, location_name)

        character = create_character(campaign, faction, location, character_name)
        character2 = create_character(campaign, faction, location, character_name)

        self.assertNotEqual(character.slug, character2.slug)
        self.assertEqual(character.slug, "test-character")
        self.assertEqual(character2.slug, "test-character-1")


class FactionTest(TestCase):
    def test_create_faction(self):
        campaign_name="Test Campaign"
        faction_name="Test Faction"

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)

        self.assertTrue(isinstance(faction, Faction))
        self.assertEqual(faction.__str__(), faction_name)


    def test_create_faction_slug(self):
        campaign_name="Test Campaign"
        faction_name="Test Faction"

        campaign = create_campaign(campaign_name)

        faction = create_faction(campaign, faction_name)
        faction2 = create_faction(campaign, faction_name)

        self.assertNotEqual(faction.slug, faction2.slug)
        self.assertEqual(faction.slug, "test-faction")
        self.assertEqual(faction2.slug, "test-faction-1")


class LocationTest(TestCase):
    def test_create_location(self):
        campaign_name="Test Campaign"
        location_name="Test Location"

        campaign = create_campaign(campaign_name)
        location = create_location(campaign, location_name)

        self.assertTrue(isinstance(location, Location))
        self.assertEqual(location.__str__(), location_name)


    def test_create_location_slug(self):
        campaign_name="Test Campaign"
        location_name="Test Location"

        campaign = create_campaign(campaign_name)
        location = create_location(campaign, location_name)
        location2 = create_location(campaign, location_name)

        self.assertNotEqual(location.slug, location2.slug)
        self.assertEqual(location.slug, "test-location")
        self.assertEqual(location2.slug, "test-location-1")


class LogEntryTest(TestCase):
    def test_create_log_entry(self):
        campaign_name="Test Campaign"
        log_entry_date = datetime.date.today()
        log_entry_title="Test Title"

        campaign = create_campaign(campaign_name)
        log_entry = create_log_entry(campaign, log_entry_date, log_entry_title)

        self.assertTrue(isinstance(log_entry, LogEntry))
        self.assertEqual(log_entry.__str__(), log_entry_title)


    def test_create_log_entry_slug(self):
        campaign_name="Test Campaign"
        log_entry_date = datetime.date.today()
        log_entry_title="Test Title"

        campaign = create_campaign(campaign_name)
        log_entry = create_log_entry(campaign, log_entry_date, log_entry_title)
        log_entry2 = create_log_entry(campaign, log_entry_date, log_entry_title)

        self.assertNotEqual(log_entry.slug, log_entry2.slug)
        self.assertEqual(log_entry.slug, "test-title")
        self.assertEqual(log_entry2.slug, "test-title-1")

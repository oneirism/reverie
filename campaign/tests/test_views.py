from django.test import TestCase
from django.urls import reverse

from campaign.models import Campaign, Character, Faction, Location

from .utils import *


def string_repr(obj: object):
    return '<{0}: {1}>'.format(obj.__class__.__name__, obj)


class CampaignViewTests(TestCase):
    def test_no_campaigns(self):
        response = self.client.get(reverse('campaign:campaign_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No campaigns are available.')
        self.assertQuerysetEqual(response.context['campaign_list'], [])

    def test_campaigns(self):
        campaign_name = 'Test campaign'
        campaign = create_campaign(campaign_name)

        response = self.client.get(reverse('campaign:campaign_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, campaign_name)
        self.assertQuerysetEqual(response.context['campaign_list'], [string_repr(campaign)])

    def test_campaign_detail(self):
        campaign_name = 'Test campaign'
        campaign = create_campaign(campaign_name)

        response = self.client.get(reverse('campaign:campaign_detail', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, campaign_name)

    def test_no_factions(self):
        campaign_name = 'Test campaign'
        campaign = create_campaign(campaign_name)

        response = self.client.get(reverse('campaign:faction_list', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No factions are available.')
        self.assertQuerysetEqual(response.context['faction_list'], [])

    def test_factions(self):
        campaign_name = 'Test campaign'
        faction_name = 'Test faction'

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)

        response = self.client.get(reverse('campaign:faction_list', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, faction_name)
        self.assertQuerysetEqual(response.context['faction_list'], [string_repr(faction)])

    def test_faction_detail(self):
        campaign_name = 'Test campaign'
        faction_name = 'Test faction'

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)

        response = self.client.get(reverse('campaign:faction_detail', args=[campaign.slug, faction.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, faction_name)

    def test_no_characters(self):
        campaign_name = 'Test campaign'
        campaign = create_campaign(campaign_name)

        response = self.client.get(reverse('campaign:character_list', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No characters are available.')
        self.assertQuerysetEqual(response.context['character_list'], [])

    def test_characters(self):
        campaign_name = 'Test campaign'
        character_name = 'Test character'
        faction_name = 'Test faction'
        location_name = 'Test location'

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)
        location = create_location(campaign, location_name)

        character = create_character(campaign, faction, location, character_name)

        response = self.client.get(reverse('campaign:character_list', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, character_name)
        self.assertQuerysetEqual(response.context['character_list'], [string_repr(character)])

    def test_character_detail(self):
        campaign_name = 'Test campaign'
        character_name = 'Test character'
        faction_name = 'Test faction'
        location_name = 'Test location'

        campaign = create_campaign(campaign_name)
        faction = create_faction(campaign, faction_name)
        location = create_location(campaign, location_name)

        character = create_character(campaign, faction, location, character_name)

        response = self.client.get(reverse('campaign:character_detail', args=[campaign.slug, character.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, character_name)
        self.assertContains(response, faction_name)
        self.assertContains(response, location_name)

    def test_no_locations(self):
        campaign_name = 'Test campaign'
        campaign = create_campaign(campaign_name)

        response = self.client.get(reverse('campaign:location_list', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No locations are available.')
        self.assertQuerysetEqual(response.context['location_list'], [])

    def test_locations(self):
        campaign_name = 'Test campaign'
        location_name = 'Test location'

        campaign = create_campaign(campaign_name)
        location = create_location(campaign, location_name)

        response = self.client.get(reverse('campaign:location_list', args=[campaign.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, location_name)
        self.assertQuerysetEqual(response.context['location_list'], [string_repr(location)])

    def test_location_detail(self):
        campaign_name = 'Test campaign'
        location_name = 'Test location'

        campaign = create_campaign(campaign_name)
        location = create_location(campaign, location_name)

        response = self.client.get(reverse('campaign:location_detail', args=[campaign.slug, location.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, location_name)


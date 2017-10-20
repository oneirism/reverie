import datetime

from campaign.models import Campaign, Character, Faction, Location, LogEntry


def create_campaign(campaign_name: str) -> Campaign:
    campaign = {
        'name': campaign_name,
        'description': 'Test description.',
        'tagline': 'Test tagline.'
    }

    return Campaign.objects.create(**campaign)


def create_character(campaign: Campaign, faction: Faction, location: Location, character_name: str) -> Character:
    character = {
        'campaign': campaign,
        'description': 'Test description.',
        'faction': faction,
        'location': location,
        'name': character_name,
        'tagline': 'Test tagline.'
    }

    return Character.objects.create(**character)


def create_faction(campaign: Campaign, faction_name: str) -> Faction:
    faction = {
        'campaign': campaign,
        'name': faction_name,
        'description': 'Test description.',
        'tagline': 'Test tagline.'
    }

    return Faction.objects.create(**faction)


def create_location(campaign: Campaign, location_name: str) -> Location:
    location = {
        'campaign': campaign,
        'name': location_name,
        'description': 'Test description.',
        'tagline': 'Test tagline.'
    }

    return Location.objects.create(**location)


def create_log_entry(campaign: Campaign, date: datetime, log_entry_title: str) -> LogEntry:
    log_entry = {
        'campaign': campaign,
        'date': date,
        'title': log_entry_title,
        'description': 'Test description'
    }

    return LogEntry.objects.create(**log_entry)

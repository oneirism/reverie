from campaign.models import Campaign, Character, Faction, Location


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

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig

from .models import Campaign, Character, Faction, Location, LogEntry
from .tables import CharacterTable


def campaign_list(request: HttpRequest) -> HttpResponse:
    campaign_list = Campaign.objects.order_by('name')

    context = {'campaign_list': campaign_list}
    return render(request, 'campaign/campaign_list.html', context)


def campaign_detail(request: HttpRequest, camp_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    context = {'campaign': campaign}
    return render(request, 'campaign/campaign_detail.html', context)


def character_list(request: HttpRequest, camp_slug:str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    character_list = Character.objects.filter(campaign=campaign).order_by('name')

    character_table = CharacterTable(character_list)
    RequestConfig(request).configure(character_table)

    context = {'campaign': campaign, 'character_list':character_list, 'table': character_table}
    return render(request, 'campaign/character_list.html', context)


def character_detail(request: HttpRequest, camp_slug: str, char_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    character = get_object_or_404(Character, slug=char_slug)

    context = {'campaign': campaign, 'character': character}
    return render(request, 'campaign/character_detail.html', context)


def faction_list(request: HttpRequest, camp_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    faction_list = Faction.objects.filter(campaign=campaign).order_by('name')

    context = {'campaign': campaign, 'faction_list':faction_list}
    return render(request, 'campaign/faction_list.html', context)


def faction_detail(request: HttpRequest, camp_slug: str, fact_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    faction = get_object_or_404(Faction, slug=fact_slug)

    context = {'campaign': campaign, 'faction': faction}
    return render(request, 'campaign/faction_detail.html', context)


def location_list(request: HttpRequest, camp_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    location_list = Location.objects.filter(campaign=campaign).order_by('name')

    context = {'campaign': campaign, 'location_list': location_list}
    return render(request, 'campaign/location_list.html', context)


def location_detail(request: HttpRequest, camp_slug: str, loc_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    location = get_object_or_404(Location, slug=loc_slug)

    context = {'campaign': campaign, 'location': location}
    return render(request, 'campaign/location_detail.html', context)


def log_entry_list(request: HttpRequest, camp_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    log_entry_list = LogEntry.objects.filter(campaign=campaign).order_by('date')

    context = {'campaign': campaign, 'log_entry_list': log_entry_list}
    return render(request, 'campaign/log_entry_list.html', context)


def log_entry_detail(request: HttpRequest, camp_slug: str, log_slug: str) -> HttpResponse:
    campaign = get_object_or_404(Campaign, slug=camp_slug)

    log = get_object_or_404(LogEntry, slug=log_slug)

    context = {'campaign': campaign, 'log': log}
    return render(request, 'campaign/log_entry_detail.html', context)

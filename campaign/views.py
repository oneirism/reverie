from dal import autocomplete
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CampaignEntryForm, CharacterEntryForm, FactionEntryForm, \
    ItemEntryForm, LocationEntryForm, LogEntryForm
from .models import Campaign, Character, Faction, Item, Location, Log
from . import utils


class PlayerAutocomplete(autocomplete.Select2QuerySetView):
    autocomplete_template = 'autocomplete_template.html'

    def get_queryset(self):
        qs = User.objects.exclude(id=self.request.user.id)

        return qs

    def get_result_label(self, result):
        label = result.username

        return label


def index(request):
    context = {}

    if request.user.is_authenticated:
        dm_campaigns = Campaign.objects.filter(
            game_master=request.user
        ).order_by('name')

        if dm_campaigns is not None:
            context['dm_campaigns'] = dm_campaigns

        player_campaigns = Campaign.objects.filter(
            players__id__exact=request.user.id
        ).order_by('name')

        if player_campaigns is not None:
            context['player_campaigns'] = player_campaigns

        public_campaigns = Campaign.objects.filter(
            public=True,
        ).exclude(
            game_master=request.user
        ).exclude(
            players__in=[request.user]
        ).order_by('name')

    else:
        public_campaigns = Campaign.objects.filter(
            public=True
        ).order_by('name')


    if public_campaigns is not None:
        context['public_campaigns'] = public_campaigns

    return render(request, 'campaign/index.html', context)


@utils.login_required
def new_campaign(request):
    form = CampaignEntryForm(request.POST or None, request.FILES or None)

    players = request.POST.getlist('players')

    if form.is_valid():
        campaign = form.save(commit=False)

        campaign.game_master_id = request.user.id
        campaign.save()
        campaign.players.set(players)
        campaign.save()

        return HttpResponseRedirect(reverse('campaign:campaign_detail', kwargs={'campaign_slug': campaign.slug}))

    context = {'form': form}

    return render(request, 'campaign/campaign_form.html', context)


@utils.login_required
@utils.is_gm
def campaign_edit(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    form = CampaignEntryForm(request.POST or None, request.FILES or None, instance=campaign)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('campaign:campaign_detail', kwargs={'campaign_slug': campaign_slug}))

    return render(request, 'campaign/campaign_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def campaign_detail(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    characters = Character.objects.filter(
        campaign = campaign
    )

    factions = Faction.objects.filter(
        campaign = campaign
    )

    items = Item.objects.filter(
        campaign = campaign
    )

    locations = Location.objects.filter(
        campaign = campaign
    )

    context = {
        'campaign': campaign,
        'characters': characters,
        'factions': factions,
        'items': items,
        'locations': locations
    }

    return render(request, 'campaign/campaign_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def character_list(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    player_characters = Character.objects.filter(
        campaign = campaign
    ).filter(
        is_pc = True
    ).order_by('name')

    non_player_characters = Character.objects.filter(
        campaign = campaign
    ).filter(
        is_pc = False
    ).order_by('name')

    context = {
        'campaign': campaign,
        'player_characters': player_characters,
        'non_player_characters': non_player_characters,
    }

    return render(request, 'campaign/character_list.html', context)

@utils.login_required
@utils.is_gm
def new_character(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    character = Character(campaign_id = campaign.id)

    form = CharacterEntryForm(request.POST or None, instance=character)

    if form.is_valid():
        character = form.save(commit=False)
        character.campaign_id = campaign.id
        character.save()

        return HttpResponseRedirect(reverse('campaign:character_detail', kwargs={'campaign_slug': campaign.slug, 'character_slug': character.slug}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/character_form.html', context)

@utils.login_required
@utils.can_edit_character
def character_edit(request, campaign_slug=None, character_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    character = get_object_or_404(Character, slug=character_slug)

    form = CharacterEntryForm(request.POST or None, request.FILES or None, instance=character)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'character': character,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('campaign:character_detail', kwargs={'campaign_slug': campaign.slug, 'character_slug': character.slug}))

    return render(request, 'campaign/character_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def character_detail(request, campaign_slug=None, character_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    character = get_object_or_404(Character, slug=character_slug)

    context = {
        'campaign': campaign,
        'character': character
    }

    return render(request, 'campaign/character_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def faction_list(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    factions = Faction.objects.filter(
        campaign = campaign
    )

    context = {
        'campaign': campaign,
        'factions': factions,
    }

    return render(request, 'campaign/faction_list.html', context)

@utils.login_required
@utils.is_gm
def new_faction(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    faction = Faction(campaign_id = campaign.id)

    form = FactionEntryForm(request.POST or None, request.FILES or None, instance=faction)

    if form.is_valid():
        faction = form.save(commit=False)
        faction.campaign_id = campaign.id
        faction.save()

        return HttpResponseRedirect(reverse('campaign:faction_detail', kwargs={'campaign_slug': campaign.slug, 'faction_slug': faction.slug}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/faction_form.html', context)

@utils.login_required
@utils.is_gm
def faction_edit(request, campaign_slug=None, faction_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    faction = get_object_or_404(Faction, slug=faction_slug)

    form = FactionEntryForm(request.POST or None, request.FILES or None, instance=faction)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'faction': faction,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('campaign:faction_detail', kwargs={'campaign_slug': campaign.slug, 'faction_slug': faction.slug}))

    return render(request, 'campaign/faction_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def faction_detail(request, campaign_slug=None, faction_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    faction = get_object_or_404(Faction, slug=faction_slug)

    context = {
        'campaign': campaign,
        'faction': faction
    }

    return render(request, 'campaign/faction_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def item_list(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    items = Item.objects.filter(
        campaign = campaign
    )

    context = {
        'campaign': campaign,
        'items': items,
    }

    return render(request, 'campaign/item_list.html', context)

@utils.login_required
@utils.is_gm
def new_item(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    item = Item(campaign_id = campaign.id)

    form = ItemEntryForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        item = form.save(commit=False)
        item.campaign_id = campaign.id
        item.save()

        return HttpResponseRedirect(reverse('campaign:item_detail', kwargs={'campaign_slug': campaign.slug, 'item_slug': item.slug}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/item_form.html', context)


@utils.login_required
@utils.is_gm
def item_edit(request, campaign_slug=None, item_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    item = get_object_or_404(Item, slug=item_slug)

    form = ItemEntryForm(request.POST or None, request.FILES or None, instance=item)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'item': item,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('campaign:item_detail', kwargs={'campaign_slug': campaign.slug, 'item_slug': item.slug}))

    return render(request, 'campaign/item_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def item_detail(request, campaign_slug=None, item_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    item = get_object_or_404(Item, slug=item_slug)

    context = {
        'campaign': campaign,
        'item': item
    }

    return render(request, 'campaign/item_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def location_list(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    locations = Location.objects.filter(
        campaign = campaign
    )

    context = {
        'campaign': campaign,
        'locations': locations,
    }

    return render(request, 'campaign/location_list.html', context)


@utils.login_required
@utils.is_gm
def new_location(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    location = Location(campaign_id = campaign.id)

    form = LocationEntryForm(request.POST or None, request.FILES or None, instance=location)

    if form.is_valid():
        location = form.save(commit=False)
        location.campaign_id = campaign.id
        location.save()

        return HttpResponseRedirect(reverse('campaign:location_detail', kwargs={'campaign_slug': campaign.slug, 'location_slug': location.slug}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/location_form.html', context)


@utils.login_required
@utils.is_gm
def location_edit(request, campaign_slug=None, location_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    location = get_object_or_404(Location, slug=location_slug)

    form = LocationEntryForm(request.POST or None, request.FILES or None, instance=location)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'location': location,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('campaign:location_detail', kwargs={'campaign_slug': campaign.slug, 'location_slug': location.slug}))

    return render(request, 'campaign/location_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def location_detail(request, campaign_slug=None, location_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    location = get_object_or_404(Location, slug=location_slug)

    context = {
        'campaign': campaign,
        'location': location
    }

    return render(request, 'campaign/location_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def log_list(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)

    logs = Log.objects.filter(
        campaign=campaign
    )

    context = {
        'campaign': campaign,
        'logs': logs,
    }

    return render(request, 'campaign/log_list.html', context)


@utils.login_required
@utils.is_gm
def new_log(request, campaign_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    log = Log(campaign_id = campaign.id)

    form = LogEntryForm(request.POST or None, request.FILES or None, instance=log)

    if form.is_valid():
        log = form.save(commit=False)
        log.campaign_id = campaign.id
        log.save()

        return HttpResponseRedirect(reverse('campaign:log_detail', kwargs={'campaign_slug': campaign.slug, 'log_slug': log.slug}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/log_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def log_detail(request, campaign_slug=None, log_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    log = get_object_or_404(Log, slug=log_slug)
    context = {
        'campaign': campaign,
        'log': log
    }

    return render(request, 'campaign/log_detail.html', context)


@utils.login_required
@utils.is_gm
def log_edit(request, campaign_slug=None, log_slug=None):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    log = get_object_or_404(Log, slug=log_slug)

    form = LogEntryForm(request.POST or None, request.FILES or None, instance=log)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'log': log,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('campaign:log_detail', kwargs={'campaign_slug': campaign.slug, 'log_slug': log.slug}))

    return render(request, 'campaign/log_form.html', context)

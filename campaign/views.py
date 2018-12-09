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

        # fixme(devenney): should redirect to campaign details.
        return HttpResponseRedirect(reverse('campaign:campaign_index'))

    context = {'form': form}

    return render(request, 'campaign/campaign_form.html', context)


@utils.login_required
@utils.is_gm
def campaign_edit(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    form = CampaignEntryForm(request.POST or None, request.FILES or None, instance=campaign)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/campaign/{}/'.format(campaign_id))

    return render(request, 'campaign/campaign_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def campaign_detail(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    characters = Character.objects.filter(
        campaign = campaign
    )

    context = {
        'campaign': campaign,
        'characters': characters
    }

    return render(request, 'campaign/campaign_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def character_list(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    characters = Character.objects.filter(
        campaign = campaign
    )

    context = {
        'campaign': campaign,
        'characters': characters,
    }

    return render(request, 'campaign/character_list.html', context)

@utils.login_required
@utils.is_gm
def new_character(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    character = Character(campaign_id = campaign_id)

    form = CharacterEntryForm(request.POST or None, instance=character)

    if form.is_valid():
        character = form.save(commit=False)
        character.campaign_id = campaign_id
        character.save()

        # fixme(devenney): should redirect to character details.
        return HttpResponseRedirect(reverse('campaign:character_list', kwargs={'campaign_id': campaign.id}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/character_form.html', context)

@utils.login_required
@utils.can_edit_character
def character_edit(request, campaign_id=None, character_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    character = get_object_or_404(Character, id=character_id)

    form = CharacterEntryForm(request.POST or None, request.FILES or None, instance=character)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'character': character,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/campaign/{}/characters/{}/'.format(campaign_id, character_id))

    return render(request, 'campaign/character_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def character_detail(request, campaign_id=None, character_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    character = get_object_or_404(Character, id=character_id)

    context = {
        'campaign': campaign,
        'character': character
    }

    return render(request, 'campaign/character_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def faction_list(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

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
def new_faction(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    faction = Faction(campaign_id = campaign_id)

    form = FactionEntryForm(request.POST or None, request.FILES or None, instance=faction)

    if form.is_valid():
        faction = form.save(commit=False)
        faction.campaign_id = campaign_id
        faction.save()

        # fixme(devenney): should redirect to faction details.
        return HttpResponseRedirect(reverse('campaign:faction_list', kwargs={'campaign_id': campaign.id}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/faction_form.html', context)

@utils.login_required
@utils.is_gm
def faction_edit(request, campaign_id=None, faction_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    faction = get_object_or_404(Faction, id=faction_id)

    form = FactionEntryForm(request.POST or None, request.FILES or None, instance=faction)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'faction': faction,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/campaign/{}/factions/{}/'.format(campaign_id, faction_id))

    return render(request, 'campaign/faction_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def faction_detail(request, campaign_id=None, faction_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    faction = get_object_or_404(Faction, id=faction_id)

    context = {
        'campaign': campaign,
        'faction': faction
    }

    return render(request, 'campaign/faction_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def item_list(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

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
def new_item(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    item = Item(campaign_id = campaign_id)

    form = ItemEntryForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        item = form.save(commit=False)
        item.campaign_id = campaign_id
        item.save()

        # fixme(devenney): should redirect to item details.
        return HttpResponseRedirect(reverse('campaign:item_list', kwargs={'campaign_id': campaign.id}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/item_form.html', context)


@utils.login_required
@utils.is_gm
def item_edit(request, campaign_id=None, item_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    item = get_object_or_404(Item, id=item_id)

    form = ItemEntryForm(request.POST or None, request.FILES or None, instance=item)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'item': item,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/campaign/{}/items/{}/'.format(campaign_id, item_id))

    return render(request, 'campaign/item_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def item_detail(request, campaign_id=None, item_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    item = get_object_or_404(Item, id=item_id)

    context = {
        'campaign': campaign,
        'item': item
    }

    return render(request, 'campaign/item_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def location_list(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

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
def new_location(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    location = Location(campaign_id = campaign_id)

    form = LocationEntryForm(request.POST or None, request.FILES or None, instance=location)

    if form.is_valid():
        location = form.save(commit=False)
        location.campaign_id = campaign_id
        location.save()

        # fixme(devenney): should redirect to location details.
        return HttpResponseRedirect(reverse('campaign:location_list', kwargs={'campaign_id': campaign.id}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/location_form.html', context)


@utils.login_required
@utils.is_gm
def location_edit(request, campaign_id=None, location_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    location = get_object_or_404(Location, id=location_id)

    form = LocationEntryForm(request.POST or None, request.FILES or None, instance=location)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'location': location,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/campaign/{}/locations/{}/'.format(campaign_id, location_id))

    return render(request, 'campaign/location_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def location_detail(request, campaign_id=None, location_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    location = get_object_or_404(Location, id=location_id)

    context = {
        'campaign': campaign,
        'location': location
    }

    return render(request, 'campaign/location_detail.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def log_list(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

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
def new_log(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    log = Log(campaign_id = campaign_id)

    form = LogEntryForm(request.POST or None, request.FILES or None, instance=log)

    if form.is_valid():
        log = form.save(commit=False)
        log.campaign_id = campaign_id
        log.save()

        # fixme(devenney): should redirect to log details.
        return HttpResponseRedirect(reverse('campaign:log_list', kwargs={'campaign_id': campaign.id}))

    context = {
        'campaign': campaign,
        'form': form
    }

    return render(request, 'campaign/log_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def log_detail(request, campaign_id=None, log_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    log = get_object_or_404(Log, id=log_id)

    context = {
        'campaign': campaign,
        'log': log
    }

    return render(request, 'campaign/log_detail.html', context)


@utils.login_required
@utils.is_gm
def log_edit(request, campaign_id=None, log_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    log = get_object_or_404(Log, id=log_id)

    form = LogEntryForm(request.POST or None, request.FILES or None, instance=log)

    context = {
        'form': form,
        'action': 'Edit',
        'campaign': campaign,
        'log': log,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/campaign/{}/log/{}/'.format(campaign_id, log_id))

    return render(request, 'campaign/log_form.html', context)

from dal import autocomplete
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CampaignEntryForm
from .models import Campaign
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


def newcampaign(request):
    form = CampaignEntryForm(request.POST or None)

    players = request.POST.getlist('players')

    if form.is_valid():
        campaign = form.save(commit=False)

        campaign.game_master_id = request.user.id
        campaign.save()
        campaign.players.set(players)
        campaign.save()

        # FIXME(devenney): Should redirect to campaign details.
        return HttpResponseRedirect(reverse('campaign:campaign_index'))

    context = {'form': form}

    return render(request, 'campaign/campaign_form.html', context)


@utils.login_required
@utils.is_gm
def campaign_edit(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    form = CampaignEntryForm(request.POST or None, instance=campaign)

    context = {
        'form': form,
        'action': 'Edit'
    }

    if form.is_valid():
        form.save()
        # FIXME(devenney): Should redirect to campaign details.
        return HttpResponseRedirect('/campaign/{}/'.format(campaign_id))

    return render(request, 'campaign/campaign_form.html', context)


@utils.login_required_if_private
@utils.is_player_if_private
def campaign_detail(request, campaign_id=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    context = {
        'campaign': campaign
    }

    return render(request, 'campaign/campaign_detail.html', context)

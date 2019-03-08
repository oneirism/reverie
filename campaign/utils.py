from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Campaign, Character


def login_required_if_private(func):
    def wrap(request, *args, **kwargs):
        campaign = Campaign.objects.get(slug=kwargs['campaign_slug'])

        if campaign.public:
            return func(request, *args, **kwargs)

        return login_required(func)(request, *args, **kwargs)

    return wrap

def is_gm(func):
    def check_and_call(request, *args, **kwargs):
        campaign = Campaign.objects.get(slug=kwargs['campaign_slug'])

        if not (request.user.id == campaign.game_master_id):
            return HttpResponse("Unauthorised", status=403)

        return func(request, *args, **kwargs)

    return check_and_call

def can_edit_character(func):
    def wrap(request, *args, **kwargs):
        campaign = Campaign.objects.get(slug=kwargs['campaign_slug'])
        character = Character.objects.get(slug=kwargs['character_slug'])

        if not (request.user == character.player or request.user == campaign.game_master):
            return HttpResponse("Unauthorised", status=403)

        return func(request, *args, **kwargs)

    return wrap

def is_player_if_private(func):
    def wrap(request, *args, **kwargs):
        campaign = Campaign.objects.get(slug=kwargs['campaign_slug'])

        if campaign.public:
            return func(request, *args, **kwargs)

        if not (request.user.id == campaign.game_master_id) and not (request.user in campaign.players.all()):
            return HttpResponse("Unauthorised", status=403)

        return func(request, *args, **kwargs)

    return wrap

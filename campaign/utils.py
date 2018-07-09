from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Campaign


def login_required_if_private(func):
    def wrap(request, *args, **kwargs):
        campaign = Campaign.objects.get(id=kwargs['campaign_id'])

        if campaign.public:
            return func(request, *args, **kwargs)

        return login_required(func)(request, *args, **kwargs)

    return wrap

def is_gm(func):
    def check_and_call(request, *args, **kwargs):
        campaign = Campaign.objects.get(id=kwargs['campaign_id'])

        if not (request.user.id == campaign.game_master_id):
            return HttpResponse("Unauthorised", status=403)

        return func(request, *args, **kwargs)

    return check_and_call

def is_player(func):
    def wrap(request, *args, **kwargs):
        campaign = Campaign.objects.get(id=kwargs['campaign_id'])

        if not (request.user.id == campaign.game_master_id) and not (request.user in campaign.players.all()):
            return HttpResponse("Unauthorised", status=403)

        return func(request, *args, **kwargs)

    return wrap

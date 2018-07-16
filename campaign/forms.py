from dal import autocomplete
from django import forms
from django.contrib.auth.models import User

from .models import Campaign

class CampaignEntryForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='campaign:player_autocomplete', forward=['game_master'])
    )

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'players', 'public']

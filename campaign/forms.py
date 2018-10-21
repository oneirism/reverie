from dal import autocomplete
from django import forms
from django.contrib.auth.models import User

from .models import Campaign, Character, Faction, Item, Location

class CampaignEntryForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='campaign:player_autocomplete', forward=['game_master']),
        required=False
    )

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'players', 'public', 'tagline']


class CharacterEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharacterEntryForm, self).__init__(*args, **kwargs)

        self.fields['player'] = forms.ModelChoiceField(
            queryset=self.instance.campaign.players,
            required=False,
            widget=forms.Select(),
            empty_label="----",
        )

    class Meta:
        model = Character
        fields = ['name', 'tagline', 'description', 'player']


class FactionEntryForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = ['name', 'tagline', 'description']


class ItemEntryForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'tagline', 'description']


class LocationEntryForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'tagline', 'description']

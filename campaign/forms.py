import datetime

from dal import autocomplete
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from .models import Campaign, Character, Faction, Item, Location, Log


class BulmaDateInput(widgets.DateInput):
    """ A custom DateInput to set 'type' correctly. """
    input_type = 'date'


class CampaignEntryForm(forms.ModelForm):
    """ A reverie Campaign form. """
    players = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='campaign:player_autocomplete', forward=['game_master']),
        required=False
    )

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'players', 'public', 'tagline']


class CharacterEntryForm(forms.ModelForm):
    """ A Reverie character form. """
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
    """ A Reverie faction form. """
    class Meta:
        model = Faction
        fields = ['name', 'tagline', 'description']


class ItemEntryForm(forms.ModelForm):
    """ A Reverie item form. """
    class Meta:
        model = Item
        fields = ['name', 'tagline', 'description']


class LocationEntryForm(forms.ModelForm):
    """ A reverie location form. """
    class Meta:
        model = Location
        fields = ['name', 'tagline', 'description']


class LogEntryForm(forms.ModelForm):
    """ A Reverie log form. """
    class Meta:
        model = Log
        fields = ['title', 'date', 'description']

    this_year = datetime.date.today().year
    years = range(this_year-5, this_year+5)

    date = forms.DateField(widget=BulmaDateInput(
        attrs={
            'autocomplete': 'off',
        }
    ))

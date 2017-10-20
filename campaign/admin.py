from django import forms
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from .models import Campaign, Character, Faction, Location, LogEntry


class CampaignForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignAdmin(admin.ModelAdmin):
    model = Campaign
    form = CampaignForm

    list_display = ['name', 'tagline']
    list_display_links = ['name']
    search_fields = ['name']


class CharacterForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Character
        fields = '__all__'


class CharacterAdmin(admin.ModelAdmin):
    model = Character
    form = CharacterForm

    list_display = ['name', 'status', 'tagline', 'location', 'faction']
    list_display_links = ['name']
    list_filter = ['faction', 'location', 'status']
    search_fields = ['name']


class FactionForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Faction
        fields = '__all__'


class FactionAdmin(admin.ModelAdmin):
    model = Faction
    form = FactionForm

    list_display = ['name', 'tagline']
    list_display_links = ['name']
    search_fields = ['name']


class LocationForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    model = Location
    form = LocationForm

    list_display = ['name', 'tagline']
    list_display_links = ['name']
    search_fields = ['name']


class LogEntryForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = LogEntry
        fields = '__all__'


class LogEntryAdmin(admin.ModelAdmin):
    model = LogEntry
    form = LogEntryForm

    list_display = ['title', 'date']
    search_fields = ['title']


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(LogEntry, LogEntryAdmin)

""" Reverie campaign admin interface.

The expected ordering of this file is as follows:

    1. Definition of all required ModelAdmin classes.
    2. Registration of the above classes to the admin site.
"""

from django.contrib import admin

from .models import Campaign, Character, Faction, Item, Location


class CampaignAdmin(admin.ModelAdmin):
    """ ModelAdmin for the Campaign class. """
    model = Campaign

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class CharacterAdmin(admin.ModelAdmin):
    """ ModelAdmin for the Character class. """
    model = Character

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class FactionAdmin(admin.ModelAdmin):
    """ ModelAdmin for the Faction class. """
    model = Faction

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class ItemAdmin(admin.ModelAdmin):
    """ ModelAdmin for the Item class. """
    model = Item

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class LocationAdmin(admin.ModelAdmin):
    """ ModelAdmin for the Location class. """
    model = Location

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)

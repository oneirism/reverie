""" Reverie campaign admin interface.

The expected ordering of this file is as follows:

    1. Definition of all required ModelAdmin classes.
    2. Registration of the above classes to the admin site.
"""

from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Campaign, Character, Faction, Item, Location


class CampaignAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """ ModelAdmin for the Campaign class. """
    model = Campaign

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class CharacterAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """ ModelAdmin for the Character class. """
    model = Character

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class FactionAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """ ModelAdmin for the Faction class. """
    model = Faction

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class ItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """ ModelAdmin for the Item class. """
    model = Item

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class LocationAdmin(ImageCroppingMixin, admin.ModelAdmin):
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

from django.contrib import admin

from .models import Campaign, Character, Faction, Item, Location 


class CampaignAdmin(admin.ModelAdmin):
    model = Campaign

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class CharacterAdmin(admin.ModelAdmin):
    model = Character

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class FactionAdmin(admin.ModelAdmin):
    model = Faction

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class ItemAdmin(admin.ModelAdmin):
    model = Item

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class LocationAdmin(admin.ModelAdmin):
    model = Location

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)

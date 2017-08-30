from django.contrib import admin

from .models import Campaign, Character, Faction, Location


admin.site.register(Campaign)
admin.site.register(Character)
admin.site.register(Faction)
admin.site.register(Location)

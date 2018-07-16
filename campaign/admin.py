from django.contrib import admin

from .models import Campaign


class CampaignAdmin(admin.ModelAdmin):
    model = Campaign

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

admin.site.register(Campaign, CampaignAdmin)

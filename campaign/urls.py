from django.urls import path

from .views import index, new_campaign, campaign_detail, campaign_edit, \
    new_character, character_list, character_detail, character_edit, \
    new_faction, faction_list, faction_detail, faction_edit, \
    new_item, item_list, item_detail, item_edit, \
    new_location, location_list, location_detail, location_edit, \
    new_log, log_list, log_detail, log_edit, \
    PlayerAutocomplete

urlpatterns = [
    path('player-autocomplete/', PlayerAutocomplete.as_view(), name='player_autocomplete'),

    path('', index, name='campaign_index'),
    path('new/', new_campaign, name='campaign_entry'),
    path('<campaign_slug>/', campaign_detail, name='campaign_detail'),
    path('<campaign_slug>/edit/', campaign_edit, name='campaign_edit'),

    path('<campaign_slug>/characters/', character_list, name='character_list'),
    path('<campaign_slug>/characters/new', new_character, name='character_entry'),
    path('<campaign_slug>/characters/<character_slug>/', character_detail, name='character_detail'),
    path('<campaign_slug>/characters/<character_slug>/edit/', character_edit, name='character_edit'),

    path('<campaign_slug>/factions/', faction_list, name='faction_list'),
    path('<campaign_slug>/factions/new', new_faction, name='faction_entry'),
    path('<campaign_slug>/factions/<faction_slug>/', faction_detail, name='faction_detail'),
    path('<campaign_slug>/factions/<faction_slug>/edit/', faction_edit, name='faction_edit'),

    path('<campaign_slug>/items/', item_list, name='item_list'),
    path('<campaign_slug>/items/new', new_item, name='item_entry'),
    path('<campaign_slug>/items/<item_slug>/', item_detail, name='item_detail'),
    path('<campaign_slug>/items/<item_slug>/edit/', item_edit, name='item_edit'),

    path('<campaign_slug>/locations/', location_list, name='location_list'),
    path('<campaign_slug>/locations/new', new_location, name='location_entry'),
    path('<campaign_slug>/locations/<location_slug>/', location_detail, name='location_detail'),
    path('<campaign_slug>/locations/<location_slug>/edit/', location_edit, name='location_edit'),

    path('<campaign_slug>/log/', log_list, name='log_list'),
    path('<campaign_slug>/log/new/', new_log, name='log_entry'),
    path('<campaign_slug>/log/<log_slug>/', log_detail, name='log_detail'),
    path('<campaign_slug>/log/<log_slug>/edit/', log_edit, name='log_edit'),
]

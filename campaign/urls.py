from django.urls import path

from .views import index, new_campaign, campaign_detail, campaign_edit, \
    new_character, character_list, character_detail, character_edit, \
    new_faction, faction_list, faction_detail, faction_edit, \
    new_item, item_list, item_detail, item_edit, \
    new_location, location_list, location_detail, location_edit, \
    PlayerAutocomplete

urlpatterns = [
    path('player-autocomplete/', PlayerAutocomplete.as_view(), name='player_autocomplete'),

    path('', index, name='campaign_index'),
    path('new/', new_campaign, name='campaign_entry'),
    path('<campaign_id>/', campaign_detail, name='campaign_detail'),
    path('<campaign_id>/edit/', campaign_edit, name='campaign_edit'),

    path('<campaign_id>/characters/', character_list, name='character_list'),
    path('<campaign_id>/characters/new', new_character, name='character_entry'),
    path('<campaign_id>/characters/<character_id>/', character_detail, name='character_detail'),
    path('<campaign_id>/characters/<character_id>/edit/', character_edit, name='character_edit'),

    path('<campaign_id>/factions/', faction_list, name='faction_list'),
    path('<campaign_id>/factions/new', new_faction, name='faction_entry'),
    path('<campaign_id>/factions/<faction_id>/', faction_detail, name='faction_detail'),
    path('<campaign_id>/factions/<faction_id>/edit/', faction_edit, name='faction_edit'),

    path('<campaign_id>/items/', item_list, name='item_list'),
    path('<campaign_id>/items/new', new_item, name='item_entry'),
    path('<campaign_id>/items/<item_id>/', item_detail, name='item_detail'),
    path('<campaign_id>/items/<item_id>/edit/', item_edit, name='item_edit'),

    path('<campaign_id>/locations/', location_list, name='location_list'),
    path('<campaign_id>/locations/new', new_location, name='location_entry'),
    path('<campaign_id>/locations/<location_id>/', location_detail, name='location_detail'),
    path('<campaign_id>/locations/<location_id>/edit/', location_edit, name='location_edit'),
]

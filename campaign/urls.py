from django.urls import path

from .views import index, new_campaign, campaign_detail, campaign_edit, PlayerAutocomplete

urlpatterns = [
    path('player-autocomplete/', PlayerAutocomplete.as_view(), name='player_autocomplete'),

    path('', index, name='campaign_index'),
    path('new/', new_campaign, name='campaign_entry'),
    path('<campaign_id>/', campaign_detail, name='campaign_detail'),
    path('<campaign_id>/edit/', campaign_edit, name='campaign_edit'),
]

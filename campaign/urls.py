from django.conf.urls import url

from . import views


urlpatterns = [
        # example: /
        url(r'^$', views.campaign_list, name='campaign_list'),
        # example: /campaign/5/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/$', views.campaign_detail, name='campaign_detail'),
        # example: /characters/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/characters/$', views.character_list, name='character_list'),
        # example: /characters/5/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/characters/(?P<char_slug>[\w-]+)$', views.character_detail, name='character_detail'),
        # example: /factions/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/factions/$', views.faction_list, name='faction_list'),
        # example: /factions/5/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/factions/(?P<fact_slug>[\w-]+)$', views.faction_detail, name='faction_detail'),
        # example: /locations/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/locations/$', views.location_list, name='location_list'),
        # example: /locations/5/
        url(r'^campaign/(?P<camp_slug>[\w-]+)/locations/(?P<loc_slug>[\w-]+)$', views.location_detail, name='location_detail'),
]

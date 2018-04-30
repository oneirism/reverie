import django_tables2 as tables
from django_tables2 import A

from .models import Character


class CharacterTable(tables.Table):
    class Meta:
        model = Character
        attrs = {
            'class': 'table is-bordered is-fullwidth is-striped',
        }
        exclude = {'campaign', 'description', 'id', 'image', 'is_pc', 'picture', 'slug', 'tagline'}

    faction = tables.LinkColumn("campaign:faction_detail", args=[A('campaign.slug'), A('faction.slug')], order_by='faction.name')
    location = tables.LinkColumn("campaign:location_detail", args=[A('campaign.slug'), A('location.slug')], order_by='location.name')
    name = tables.LinkColumn("campaign:character_detail", args=[A('campaign.slug'), A('slug')])

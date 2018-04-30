from django.urls import reverse
from django.template import Context, Template
from django.test import TestCase

from campaign.tests.utils import *


class CrossReferencesTest(TestCase):
    def test_standalone_references(self):
        campaign_name = "Test Campaign"
        campaign = create_campaign(campaign_name)

        faction_name = "Test Faction"
        faction = create_faction(campaign, faction_name)

        test_markdown = "{{{{campaign:{0}}}}} {{{{faction:{1}}}}}".format(
            campaign.slug, faction.slug
        )

        test_template = Template(
                "{% load markdown_extras %}"
                "{{description | cross_reference}}"
        )
        rendered = test_template.render(Context({
                'description': test_markdown
        }))

        campaign_url = reverse('campaign:campaign_detail', args=[campaign.slug])
        faction_url = reverse('campaign:faction_detail', args=[campaign.slug, faction.slug])

        self.assertEqual(rendered, "[{0}]({1}) [{2}]({3})".format(
            campaign_name, campaign_url, faction_name, faction_url
        ))

    def test_markdown_reference(self):
        campaign_name = "Test Campaign"
        campaign = create_campaign(campaign_name)

        test_markdown = "[Campaign]({{campaign:test-campaign}})"

        test_template = Template(
                "{% load markdown_extras %}"
                "{{description | cross_reference}}"
        )
        rendered = test_template.render(Context({
                'description': test_markdown
        }))

        campaign_url = reverse('campaign:campaign_detail', args=[campaign.slug])
        self.assertEqual(rendered, "[Campaign]({0})".format(campaign_url))

    def test_bad_reference(self):
        test_markdown = "[Campaign]({{campaign:test-campaign}})"

        test_template = Template(
                "{% load markdown_extras %}"
                "{{description | cross_reference}}"
        )
        rendered = test_template.render(Context({
                'description': test_markdown
        }))

        self.assertEqual(rendered, test_markdown)


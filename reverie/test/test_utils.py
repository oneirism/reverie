from campaign.models import Campaign, Character
from reverie.utils import markdownify

from django.test import TestCase

class UtilsTest(TestCase):
    def setUp(self):
        campaign = {
            'game_master_id': 1,
            'name': 'Test Campaign',
            'description': 'Test Description',
            'public': True
        }

        self.campaign = Campaign.objects.create(**campaign)

        character = {
            'name': 'Test Character',
            'description': 'Test Description',
            'campaign_id': self.campaign.id,
        }

        self.character = Character.objects.create(**character)

    def test_standalone_markdown(self):
        content = "{{character:test-character}}"

        md = markdownify(content)

        self.assertTrue("Test Character" in md)

    def test_standalone_markdown_campaign(self):
        content = "{{campaign:test-campaign}}"

        md = markdownify(content)

        self.assertTrue("Test Campaign" in md)

    def test_standalone_markdown_bad(self):
        content = "{{character:not-a-character}}"

        md = markdownify(content)

        self.assertEqual(md, content)

    def test_linked_markdown(self):
        content = "[Testing Character]({{character:test-character}})"

        md = markdownify(content)

        self.assertTrue("/test-character/" in md)

    def test_standalone_markdown_bad(self):
        content = "[Not a character]({{character:not-a-character}})"

        md = markdownify(content)

        self.assertTrue("{{character:not-a-character}}" in md)

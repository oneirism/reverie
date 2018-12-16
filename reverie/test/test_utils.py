from reverie.utils import markdownify

from django.test import TestCase

class UtilsTest(TestCase):
    def test_markdownify(self):
        test_content = "# Test"

        md = markdownify(test_content)

        self.assertEqual(md, "<h1>Test</h1>\n")

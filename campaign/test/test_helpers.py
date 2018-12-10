from django.test import TestCase

from campaign.helpers import RandomFileName

class RandomFileNameTest(TestCase):
    def test_init(self):
        filename = RandomFileName('/static/test')
        filename2 = RandomFileName('/static/test')

        self.assertNotEqual(filename, filename2)

    def test_call(self):
        filename = RandomFileName('/static/test')

        call = filename('test', 'test.jpg')
        call2 = filename('test', 'test.jpg')
        self.assertNotEqual(call, call2)


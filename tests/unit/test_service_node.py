import unittest

from kong.client import Client


class TestStatusService(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.client = Client("http://www.test.com", username="foo", password="bar")

    def test_status(self):
        assert self.client



import unittest

from ..utils import get_integration_testing_client


class TestStatusService(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.client = get_integration_testing_client()

    def test_status(self):
        response = self.client.status.get()
        assert response.get('database')
        assert response.get('server')



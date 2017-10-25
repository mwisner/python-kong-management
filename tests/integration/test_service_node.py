import unittest

from ..utils import get_integration_testing_client


class TestNodeService(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.client = get_integration_testing_client()

    def test_information(self):
        response = self.client.node.information()
        assert response.get('hostname')
        assert response.get('lua_version')

    def test_status(self):
        response = self.client.node.status()
        assert response.get('database')
        assert response.get('server')

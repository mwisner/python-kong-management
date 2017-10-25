import unittest

from ..utils import get_integration_testing_client
from uuid import uuid4

class TestConsumerService(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.client = get_integration_testing_client()

    def test_create_with_username(self):
        client = self.client
        payload = {
            'username': str(uuid4())
        }

        response = client.consumers.create(payload)
        assert response.get('username') == payload['username']

    def test_create_with_custom_id(self):
        client = self.client
        payload = {
            'custom_id': str(uuid4())
        }

        response = client.consumers.create(payload)
        assert response.get('custom_id') == payload['custom_id']

    def test_lifecycle(self):
        """
        Smoke test the entire lifecycle of a consumer
        :return:
        """
        client = self.client

        #
        # Create
        create_payload = {
            'username': str(uuid4())
        }

        response = client.consumers.create(create_payload)
        assert response.get('username') == create_payload['username']

        #
        # Update
        update_payload = {
            'custom_id': str(uuid4())
        }
        response = client.consumers.update(create_payload['username'], update_payload)
        assert response.get('custom_id') == update_payload['custom_id']

        #
        # Delete
        response = client.consumers.delete(create_payload['username'])
        assert response is None

    def test_add_key(self):
        client = self.client
        payload = {
            'username': str(uuid4())
        }

        response = client.consumers.create(payload)
        assert response.get('username') == payload['username']

        response = client.consumers.add_key(payload['username'])
        assert response.get('key')

        key = str(uuid4())
        response = client.consumers.add_key(payload['username'], key)
        assert key == response.get('key')

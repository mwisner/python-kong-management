from .base_service import BaseService
from kong.errors import KongError


class Consumers(BaseService):

    def create(self, data):
        """

        :return:
        """
        response = self.client.post('consumers/', data)
        return response

    def update_or_create(self, data):
        """

        :return:
        """
        response = self.client.put('consumers/', data)
        return response

    def retrieve(self, username_or_id):
        """

        :return:
        """
        response = self.client.get('consumers/%s' % username_or_id)
        return response

    def list(self, id=None, custom_id=None, username=None, size=None, offset=None):
        """

        :return:
        """

        filters = {}

        if id:
            filters['id'] = id

        if custom_id:
            filters['custom_id'] = custom_id

        if username:
            filters['username'] = username

        if size:
            filters['size'] = size

        if offset:
            filters['offset'] = offset

        response = self.client.get('consumers', filters)
        return response

    def update(self, username_or_id, data):
        """

        :return:
        """
        response = self.client.patch('consumers/%s' % username_or_id, data)
        return response

    def delete(self, username_or_id):
        """

        :return:
        """
        response = self.client.delete('consumers/%s' % username_or_id)
        return response

    def add_key(self, username_or_id, key=None):
        payload = {}

        if key:
            payload['key'] = key

        response = self.client.post('consumers/%s/key-auth' % username_or_id, payload)
        return response

    def remove_key(self, username_or_id, key_id):
        response = self.client.delete('consumers/%s/key-auth/%s' % (username_or_id, key_id))
        return response






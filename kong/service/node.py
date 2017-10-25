from .base_service import BaseService
from kong.errors import KongError


class Node(BaseService):

    def information(self):
        """

        :return:
        """
        response = self.client.get('/')
        return response

    def status(self):
        """

        :return:
        """
        response = self.client.get('status/')
        return response

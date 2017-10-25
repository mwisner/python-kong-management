from .base_service import BaseService
from kong.errors import KongError


class Status(BaseService):
    def get(self):
        """

        :return:
        """
        response = self.client.get('status/')
        return response

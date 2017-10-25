import os
from kong.client import Client
from kong.errors import KongError


def get_integration_testing_client():
    """
    Load the client using
    :return:
    """
    management_domain = os.environ.get('KONG_MANAGEMENT')
    username = os.environ.get('KONG_USERNAME')
    password = os.environ.get('KONG_PASSWORD')

    return Client(management_domain, username=username, password=password)

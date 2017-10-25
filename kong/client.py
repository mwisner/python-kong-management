import requests
from .errors import KongError


class Client(object):

    def __init__(self, base_url, username=None, password=None):

        if base_url[-1:] != '/':
            base_url = base_url + '/'

        self.base_url = base_url
        self.username = username
        self.password = password

        self.rate_limit_details = {}
        self.http_session = requests.Session()

    @property
    def _auth(self):
        if self.username and self.password:
            return self.username, self.password
        return None

    @property
    def node(self):
        from .service import node
        return node.Node(self)

    @property
    def consumers(self):
        from .service import consumers
        return consumers.Consumers(self)

    def _execute_request(self, request, params):
        result = request.execute(self.base_url, self._auth, params)
        return result

    def get(self, path, params={}):
        from . import request
        req = request.Request('GET', path, self.http_session)
        return self._execute_request(req, params)

    def post(self, path, params):
        from . import request
        req = request.Request('POST', path, self.http_session)
        return self._execute_request(req, params)

    def put(self, path, params):
        from . import request
        req = request.Request('PUT', path, self.http_session)
        return self._execute_request(req, params)

    def patch(self, path, params):
        from . import request
        req = request.Request('PATCH', path, self.http_session)
        return self._execute_request(req, params)

    def delete(self, path, params = {}):
        from . import request
        req = request.Request('DELETE', path, self.http_session)
        return self._execute_request(req, params)

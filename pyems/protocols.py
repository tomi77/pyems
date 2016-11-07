from base64 import b64encode
import json
import socket

try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection

from .utils import EvoStreamException


SCHEMES = {
    'http': 'pyems.protocols.HTTPProtocol',
    'telnet': 'pyems.protocols.TelnetProtocol',
}


class BaseProtocol(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def get_result(self, command, **params):
        raise NotImplementedError()

    @staticmethod
    def parse_result(result):
        result = json.loads(result)
        if result['status'] == 'FAIL':
            raise EvoStreamException(result['description'])
        else:
            return result['data']

    @staticmethod
    def stringify_params(**params):
        return ' '.join(['%s=%s' % (key, val) for key, val in params.items()])

    def execute(self, command, **params):
        result = self.get_result(command, **params)

        return self.parse_result(result)


class HTTPProtocol(BaseProtocol):
    def make_uri(self, command, **params):
        uri = '/%s' % command
        if len(params) > 0:
            str_params = self.stringify_params(**params).encode('ascii')
            uri += '?params=%s' % b64encode(str_params).decode()
        return uri

    def get_result(self, command, **params):
        conn = HTTPConnection("%s:%d" % (self.hostname, self.port))
        uri = self.make_uri(command, **params)
        try:
            conn.request('GET', uri)
        except socket.error as ex:
            raise EvoStreamException(ex)
        response = conn.getresponse()
        return response.read()


class TelnetProtocol(BaseProtocol):
    def get_result(self, command, **params):
        raise NotImplementedError('Telnet protocol is not implemented')

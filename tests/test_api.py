import json
import os
import re
import unittest

import pyems

try:
    from unittest import mock
except ImportError:
    import mock


class Response:
    def __init__(self, filename):
        fh = open(os.path.join(os.path.dirname(__file__), 'testdata', filename))
        self.data = ''.join(fh.readlines())
        fh.close()

    def read(self):
        return self.data


class EmsTestCase(unittest.TestCase):
    api = pyems.Api('http://127.0.0.1:8000')
    data = None
    response = None

    def setUp(self):
        filename = '%s.json' % re.sub('([A-Z])', '_\\1', self.__class__.__name__[:-8]).lower()[1:]
        response = Response(filename)
        self.data = json.loads(response.read())
        self.response = mock.MagicMock(return_value=response)


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class PullStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.pull_stream(uri='rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4',
                                       localStreamName='testpullstream')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class PushStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.push_stream(uri='rtmp://DestinationAddress/live',
                                       localStreamName='testpullstream', targetStreamName='testpushStream')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListStreamsIdsTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_streams_ids()
            self.assertListEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class GetStreamInfoTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.get_stream_info(id=1)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListStreamsTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_streams()
            self.assertListEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class GetStreamsCountTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.get_streams_count()
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ShutdownStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.shutdown_stream(id=55)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListConfigTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_config()
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class RemoveConfigTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.remove_config(id=555)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class GetConfigInfoTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.get_config_info(1)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class AddStreamAliasTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.add_stream_alias('MyStream', 'video1', expirePeriod=-300)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListStreamAliasesTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_stream_aliases()
            self.assertListEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class RemoveStreamAliasTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.remove_stream_alias(aliasName='video1')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class FlushStreamAliasesTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.flush_stream_aliases()
            self.assertIsNone(out)


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class AddGroupNameAliasTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.add_group_name_alias(groupName='MyGroup', aliasName='TestGroupAlias')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class FlushGroupNameAliasesTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.flush_group_name_aliases()
            self.assertIsNone(out)


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class GetGroupNameByAliasTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.get_group_name_by_alias(aliasName='TestGroupAlias')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListGroupNameAliasesTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_group_name_aliases()
            self.assertListEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class RemoveGroupNameAliasTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.remove_group_name_alias(aliasName='TestGroupAlias')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListHttpStreamingSessionsTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_http_streaming_sessions()
            self.assertListEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class CreateIngestPointTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.create_ingest_point(privateStreamName='theIngestPoint', publicStreamName='useMeToViewStream')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class RemoveIngestPointTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.remove_ingest_point(privateStreamName='theIngestPoint')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class ListIngestPointsTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.list_ingest_points()
            self.assertListEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class CreateHlsStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.create_hls_stream('hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                                             playlistType='rolling', playlistLength=10, chunkLength=5)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class CreateHdsStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.create_hds_stream('testpullStream', '../evo-webroot', groupName='hds', playlistType='rolling')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class IsStreamRunningTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.is_stream_running(id=1)
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class CreateMssStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.create_mss_stream('testpullStream', '../evo-webroot', groupName='mss')
            self.assertDictEqual(out, self.data['data'])


@mock.patch('pyems.protocols.HTTPConnection.request', mock.Mock())
class CreateDashStreamTestCase(EmsTestCase):
    def test_api(self):
        with mock.patch('pyems.protocols.HTTPConnection.getresponse', self.response):
            out = self.api.create_dash_stream('testpullStream', '../evo-webroot', groupName='dash')
            self.assertDictEqual(out, self.data['data'])

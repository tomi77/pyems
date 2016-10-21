import json
import os
from unittest import TestCase

from pyems import Api
from pyems.protocols import HTTPProtocol


class TestHTTPProtocol(HTTPProtocol):
    def __init__(self, data):
        self.result = json.dumps(data)

    def get_result(self, command, **params):
        return self.result


def load_test_data(filename):
    fh = open(os.path.join(os.path.dirname(__file__), 'testdata', filename))
    data = json.load(fh)
    fh.close()
    return data


class EmsTestCase(TestCase):
    file_data = None
    data = None

    def setUp(self):
        self.data = load_test_data(self.file_data)
        self.api = Api('http://127.0.0.1:8000')
        self.api.protocol = TestHTTPProtocol(self.data)


class PullStreamTestCase(EmsTestCase):
    file_data = 'pull_stream.json'

    def test_api(self):
        out = self.api.pull_stream(uri='rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4',
                                   localStreamName='testpullstream')
        self.assertDictEqual(out, self.data['data'])


class PushStreamTestCase(EmsTestCase):
    file_data = 'push_stream.json'

    def test_api(self):
        out = self.api.push_stream(uri='rtmp://DestinationAddress/live',
                                   localStreamName='testpullstream', targetStreamName='testpushStream')
        self.assertDictEqual(out, self.data['data'])


class ListStreamsIdsTestCase(EmsTestCase):
    file_data = 'list_streams_ids.json'

    def test_api(self):
        out = self.api.list_streams_ids()
        self.assertListEqual(out, self.data['data'])


class GetStreamInfoTestCase(EmsTestCase):
    file_data = 'get_stream_info.json'

    def test_api(self):
        out = self.api.get_stream_info(id=1)
        self.assertDictEqual(out, self.data['data'])


class ListStreamsTestCase(EmsTestCase):
    file_data = 'list_streams.json'

    def test_api(self):
        out = self.api.list_streams()
        self.assertListEqual(out, self.data['data'])


class GetStreamsCountTestCase(EmsTestCase):
    file_data = 'get_streams_count.json'

    def test_api(self):
        out = self.api.get_streams_count()
        self.assertDictEqual(out, self.data['data'])


class ShutdownStreamTestCase(EmsTestCase):
    file_data = 'shutdown_stream.json'

    def test_api(self):
        out = self.api.shutdown_stream(id=55)
        self.assertDictEqual(out, self.data['data'])


class ListConfigTestCase(EmsTestCase):
    file_data = 'list_config.json'

    def test_api(self):
        out = self.api.list_config()
        self.assertDictEqual(out, self.data['data'])


class RemoveConfigTestCase(EmsTestCase):
    file_data = 'remove_config.json'

    def test_api(self):
        out = self.api.remove_config(id=555)
        self.assertDictEqual(out, self.data['data'])


class GetConfigInfoTestCase(EmsTestCase):
    file_data = 'get_config_info.json'

    def test_api(self):
        out = self.api.get_config_info(1)
        self.assertDictEqual(out, self.data['data'])


class AddStreamAliasTestCase(EmsTestCase):
    file_data = 'add_stream_alias.json'

    def test_api(self):
        out = self.api.add_stream_alias('MyStream', 'video1', expirePeriod=-300)
        self.assertDictEqual(out, self.data['data'])


class ListStreamAliasesTestCase(EmsTestCase):
    file_data = 'list_stream_aliases.json'

    def test_api(self):
        out = self.api.list_stream_aliases()
        self.assertListEqual(out, self.data['data'])


class RemoveStreamAliasTestCase(EmsTestCase):
    file_data = 'remove_stream_alias.json'

    def test_api(self):
        out = self.api.remove_stream_alias(aliasName='video1')
        self.assertDictEqual(out, self.data['data'])


class FlushStreamAliasesTestCase(EmsTestCase):
    file_data = 'flush_stream_aliases.json'

    def test_api(self):
        out = self.api.flush_stream_aliases()
        self.assertIsNone(out)


class AddGroupNameAliasTestCase(EmsTestCase):
    file_data = 'add_group_name_alias.json'

    def test_api(self):
        out = self.api.add_group_name_alias(groupName='MyGroup', aliasName='TestGroupAlias')
        self.assertDictEqual(out, self.data['data'])


class FlushGroupNameAliasesTestCase(EmsTestCase):
    file_data = 'flush_group_name_aliases.json'

    def test_api(self):
        out = self.api.flush_stream_aliases()
        self.assertIsNone(out)


class GetGroupNameByAliasTestCase(EmsTestCase):
    file_data = 'get_group_name_by_alias.json'

    def test_api(self):
        out = self.api.get_group_name_by_alias(aliasName='TestGroupAlias')
        self.assertDictEqual(out, self.data['data'])


class ListGroupNameAliasesTestCase(EmsTestCase):
    file_data = 'list_group_name_aliases.json'

    def test_api(self):
        out = self.api.list_group_name_aliases()
        self.assertListEqual(out, self.data['data'])


class RemoveGroupNameAliasTestCase(EmsTestCase):
    file_data = 'remove_group_name_alias.json'

    def test_api(self):
        out = self.api.remove_group_name_alias(aliasName='TestGroupAlias')
        self.assertDictEqual(out, self.data['data'])


class ListHttpStreamingSessionsTestCase(EmsTestCase):
    file_data = 'list_http_streaming_sessions.json'

    def test_api(self):
        out = self.api.list_http_streaming_sessions()
        self.assertListEqual(out, self.data['data'])


class CreateIngestPointTestCase(EmsTestCase):
    file_data = 'create_ingest_point.json'

    def test_api(self):
        out = self.api.create_ingest_point(privateStreamName='theIngestPoint', publicStreamName='useMeToViewStream')
        self.assertDictEqual(out, self.data['data'])


class RemoveIngestPointTestCase(EmsTestCase):
    file_data = 'remove_ingest_point.json'

    def test_api(self):
        out = self.api.remove_ingest_point(privateStreamName='theIngestPoint')
        self.assertDictEqual(out, self.data['data'])


class ListIngestPointsTestCase(EmsTestCase):
    file_data = 'list_ingest_points.json'

    def test_api(self):
        out = self.api.list_ingest_points()
        self.assertListEqual(out, self.data['data'])


class CreateHLSStreamTestCase(EmsTestCase):
    file_data = 'create_hls_stream.json'

    def test_api(self):
        out = self.api.create_hls_stream('hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                                         playlistType='rolling', playlistLength=10, chunkLength=5)
        self.assertDictEqual(out, self.data['data'])


class CreateHDSStreamTestCase(EmsTestCase):
    file_data = 'create_hds_stream.json'

    def test_api(self):
        out = self.api.create_hds_stream('testpullStream', '../evo-webroot', groupName='hds', playlistType='rolling')
        self.assertDictEqual(out, self.data['data'])


class IsStreamRunningTestCase(EmsTestCase):
    file_data = 'is_stream_running.json'

    def test_api(self):
        out = self.api.is_stream_running(id=1)
        self.assertDictEqual(out, self.data['data'])

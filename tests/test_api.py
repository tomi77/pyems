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
    return json.load(open(os.path.join(os.path.dirname(__file__), 'testdata', filename)))


PULL_STREAM_TEST_DATA = load_test_data('pull_stream.json')
PUSH_STREAM_TEST_DATA = load_test_data('push_stream.json')
LIST_STREAMS_IDS_TEST_DATA = load_test_data('list_streams_ids.json')
GET_STREAM_INFO_TEST_DATA = load_test_data('get_stream_info.json')
LIST_STREAMS_TEST_DATA = load_test_data('list_streams.json')
GET_STREAMS_COUNT_TEST_DATA = load_test_data('get_streams_count.json')
SHUTDOWN_STREAM_TEST_DATA = load_test_data('shutdown_stream.json')
LIST_CONFIG_TEST_DATA = load_test_data('list_config.json')
REMOVE_CONFIG_TEST_DATA = load_test_data('remove_config.json')
GET_CONFIG_INFO_TEST_DATA = load_test_data('get_config_info.json')
ADD_STREAM_ALIAS_TEST_DATA = load_test_data('add_stream_alias.json')
LIST_STREAM_ALIASES_TEST_DATA = load_test_data('list_stream_aliases.json')
REMOVE_STREAM_ALIAS_TEST_DATA = load_test_data('remove_stream_alias.json')
FLUSH_STREAM_ALIASES_TEST_DATA = load_test_data('flush_stream_aliases.json')
ADD_GROUP_NAME_ALIAS_TEST_DATA = load_test_data('add_group_name_alias.json')
FLUSH_GROUP_NAME_ALIASES_TEST_DATA = load_test_data('flush_group_name_aliases.json')
GET_GROUP_NAME_BY_ALIAS_TEST_DATA = load_test_data('get_group_name_by_alias.json')
LIST_GROUP_NAME_ALIASES_TEST_DATA = load_test_data('list_group_name_aliases.json')
REMOVE_GROUP_NAME_ALIAS_TEST_DATA = load_test_data('remove_group_name_alias.json')
LIST_HTTP_STREAMING_SESSIONS_TEST_DATA = load_test_data('list_http_streaming_sessions.json')
CREATE_INGEST_POINT_TEST_DATA = load_test_data('create_ingest_point.json')
REMOVE_INGEST_POINT_TEST_DATA = load_test_data('remove_ingest_point.json')
LIST_INGEST_POINTS_TEST_DATA = load_test_data('list_ingest_points.json')
CREATE_HLS_STREAM_TEST_DATA = load_test_data('create_hls_stream.json')
CREATE_HDS_STREAM_TEST_DATA = load_test_data('create_hds_stream.json')
IS_STREAM_RUNNING_TEST_DATA = load_test_data('is_stream_running.json')


class EmsTestCase(TestCase):
    data = None

    def setUp(self):
        self.api = Api('http://127.0.0.1:8000')
        self.api.protocol = TestHTTPProtocol(self.data)


class PullStreamTestCase(EmsTestCase):
    data = PULL_STREAM_TEST_DATA

    def test_api(self):
        out = self.api.pull_stream(uri='rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4',
                                   localStreamName='testpullstream')
        self.assertDictEqual(out, self.data['data'])


class PushStreamTestCase(EmsTestCase):
    data = PUSH_STREAM_TEST_DATA

    def test_api(self):
        out = self.api.push_stream(uri='rtmp://DestinationAddress/live',
                                   localStreamName='testpullstream', targetStreamName='testpushStream')
        self.assertDictEqual(out, self.data['data'])


class ListStreamsIdsTestCase(EmsTestCase):
    data = LIST_STREAMS_IDS_TEST_DATA

    def test_api(self):
        out = self.api.list_streams_ids()
        self.assertListEqual(out, self.data['data'])


class GetStreamInfoTestCase(EmsTestCase):
    data = GET_STREAM_INFO_TEST_DATA

    def test_api(self):
        out = self.api.get_stream_info(id=1)
        self.assertDictEqual(out, self.data['data'])


class ListStreamsTestCase(EmsTestCase):
    data = LIST_STREAMS_TEST_DATA

    def test_api(self):
        out = self.api.list_streams()
        self.assertListEqual(out, self.data['data'])


class GetStreamsCountTestCase(EmsTestCase):
    data = GET_STREAMS_COUNT_TEST_DATA

    def test_api(self):
        out = self.api.get_streams_count()
        self.assertDictEqual(out, self.data['data'])


class ShutdownStreamTestCase(EmsTestCase):
    data = SHUTDOWN_STREAM_TEST_DATA

    def test_api(self):
        out = self.api.shutdown_stream(id=55)
        self.assertDictEqual(out, self.data['data'])


class ListConfigTestCase(EmsTestCase):
    data = LIST_CONFIG_TEST_DATA

    def test_api(self):
        out = self.api.list_config()
        self.assertDictEqual(out, self.data['data'])


class RemoveConfigTestCase(EmsTestCase):
    data = REMOVE_CONFIG_TEST_DATA

    def test_api(self):
        out = self.api.remove_config(id=555)
        self.assertDictEqual(out, self.data['data'])


class GetConfigInfoTestCase(EmsTestCase):
    data = GET_CONFIG_INFO_TEST_DATA

    def test_api(self):
        out = self.api.get_config_info(1)
        self.assertDictEqual(out, self.data['data'])


class AddStreamAliasTestCase(EmsTestCase):
    data = ADD_STREAM_ALIAS_TEST_DATA

    def test_api(self):
        out = self.api.add_stream_alias('MyStream', 'video1', expirePeriod=-300)
        self.assertDictEqual(out, self.data['data'])


class ListStreamAliasesTestCase(EmsTestCase):
    data = LIST_STREAM_ALIASES_TEST_DATA

    def test_api(self):
        out = self.api.list_stream_aliases()
        self.assertListEqual(out, self.data['data'])


class RemoveStreamAliasTestCase(EmsTestCase):
    data = REMOVE_STREAM_ALIAS_TEST_DATA

    def test_api(self):
        out = self.api.remove_stream_alias(aliasName='video1')
        self.assertDictEqual(out, self.data['data'])


class FlushStreamAliasesTestCase(EmsTestCase):
    data = FLUSH_STREAM_ALIASES_TEST_DATA

    def test_api(self):
        out = self.api.flush_stream_aliases()
        self.assertIsNone(out)


class AddGroupNameAliasTestCase(EmsTestCase):
    data = ADD_GROUP_NAME_ALIAS_TEST_DATA

    def test_api(self):
        out = self.api.add_group_name_alias(groupName='MyGroup', aliasName='TestGroupAlias')
        self.assertDictEqual(out, self.data['data'])


class FlushGroupNameAliasesTestCase(EmsTestCase):
    data = FLUSH_GROUP_NAME_ALIASES_TEST_DATA

    def test_api(self):
        out = self.api.flush_stream_aliases()
        self.assertIsNone(out)


class GetGroupNameByAliasTestCase(EmsTestCase):
    data = GET_GROUP_NAME_BY_ALIAS_TEST_DATA

    def test_api(self):
        out = self.api.get_group_name_by_alias(aliasName='TestGroupAlias')
        self.assertDictEqual(out, self.data['data'])


class ListGroupNameAliasesTestCase(EmsTestCase):
    data = LIST_GROUP_NAME_ALIASES_TEST_DATA

    def test_api(self):
        out = self.api.list_group_name_aliases()
        self.assertListEqual(out, self.data['data'])


class RemoveGroupNameAliasTestCase(EmsTestCase):
    data = REMOVE_GROUP_NAME_ALIAS_TEST_DATA

    def test_api(self):
        out = self.api.remove_group_name_alias(aliasName='TestGroupAlias')
        self.assertDictEqual(out, self.data['data'])


class ListHttpStreamingSessionsTestCase(EmsTestCase):
    data = LIST_HTTP_STREAMING_SESSIONS_TEST_DATA

    def test_api(self):
        out = self.api.list_http_streaming_sessions()
        self.assertListEqual(out, self.data['data'])


class CreateIngestPointTestCase(EmsTestCase):
    data = CREATE_INGEST_POINT_TEST_DATA

    def test_api(self):
        out = self.api.create_ingest_point(privateStreamName='theIngestPoint', publicStreamName='useMeToViewStream')
        self.assertDictEqual(out, self.data['data'])


class RemoveIngestPointTestCase(EmsTestCase):
    data = REMOVE_INGEST_POINT_TEST_DATA

    def test_api(self):
        out = self.api.remove_ingest_point(privateStreamName='theIngestPoint')
        self.assertDictEqual(out, self.data['data'])


class ListIngestPointsTestCase(EmsTestCase):
    data = LIST_INGEST_POINTS_TEST_DATA

    def test_api(self):
        out = self.api.list_ingest_points()
        self.assertListEqual(out, self.data['data'])


class CreateHLSStreamTestCase(EmsTestCase):
    data = CREATE_HLS_STREAM_TEST_DATA

    def test_api(self):
        out = self.api.create_hls_stream('hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls',
                                         playlistType='rolling', playlistLength=10, chunkLength=5)
        self.assertDictEqual(out, self.data['data'])


class CreateHDSStreamTestCase(EmsTestCase):
    data = CREATE_HDS_STREAM_TEST_DATA

    def test_api(self):
        out = self.api.create_hds_stream('testpullStream', '../evo-webroot', groupName='hds', playlistType='rolling')
        self.assertDictEqual(out, self.data['data'])


class IsStreamRunningTestCase(EmsTestCase):
    data = IS_STREAM_RUNNING_TEST_DATA

    def test_api(self):
        out = self.api.is_stream_running(id=1)
        self.assertDictEqual(out, self.data['data'])

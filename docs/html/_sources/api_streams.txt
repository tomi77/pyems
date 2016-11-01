.. _ref-api_streams:

=======
Streams
=======

``pull_stream``
===============

This will try to pull in a stream from an external source. Once a stream
has been successfully pulled it is assigned a 'local stream name' which can
be used to access the stream from the EMS.

Required:

:``uri`` `(str)`:
    The URI of the external stream. Can be RTMP, RTSP or
    unicast/multicast (d) mpegts

Optional:

:``keepAlive`` `(int)`:
    If keepAlive is set to 1, the server will attempt to
    reestablish connection with astream source after a connection has been
    lost. The reconnect will be attempted once every second
    (default: 1 true)

:``localStreamName`` `(str)`:
    If provided, the stream will be given this
    name. Otherwise, a fallback techniqueis used to determine the stream
    name (based on the URI)

:``forceTcp`` `(int)`:
    If 1 and if the stream is RTSP, a TCP connection will
    be forced. Otherwise the transport mechanism will be negotiated (UDP
    or TCP) (default: 1 true)

:``tcUrl`` `(str)`:
    When specified, this value will be used to set the TC URL in
    the initial RTMPconnect invoke

:``pageUrl`` `(str)`:
    When specified, this value will be used to set the
    originating web page address inthe initial RTMP connect invoke

:``swfUrl`` `(str)`:
    When specified, this value will be used to set the
    originating swf URL in theinitial RTMP connect invoke

:``rangeStart`` `(int)`:
    For RTSP and RTMP connections.  A value fromwhich the
    playback should start expressed in seconds. There are 2 specialvalues:
    -2 and -1. For more information, please read about start/len
    parameters here: http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000185.html

:``rangeEnd`` `(int)`:
    The length in seconds for the playback. -1 is a special
    value. For more information, please read about start/len parameters
    here: http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000185.html

:``ttl`` `(int)`:
    Sets the IP_TTL (time to live) option on the socket

:``tos`` `(int)`:
    Sets the IP_TOS (Type of Service) option on the socket

:``rtcpDetectionInterval`` `(int)`:
    How much time (in seconds) should the server
    wait for RTCP packets before declaring the RTSP stream as a RTCP-less
    stream

:``emulateUserAgent`` `(str)`:
    When specified, this value will be used as the
    user agent string. It is meaningful only for RTMP

:``isAudio`` `(int)`:
    If 1 and if the stream is RTP, it indicates that the
    currently pulled stream is an audio source. Otherwise the pulled
    source is assumed as a video source

:``audioCodecBytes`` `(str)`:
    The audio codec setup of this RTP stream if it is
    audio. Represented as hex format without ‘0x’ or ‘h’. For example:
    audioCodecBytes=1190

:``spsBytes`` `(str)`:
    The video SPS bytes of this RTP stream if it is video. It
    should be base 64 encoded.

:``ppsBytes`` `(str)`:
    The video PPS bytes of this RTP stream if it is video. It
    should be base 64 encoded

:``ssmIp`` `(str)`:
    The source IP from source-specific-multicast. Only usable
    when doing UDP based pull

:``httpProxy`` `(str)`:
    This parameter has two valid values: IP:Port – This
    value combination specifies an RTSP HTTP Proxy from which the RTSP
    stream should be pulled from Self - Specifying “self” as the value
    implies pulling RTSP over HTTP

Example:

.. sourcecode:: python

 api.pull_stream('rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4', localStreamName='testpullStream')

http://docs.evostream.com/ems_api_definition/pullstream

``push_stream``
===============

Try to push a local stream to an external destination. The pushed stream
can only use the RTMP, RTSP or MPEG-TS unicast/multicast protocol.

Required:

:``uri`` `(str)`:
    The URI of the external stream. Can be RTMP, RTSP or unicast/multicast
    (d) mpegts.

Optional:

:``keepAlive`` `(int)`:
    If ``keepAlive`` is set to 1, the server will attempt to reestablish
    connection with a stream source after a connection has been lost. The
    reconnect will be attempted once every second.

:``localStreamName`` `(str)`:
    If provided, the stream will be given this name. Otherwise, a fallback
    techniques used to determine the stream name (based on the URI).

:``targetStreamName`` `(str)`:
    The name of the stream at destination. If not provided, the target
    stream name will be the same as the local stream name.

:``targetStreamType`` `(str)`:
    It can be one of following: **live**, **record**, **append**. It is
    meaningful only for RTMP.

:``tcUrl`` `(str)`:
    When specified, this value will be used to set the TC URL in the initial
    RTMP connect invoke.

:``pageUrl`` `(str)`:
    When specified, this value will be used to set the originating web page
    address in the initial RTMP connect invoke.

:``swfUrl`` `(str)`:
    When specified, this value will be used to set the originating swf URL
    in the initial RTMP connect invoke.

:``ttl`` `(int)`:
    Sets the IP_TTL (time to live) option on the socket.

:``tos`` `(int)`:
    Sets the IP_TOS (Type of Service) option on the socket.

:``emulateUserAgent`` `(str)`:
    When specified, this value will be used as the user agent string.
    It is meaningful only for RTMP.

:``rtmpAbsoluteTimestamps`` `(int)`:
    Forces the timestamps to be absolute when using RTMP.

:``sendChunkSizeRequest`` `(int)`:
    Sets whether the RTMP stream will or will not send a "Set Chunk Length"
    message. This is significant when pushing to Akamai’s new RTMP HD
    ingest point where this parameter should be set to 0 so that Akamai will
    not drop the connection.

:``useSourcePts`` `(int)`:
    When value is true, timestamps on source inbound RTMP stream are passed
    directly to the outbound (pushed) RTMP streams. This affects only pushed
    Outbound Net RTMP with net RTMP source. This parameter overrides the
    value of the config.lua option of the same name.

Example:

.. sourcecode:: python

 api.push_stream('rtmp://DestinationAddress/live' localStreamName='testpullstream' targetStreamName='testpushStream')

http://docs.evostream.com/ems_api_definition/pushstream

``create_hls_stream``
=====================

Create an HTTP Live Stream (HLS) out of an existing H.264/AAC stream. HLS
is used to stream live feeds to iOS devices such as iPhones and iPads.

Required:

:``localStreamNames`` `(str)`: The stream(s) that will be used as the input.
    This is a comma-delimited list of active stream names (local stream names).

:``targetFolder`` `(str)`: The folder where all the .ts/.m3u8 files will be
    stored. This folder must be accessible by the HLS clients. It is
    usually in the web-root of the server.

Optional:

:``keepAlive`` `(int)`: If true, the EMS will attempt to reconnect to the
    stream source if the connection is severed.

:``overwriteDestination`` `(int)`: If true, it will force overwrite of
    destination files.

:``staleRetentionCount`` `(int)`: The number of old files kept besides the ones
    listed in the current version of the playlist. Only applicable for
    rolling playlists.

:``createMasterPlaylist`` `(int)`: If true, a master playlist will be created.

:``cleanupDestination`` `(int)`: If true, all \*.ts and \*.m3u8 files in the
    target folder will be removed before HLS creation is started.

:``bandwidths`` `(int)`: The corresponding bandwidths for each stream listed in
    localStreamNames. Again, this can be a comma-delimited list.

:``groupName`` `(str)`: The name assigned to the HLS stream or group. If the
    localStreamNames parameter contains only one entry and groupName is
    not specified, groupName will have the value of the input stream name.

:``playlistType`` `(str)`: Either appending or rolling.

:``playlistLength`` `(int)`: The length (number of elements) of the playlist.
    Used only when playlistType is rolling. Ignored otherwise.

:``playlistName`` `(str)`: The file name of the playlist (\*.m3u8).

:``chunkLength`` `(int)`: The length (in seconds) of each playlist element (\*.ts
    file). Minimum value is 1 (second).

:``maxChunkLength`` `(int)`: Maximum length (in seconds) the EMS will allow any
    single chunk to be. This is primarily in the case of chunkOnIDR=true where
    the EMS will wait for the next key-frame. If the maxChunkLength is less than
    chunkLength, the parameter shall be ignored.

:``chunkBaseName`` `(str)`: The base name used to generate the \*.ts chunks.

:``chunkOnIDR`` `(int)`: If true, chunking is performed ONLY on IDR. Otherwise,
    chunking is performed whenever chunk length is achieved.

:``drmType`` `(str)`: Type of DRM encryption to use. Options are: none
    (no encryption), evo (AES Encryption), SAMPLE-AES (Sample-AES),
    verimatrix (Verimatrix DRM). For Verimatrix DRM, the "drm" section of
    the config.lua file must be active and properly configured.

:``AESKeyCount`` `(int)`: Number of keys that will be automatically generated
    and rotated over while encrypting this HLS stream.

:``audioOnly`` `(int)`: If true, stream will be audio only.

:``hlsResume`` `(int)`: If true, HLS will resume in appending segments to
    previously created child playlist even in cases of EMS shutdown or cut
    off stream source.

:``cleanupOnClose`` `(int)`: If true, corresponding hls files to a stream will
    be deleted if the said stream is removed or shut down or disconnected.

:``useByteRange`` `(int)`: If true, will use the EXT-X-BYTERANGE feature of HLS
    (version 4 and up).

:``fileLength`` `(int)`: When using useByteRange=1, this parameter needs to be
    set too. This will be the size of file before chunking it to another
    file, this replace the chunkLength in case of EXT-X-BYTERANGE, since
    chunkLength will be the byte range chunk.

:``useSystemTime`` `(int)`: If true, uses UTC in playlist time stamp otherwise
    will use the local server time.

:``offsetTime`` `(int)`:

:``startOffset`` `(int)`: A parameter valid only for HLS v.6 onwards. This will
    indicate the start offset time (in seconds) for the playback of the
    playlist.

Example:

.. sourcecode:: python

 api.create_hls_stream('hlstest', '/MyWebRoot/', bandwidths=128, groupName='hls', playlistType='rolling', playlistLength=10, chunkLength=5)

http://docs.evostream.com/ems_api_definition/createhlsstream

``create_hds_stream``
=====================

Create an HDS (HTTP Dynamic Streaming) stream out of an existing H.264/AAC
stream. HDS is used to stream standard MP4 media over regular HTTP
connections.

Required:

:``localStreamNames`` `(str)`: The stream(s) that will be used as the input.
    This is a comma-delimited list of active stream names (local stream
    names).

:``targetFolder`` `(str)`: The folder where all the manifest (*.f4m) and
    fragment (f4v*) files will be stored. This folder must be accessible by
    the HDS clients. It is usually in the web-root of the server.

Optional:

:``bandwidths`` `(int)`: The corresponding bandwidths for each stream listed in
    localStreamNames. Again, this can be a comma-delimited list.

:``chunkBaseName`` `(str)`: The base name used to generate the fragments.

:``chunkLength`` `(int)`: The length (in seconds) of fragments to be made.
    Minimum value is 1 (second)

:``chunkOnIDR`` `(int)`: If true, chunking is performed ONLY on IDR. Otherwise,
    chunking is performed whenever chunk length is achieved.

:``groupName`` `(str)`: The name assigned to the HDS stream or group. If the
    ``localStreamNames`` parameter contains only one entry and ``groupName`` is
    not specified, ``groupName`` will have the value of the input stream name.

:``keepAlive`` `(int)`: If true, the EMS will attempt to reconnect to the
    stream source if the connection is severed.

:``manifestName`` `(str)`: The manifest file name.

:``overwriteDestination`` `(int)`: If true, it will allow overwrite of
    destination files.

:``playlistType`` `(str)`: Either `appending` or `rolling`.

:``playlistLength`` `(int)`: The number of fragments before the server starts to
    overwrite the older fragments. Used only when ``playlistType`` is
    `rolling`. Ignored otherwise.
:type playlistLength: int

:``staleRetentionCount`` `(int)`: The number of old files kept besides the ones
    listed in the current version of the playlist. Only applicable for
    `rolling` playlists.

:``createMasterPlaylist`` `(int)`: If true, a master playlist will be created.

:``cleanupDestination`` `(int)`: If true, all manifest and fragment files in the
    target folder will be removed before HDS creation is started.

Example:

.. sourcecode:: python

 api.create_hds_stream('testpullStream', '../evo-webroot', groupName='hds', playlistType='rolling')

http://docs.evostream.com/ems_api_definition/createhdsstream

``create_mss_stream``
=====================

Create a Microsoft Smooth Stream (MSS) out of an existing H.264/AAC
stream. Smooth Streaming was developed by Microsoft to compete with
other adaptive streaming technologies.

Required:

:``localStreamNames`` `(str)`: The stream(s) that will be used as the input.
    This is a comma-delimited list of active stream names (local
    stream names)

:``targetFolder`` `(str)`: The folder where all the manifest and fragment
    files will be stored. This folder must be accessible by the MSS
    clients. It is usually in the web-root of the server.

Optional:

:``bandwidths`` `(str)`: The corresponding bandwidths for each stream listed
    in ``localStreamNames``. Again, this can be a comma-delimited list.

:``groupName`` `(str)`: The name assigned to the MSS stream or group. If the
    ``localStreamNames`` parameter contains only one entry and groupName
    is not specified, groupName will have the value of the input
    stream name.

:``playlistType`` `(str)`: Either `appending` or `rolling`

:``playlistLength`` `(int)`: The number of fragments before the server
    starts to overwrite the older fragments. Used only when
    ``playlistType`` is `rolling`. Ignored otherwise.

:``manifestName`` `(str)`: The manifest file name.

:``chunkLength`` `(int)`: The length (in seconds) of fragments to be made.

:``chunkOnIDR`` `(int)`: If 1 (true), chunking is performed ONLY on IDR.
    Otherwise, chunking is performed whenever chunk length is
    achieved.

:``keepAlive`` `(int)`: If 1 (true), the EMS will attempt to reconnect to
    the stream source if the connection is severed.

:``overwriteDestination`` `(int)`: If 1 (true), it will allow overwrite of
    destination files.

:``staleRetentionCount`` `(int)`: How many old files are kept besides the
    ones present in the current version of the playlist. Only
    applicable for rolling playlists.

:``cleanupDestination`` `(int)`: If 1 (true), all manifest and fragment
    files in the target folder will be removed before MSS creation is
    started.

:``ismType`` `(int)`: Either ismc for serving content to client or isml for
    serving content to smooth server.

:``isLive`` `(int)`: If true, creates a live MSS stream, otherwise set to 0
    for VOD.

:``publishingPoint`` `(str)`: This parameter is needed when `ismType=isml`,
    it is the REST URI where the mss contents will be ingested.

:``ingestMode`` `(str)`: Either `single` for a non looping ingest or `loop`
    for looping an ingest.

Example:

.. sourcecode:: python

 api.create_mss_stream('testpullStream', '../evo-webroot', groupName='mss')

http://docs.evostream.com/ems_api_definition/createmssstream

``create_dash_stream``
======================

Create Dynamic Adaptive Streaming over HTTP (DASH) out of an existing
H.264/AAC stream. DASH was developed by the Moving Picture Experts
Group (MPEG) to establish a standard for HTTP adaptive-bitrate
streaming that would be accepted by multiple vendors and facilitate
interoperability.

Required:

:``localStreamNames`` `(str)`: The stream(s) that will be used as the
    input. This is a comma-delimited list of active stream names
    (local stream names).

:``targetFolder`` `(str)`: The folder where all the manifest and fragment
    files will be stored. This folder must be accessible by the DASH
    clients. It is usually in the web-root of the server.

Optional:

:``bandwidths`` `(str)`: The corresponding bandwidths for each stream listed
    in ``localStreamNames``. Again, this can be a comma-delimited list.

:``groupName`` `(str)`: The name assigned to the DASH stream or group. If
    the ``localStreamNames`` parameter contains only one entry and
    ``groupName`` is not specified, ``groupName`` will have the value of
    the input stream name.

:``playlistType`` `(str)`: Either `appending` or `rolling`.

:``playlistLength`` `(int)`: The number of fragments before the server
    starts to overwrite the older fragments. Used only when
    ``playlistType`` is `rolling`. Ignored otherwise.

:``manifestName`` `(str)`: The manifest file name.

:``chunkLength`` `(int)`: The length (in seconds) of fragments to be made.

:``chunkOnIDR`` `(int)`: If true, chunking is performed ONLY on IDR.
    Otherwise, chunking is performed whenever chunk length is
    achieved.

:``keepAlive`` `(int)`: If true, the EMS will attempt to reconnect to the
    stream source if the connection is severed.

:``overwriteDestination`` `(int)`: If true, it will allow overwrite of
    destination files.

:``staleRetentionCount`` `(int)`: How many old files are kept besides the
    ones present in the current version of the playlist. Only
    applicable for rolling playlists.

:``cleanupDestination`` `(int)`: If true, all manifest and fragment files in
    the target folder will be removed before DASH creation is started.

:``dynamicProfile`` `(int)`: Set this parameter to 1 (default) for a live
    DASH, otherwise set it to 0 for a VOD.

Example:

.. sourcecode:: python

 api.create_dash_stream('testpullStream', '../evo-webroot', groupName='dash')

http://docs.evostream.com/ems_api_definition/createdashstream

``record``
==========

Records any inbound stream. The record command allows users to record
a stream that may not yet exist. When a new stream is brought into
the server, it is checked against a list of streams to be recorded.

Streams can be recorded as FLV files, MPEG-TS files or as MP4 files.

Required:

:``localStreamName`` `(str)`: The name of the stream to be used as input
    for recording.

:``pathToFile`` `(str)`: Specify path and file name to write to.

Optional:

:``type`` `(str)`: `ts`, `mp4` or `flv`

:``overwrite`` `(int)`: If false, when a file already exists for the stream
    name, a new file will be created with the next appropriate number
    appended. If 1 (true), files with the same name will be
    overwritten.

:``keepAlive`` `(int)`: If 1 (true), the server will restart recording every
    time the stream becomes available again.

:``chunkLength`` `(int)`: If non-zero the record command will start a new
    recording file after ChunkLength seconds have elapsed.

:``waitForIDR`` `(int)`: This is used if the recording is being chunked.
    When true, new files will only be created on IDR boundaries.

:``winQtCompat`` `(int)`: Mandates 32bit header fields to ensure
    compatibility with Windows QuickTime.

:``dateFolderStructure`` `(int)`: If set to 1 (true), folders will be
    created with names in `YYYYMMDD` format. Recorded files will be
    placed inside these folders based on the date they were created.

Example:

.. sourcecode:: python

 api.record('testpullstream', '../media/testRecord', type='mp4', overwrite=1)

http://docs.evostream.com/ems_api_definition/record

``transcode``
=============

Changes the compression characteristics of an audio and/or video
stream. Allows you to change the resolution of a source stream, change
the bitrate of a stream, change a VP8 or MPEG2 stream into H.264 and
much more. Allow users to create overlays on the final stream as well
as crop streams.

Required:

:``source`` `(str)`: Can be a URI or a local stream name from EMS.

:``destinations`` `(str)`: The target URI(s) or stream name(s) of the
    transcoded stream. If only a name is given, it will be pushed
    back to the EMS.

Optional:

:``targetStreamNames`` `(str)`: The name of the stream(s) at destination(s).
    If not specified, and a full URI is provided to destinations,
    name will have a time stamped value.

:``groupName`` `(str)`: The group name assigned to this process. If not
    specified, groupName will have a random value.

:``videoBitrates`` `(str)`: Target output video bitrate(s) (in bits/s,
    append `k` to value for kbits/s). Accepts the value `copy` to
    copy the input bitrate. An empty value passed would mean no video.

:``videoSizes`` `(str)`: Target output video size(s) in wxh (width x height)
    format. IE: `240x480`.

:``videoAdvancedParamsProfiles`` `(str)`: Name of video profile template
    that will be used.

:``audioBitrates`` `(str)`: Target output audio bitrate(s) (in bits/s,
    append `k` to value for kbits/s). Accepts the value `copy` to
    copy the input bitrate. An empty value passed would mean no audio.

:``audioChannelsCounts`` `(str)`: Target output audio channel(s) count(s).
    Valid values are 1 (mono), 2 (stereo), and so on. Actual supported
    channel count is dependent on the number of input audio channels.

:``audioFrequencies`` `(str)`: Target output audio frequency(ies) (in Hz,
    append `k` to value for kHz).

:``audioAdvancedParamsProfiles`` `(str)`: Name of audio profile template
    that will be used.

:``overlays`` `(str)`: Location of the overlay source(s) to be used. These
    are transparent images (normally in PNG format) that have the same
    or smaller size than the video. Image is placed at the top-left
    position of the video.

:``croppings`` `(str)`: Target video cropping position(s) and size(s) in
    `left : top : width : height` format (e.g. `0:0:200:100`. Positions
    are optional (`200:100` for a centered cropping of `200` width and `100`
    height in pixels). Values are limited to the actual size of the
    video.

:``keepAlive`` `(int)`: If keepAlive is set to 1, the server will restart
    transcoding if it was previously activated.

:``commandFlags`` `(str)`: Other commands to the transcode process that are
    not supported by the baseline transcode command.

Example:

.. sourcecode:: python

 api.transcode('rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4', 'stream1', groupName='group', videoBitrates='200k')

http://docs.evostream.com/ems_api_definition/transcode

``list_streams_ids``
====================

Get a list of IDs for every active stream.

Example:

.. sourcecode:: python

 api.list_streams_ids()

http://docs.evostream.com/ems_api_definition/liststreamsids

``get_stream_info``
===================

Returns a detailed set of information about a stream.

Required:

One of these parameters is required.

:``id`` `(int)`:
    The uniqueId of the stream. Usually a value returned by listStreamsIDs.

:``localStreamName`` `(str)`:
    The name of the stream.

Example:

.. sourcecode:: python

 api.get_stream_info(id=1)

http://docs.evostream.com/ems_api_definition/getstreaminfo

``list_streams``
================

Provides a detailed description of all active streams.

Optional:

:``disableInternalStreams`` `(int)`:
    If this is 1 (true), internal streams (origin-edge related) are filtered
    out from the list

Example:

.. sourcecode:: python

 api.list_streams()

http://docs.evostream.com/ems_api_definition/liststreams

``get_streams_count``
=====================

Returns the number of active streams.

Example:

.. sourcecode:: python

 api.get_streams_count()

``shutdown_stream``
===================

Terminates a specific stream. When ``permanently=1`` is used, this command is
analogous to ``remove_config``.

Required:

One of these parameters is required.

:``id`` `(int)`:
    The uniqueId of the stream that needs to be terminated. The
    stream ID’s can be obtained using the listStreams command.

:``localStreamName`` `(str)`:
    The name of the inbound stream which you wish to
    terminate. This will also terminate any outbound streams that are
    dependent upon this input stream.

Optional:

:``permanently`` `(int)`:
    If true, the corresponding push/pull configuration will
    also be terminated. Therefore, the stream will NOT be reconnected when
    the server restarts

Example:

.. sourcecode:: python

 api.shutdown_stream(id=55)

http://docs.evostream.com/ems_api_definition/shutdownstream

``list_config``
===============

Returns a list with all push/pull configurations.

Whenever the pullStream or pushStream interfaces are called, a record
containing the details of the pull or push is created in the
``pullpushconfig.xml`` file. Then, the next time the EMS is started, the
``pullpushconfig.xml`` file is read, and the EMS attempts to reconnect all of
the previous pulled or pushed streams.

Example:

.. sourcecode:: python

 api.list_config()

http://docs.evostream.com/ems_api_definition/listconfig

``remove_config``
=================

This command will both stop the stream and remove the corresponding
configuration entry. This command is the same as performing::

 shutdownStream permanently=1

Required:

One of these parameters is required.

:``id`` `(int)`:
    The configId of the configuration that needs to be removed.
    ConfigId’s can be obtained from the listConfig interface. Removing an
    inbound stream will also automatically remove all associated outbound
    streams.

:``groupName`` `(str)`:
    The name of the group that needs to be removed (applicable to HLS, HDS and
    external processes).

Optional:

:``removeHlsHdsFiles`` `(int)`:
    If 1 (true) and the stream is HLS or HDS, the folder associated with it
    will be removed.

Example:

.. sourcecode:: python

 api.remove_config(id=55)

http://docs.evostream.com/ems_api_definition/removeconfig

``get_config_info``
===================

Returns the information of the stream by the `configId`.

Required:

:``id`` `(int)`:
    The `configId` of the configuration to get some information.

Example:

.. sourcecode:: python

 api.get_config_info(id=1)

http://docs.evostream.com/ems_api_definition/getconfiginfo

``is_stream_running``
=====================

Checks a specific stream if it is running or not.

Required:

One of these parameters is required.

:``id`` `(int)`: The unique id of the stream to check.

:``localStreamName`` `(str)`: The name of the stream to check.

Example:

.. sourcecode:: python

 api.is_stream_running(id=1)
 api.is_stream_running(localStreamName='testStream')

http://docs.evostream.com/ems_api_definition/isstreamrunning

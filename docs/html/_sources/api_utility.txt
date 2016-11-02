.. _ref-api_utility:

=================================
Utility and Feature API Functions
=================================

``start_web_rtc``
=================

Starts a WebRTC signalling client to an ERS (Evostream Rendezvous
Server).

Required:

:``ersip`` `(str)`: IP address (xx.yy.zz.xx) of ERS.

:``ersport`` `(str)`: IP address (xx.yy.zz.xx) of ERS.

:``roomId`` `(str)`: Unique room Identifier within ERS that will be used by
    client browsers to connect to this EMS.

Example:

.. sourcecode:: python

 api.start_web_rtc('52.6.14.61', '3535', 'ThisIsATestRoomName')

http://docs.evostream.com/ems_api_definition/startwebrtc

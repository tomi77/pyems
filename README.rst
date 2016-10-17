==============================
pyems - Python EMS API wrapper
==============================

.. image:: https://codeclimate.com/github/tomi77/pyems/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/pyems
   :alt: Code Climate
.. image:: https://travis-ci.org/tomi77/pyems.svg?branch=master
   :target: https://travis-ci.org/tomi77/pyems
.. image:: https://coveralls.io/repos/github/tomi77/pyems/badge.svg?branch=master
   :target: https://coveralls.io/github/tomi77/pyems?branch=master

Installation
============

Install package via ``pip``
::

    pip install pyems

API Usage
=========

::

    from pyems import Api

    api = Api('http://127.0.0.1:7777')
    print api.list_streams()


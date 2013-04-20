#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati_http
~~~~~~~~~~~

Simple statistics aggregator

HTTP client for GottWall (scalable realtime metrics collecting and aggregation platform and service)


:copyright: (c) 2012 - 2013 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

__all__ = 'get_version', 'Client'
__author__ = "Alex Lispython (alex@obout.ru)"
__license__ = "BSD, see LICENSE for more details"
__maintainer__ = "Alexandr Lispython"

try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('stati_http').version
except Exception, e:
    __version__ = 'unknown'

if __version__ == 'unknown':
    __version_info__ = (0, 0, 0)
else:
    __version_info__ = __version__.split('.')
__build__ = 0x00005


from stati_http.client import Client, HTTPClient

assert Client
assert HTTPClient


def get_version():
    return __version__

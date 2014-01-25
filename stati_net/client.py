#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stati.client
~~~~~~~~~~~~

Client for GottWall

:copyright: (c) 2012 - 2013  by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-python-net
"""
import logging

try:
    import ujson as json
except ImportError:
    import json

import datetime
import time


logger = logging.getLogger('stati')


class Client(object):
    """Base client
    """
    def __init__(self, project, private_key, public_key):
        self._project = project
        self._private_key = private_key
        self._public_key = public_key


    @staticmethod
    def dt_to_ts(dt):
        """Convert datetime object to timestamp

        :param dt:
        :return: ts in seconds
        """
        return int(time.mktime(dt.timetuple()))

    def serialize(self, name, timestamp, value, filters={}):
        """Make data bucket

        :param data: dict of data
        """
        return json.dumps(
            {"n": name,
             "ts": self.dt_to_ts(timestamp),
             "f": filters,
             "v": value})

    def incr(self, name, timestamp=datetime.datetime.now(), value=1,
             filters={}):
        """Add data incrementation

        :param name:
        :param timestamp:
        :param value:
        :param filters:
        """
        raise NotImplementedError


    def decr(self, name, timestamp=datetime.datetime.now(), value=1,
             filters={}):
        """Add data incrementation

        :param name:
        :param timestamp:
        :param value:
        :param filters:
        """
        raise NotImplementedError

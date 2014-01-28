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
import hashlib
import hmac

try:
    import ujson as json
except ImportError:
    import json

from datetime import datetime
import time
from time import mktime


logger = logging.getLogger('stati')


class Client(object):
    """Base client
    """
    def __init__(self, project, private_key, public_key, solt_base=1000):
        self._project = project
        self._private_key = private_key
        self._public_key = public_key
        self._solt_base = solt_base


    @staticmethod
    def dt_to_ts(dt):
        """Convert datetime object to timestamp

        :param dt:
        :return: ts in seconds
        """
        return int(mktime(dt.timetuple()))

    def serialize(self, name, timestamp, value, filters={}):
        """Make data bucket

        :param data: dict of data
        """
        return json.dumps(
            {"n": name,
             "ts": self.dt_to_ts(timestamp),
             "f": filters,
             "v": value})

    def incr(self, name, timestamp=None, value=1,
             filters={}):
        """Add data incrementation

        :param name:
        :param timestamp:
        :param value:
        :param filters:
        """
        raise NotImplementedError


    def decr(self, name, timestamp=None, value=1,
             filters={}):
        """Add data incrementation

        :param name:
        :param timestamp:
        :param value:
        :param filters:
        """
        raise NotImplementedError

    def make_sign(self, ts):
        return hmac.new(key=self._private_key,
                        msg=self.sign_msg(ts),
                        digestmod=hashlib.md5).hexdigest()

    def get_solt(self, ts):
        return int(round(ts / self._solt_base) * self._solt_base)

    def sign_msg(self, ts):
        return str(self._public_key) + str(self.get_solt(ts))

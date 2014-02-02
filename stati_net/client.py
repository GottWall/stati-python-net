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
import six
try:
    import ujson as json
except ImportError:
    import json

from datetime import datetime
import time
from time import mktime


logger = logging.getLogger('stati')

from six import text_type, binary_type


def utf8(value):
    """Converts a string argument to a byte string.

    If the argument is already a byte string or None, it is returned unchanged.
    Otherwise it must be a unicode string and is encoded as utf8.
    """
    if isinstance(value, (binary_type, type(None))):
        return value
    if not isinstance(value, text_type):
        raise TypeError("Expected bytes, unicode, or None; got %r" % type(value))
    return value.encode("utf-8")


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
        return hmac.new(key=utf8(self._private_key), msg=utf8(self.sign_msg(ts)),
                        digestmod=hashlib.md5).hexdigest()

    def get_solt(self, ts):
        return int(round(ts / self._solt_base) * self._solt_base)

    def sign_msg(self, ts):
        return utf8(str(self._public_key) + str(self.get_solt(ts)))

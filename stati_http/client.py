#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stati.client
~~~~~~~~~~~~

Client for GottWall

:copyright: (c) 2012 - 2013  by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-http-python
"""
import logging
import json
import datetime
import time
import requests


logger = logging.getLogger('stati')


class Client(object):
    """Base client
    """
    def __init__(self, project, private_key, public_key):
        self._project = project
        self._private_key = private_key
        self._public_key = public_key

    def serialize(self, name, timestamp, value, filters={}):
        """Make data bucket

        :param data: dict of data
        """
        return json.dumps(
            {"n": name,
             "ts": int(time.mktime(timestamp.timetuple())),
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


class HTTPClient(Client):
    """GottWall client that send data to redis pub/sub
    """

    def __init__(self, project, private_key, public_key,
                 host='http://127.0.0.1/', prefix='/gottwall'):
        super(HTTPClient, self).__init__(project, private_key, public_key)
        self._host = host
        self.prefix = prefix

    def get_url(self, action):
        return "{host}{prefix}/api/v1/{project}/{action}".format(
            action=action, project=self._project,
            prefix=self.prefix if self.prefix else '',
            host = self._host)

    @property
    def headers(self):
        return {"Content-Type": "application/json",
                "X-GottWall-Auth": "GottWall private_key={0}, public_key={1}".format(
                    self._private_key, self._public_key)}

    def incr(self, name, timestamp=None, value=1, filters={}):
        timestamp = timestamp or datetime.datetime.now()

        try:
            requests.post(self.get_url('incr'), data=self.serialize(name, timestamp, value, filters),
                          headers=self.headers)
        except Exception, e:
            print(e)
            logger.warn(e)

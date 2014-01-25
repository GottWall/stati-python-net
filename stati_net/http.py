#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stati.client
~~~~~~~~~~~~

Client for GottWall

:copyright: (c) 2012 - 2014  by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-python-net
"""
import logging
import datetime
import requests

from stati_net.client import Client

logger = logging.getLogger('stati')


class HTTPClient(Client):
    """GottWall client to send data via
    """

    def __init__(self, project, private_key, public_key,
                 host='http://127.0.0.1', prefix='/gottwall', port=80):
        super(HTTPClient, self).__init__(project, private_key, public_key)
        self._host = host
        self._port = port
        self.prefix = prefix

    def get_url(self, action):
        return "{host}:{port}{prefix}/api/v1/{project}/{action}".format(
            action=action, project=self._project,
            prefix=self.prefix if self.prefix else '/',
            host=self._host, port=self._port)

    @property
    def headers(self):
        return {"Content-Type": "application/json",
                "X-GottWall-Auth": "GottWall private_key={0}, public_key={1}".format(
                    self._private_key, self._public_key)}

    def request(self, action, name, timestamp=None, value=1, filters={}):
        """Make request to api

        :param action: api action
        :param name: metric name
        :param timestamp: timestamp
        :param value: metric value
        :param filters: filters fict
        :return: request result
        """

        timestamp = timestamp or datetime.datetime.utcnow()

        try:
            return requests.post(self.get_url(action), data=self.serialize(name, timestamp, value, filters),
                                 headers=self.headers).status_code == requests.codes.ok
        except Exception as e:
            logger.error(e)
            return False
        return True

    def incr(self, *args, **kwargs):
        return self.request('incr', *args, **kwargs)

    def decr(self, *args, **kwargs):
        return self.request('decr', *args, **kwargs)

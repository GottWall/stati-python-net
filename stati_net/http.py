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
from datetime import datetime
import requests

from stati_net.client import Client
import hmac

logger = logging.getLogger('stati')


class HTTPClient(Client):
    """GottWall client to send data via
    """

    def __init__(self, project, private_key, public_key,
                 host='http://127.0.0.1', prefix='/gottwall', port=80,
                 proto="http", secure_auth=False, solt_base=1000):
        super(HTTPClient, self).__init__(project, private_key, public_key, solt_base)
        self.host, self.port, self.proto, self.prefix = host, port, proto, prefix
        self._secure_auth = secure_auth
        self._auth_header = None


    def get_url(self, action):
        return "{proto}://{host}:{port}{prefix}/api/v1/{project}/{action}".format(
            action=action, project=self._project,
            prefix=self.prefix or '', host=self.host, port=self.port,
            proto=self.proto or 'http')

    @property
    def headers(self):
        return {"Content-Type": "application/json",
                "X-GottWall-Auth": self.auth_header}

    @property
    def auth_header(self):
        ts = self.dt_to_ts(datetime.utcnow())
        return "GottWallS1 {0} {1} {2}".format(ts, self.make_sign(ts), self._solt_base)

    def request(self, action, name, timestamp=None, value=1, filters={}):
        """Make request to api

        :param action: api action
        :param name: metric name
        :param timestamp: timestamp
        :param value: metric value
        :param filters: filters fict
        :return: request result
        """

        timestamp = timestamp or datetime.utcnow()

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

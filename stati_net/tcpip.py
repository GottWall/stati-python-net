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
import socket
from datetime import datetime

from stati_net.client import Client

try:
    import ujson as json
except Exception:
    import json


logger = logging.getLogger('stati')


class TCPIPClient(Client):
    """GottWall client to send data via custom TCP/IP protocol
    """

    def __init__(self, project, private_key, public_key,
                 host='127.0.0.1', port=8097, solt_base=1000,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 auth_delimiter="--stream-auth--", chunk_delimiter="--chunk--"):
        super(TCPIPClient, self).__init__(project, private_key, public_key, solt_base)
        self.host, self.port = host, port
        self.timeout = timeout
        self.authenticated = False
        self.auth_delimiter = auth_delimiter
        self.chunk_delimiter = chunk_delimiter
        self.sock = None

    @property
    def auth_header(self):
        ts = self.dt_to_ts(datetime.utcnow())
        return "GottWallS2 {0} {1} {2} {3}".format(
            ts, self.make_sign(ts), self._solt_base, self._project)


    def serialize(self, auth, action, name, timestamp, value, filters={}):
        """Serialize data to json

        """
        return json.dumps({"p": self._project,
                           "n": name,
                           "auth": self.auth_header,
                           "ts": self.dt_to_ts(timestamp),
                           "a": action,
                           "v": value,
                           "f": filters})


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
            auth = self.auth_header
            self.send_bucket(auth, self.serialize(auth, action, name, timestamp, value, filters))
        except Exception as e:
            print(e)
            #logger.error(e)
            return False
        return True

    def incr(self, *args, **kwargs):
        return self.request('incr', *args, **kwargs)

    def decr(self, *args, **kwargs):
        return self.request('decr', *args, **kwargs)

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        return sock

    @property
    def connection(self):
        if not self.sock:
            self.sock = self.connect()
        return self.sock

    def send_bucket(self, auth, data):
        try:
            if not self.authenticated:
                self.authenticate_connection(auth)
            self.connection.send(data + self.chunk_delimiter)
        except Exception as e:
            print(e)

    def authenticate_connection(self, auth):
        """Authenticate connection
        """
        if not self.sock:
            self.sock = self.connect()
            # Every new connection not authenticated
            self.authenticated = False

        if not self.authenticated:
            self.sock.send(auth + self.auth_delimiter)

            resp = self.sock.recv(2)

            if resp == "OK":
                self.authenticated = True
                return True
            raise RuntimeError("Can't authenticate connection")

        return True

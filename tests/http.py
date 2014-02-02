#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati.tests
~~~~~~~~~~~

Unittests for stati

:copyright: (c) 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
import json
from datetime import datetime
from .base import BaseTestCase
from stati_net import HTTPClient
import responses
from six import b


class HTTPTestCase(BaseTestCase):

    project = "test_gottwall_project"
    private_key = "gottwall_pricatekey"
    public_key = "project_public_key"
    project = "test_gottwall_project"
    host = "127.0.0.1"
    port = 8888
    prefix = "/gottwall"

    test_data = {"name": "orders", "value": 2, "timestamp": datetime.now(),
                 "filters": {"status": ["Completed", "Test"]}}

    def setUp(self):
        self.client = HTTPClient(self.project, self.private_key, self.public_key,
                            host=self.host, port=self.port, prefix=self.prefix,
                            proto="https")


    def test_init(self):
        client = self.client


        self.assertEqual(client.get_url("incr"), "{proto}://{host}:{port}{prefix}/api/v1/{project}/{action}".format(
            project=self.project,  host=self.host, port=self.port, prefix=self.prefix, action='incr', proto="https"))


        data = self.test_data

        serialized_data = client.serialize(data['name'], data['timestamp'], data['value'], data['filters'])
        decoded_data = json.loads(serialized_data)
        self.assertEqual(client.dt_to_ts(data.get('timestamp')),
                          decoded_data['ts'])
        self.assertEqual(data['name'], decoded_data['n'])
        self.assertEqual(data['value'], decoded_data['v'])
        self.assertEqual(data['filters'], decoded_data['f'])


    @responses.activate
    def test_methods(self):
        client = self.client
        responses.add(responses.POST, client.get_url('incr'),
                  body=b('OK'), status=200)
        responses.add(responses.POST, client.get_url('decr'),
                      body=b('OK'), status=500)

        self.assertTrue(client.incr(**self.test_data))
        self.assertFalse(client.decr(**self.test_data))

    def test_headers(self):
        client = self.client

        ts = client.dt_to_ts(datetime.utcnow())
        self.assertEqual(client.auth_header, "GottWallS1 {0} {1} {2}".format(ts, client.make_sign(ts), client._solt_base))

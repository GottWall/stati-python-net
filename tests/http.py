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
from base import BaseTestCase
from stati_net import HTTPClient
import responses


class HTTPTestCase(BaseTestCase):

    project = "test_gottwall_project"
    private_key = "gottwall_pricatekey"
    public_key = "project_public_key"
    project = "test_gottwall_project"
    host = "http://127.0.0.1"
    port = 8888
    prefix = "/gottwall"

    test_data = {"name": "orders", "value": 2, "timestamp": datetime.now(),
                 "filters": {"status": ["Completed", "Test"]}}

    def setUp(self):
        self.client = HTTPClient(self.project, self.private_key, self.public_key,
                            host=self.host, port=self.port, prefix=self.prefix)


    def test_init(self):
        client = self.client


        self.assertEquals(client.get_url("incr"), "{host}:{port}{prefix}/api/v1/{project}/{action}".format(
            project=self.project,  host=self.host, port=self.port, prefix=self.prefix, action='incr'))

        self.assertEquals(client.headers['X-GottWall-Auth'],
                          "GottWall private_key={0}, public_key={1}".format(
                              self.private_key, self.public_key))

        data = self.test_data

        serialized_data = client.serialize(data['name'], data['timestamp'], data['value'], data['filters'])
        decoded_data = json.loads(serialized_data)
        self.assertEquals(client.dt_to_ts(data.get('timestamp')),
                          decoded_data['ts'])
        self.assertEquals(data['name'], decoded_data['n'])
        self.assertEquals(data['value'], decoded_data['v'])
        self.assertEquals(data['filters'], decoded_data['f'])


    @responses.activate
    def test_methods(self):
        client = self.client
        responses.add(responses.POST, client.get_url('incr'),
                  body='OK', status=200)
        responses.add(responses.POST, client.get_url('decr'),
                      body='OK', status=500)

        self.assertTrue(client.incr(**self.test_data))
        self.assertFalse(client.decr(**self.test_data))
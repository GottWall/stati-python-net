#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati.tests
~~~~~~~~~~~~~~~~

Unittests for stati

:copyright: (c) 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
import hashlib
import hmac
import json
from datetime import datetime

from .base import BaseTestCase
from stati_net import Client
from stati_net.client import utf8


private_key = "gottwall_privatekey"
public_key = "project_public_key"
project = "test_gottwall_project"



class ClientTestCase(BaseTestCase):

    test_data = {"name": "orders", "value": 2, "timestamp": datetime.now(),
                 "filters": {"status": ["Completed", "Test"]}}

    def setUp(self):
        self.client = Client(project, private_key, public_key)


    def test_default_methods(self):
        client = self.client

        client = Client(project, private_key, public_key)


        self.assertRaises(NotImplementedError, client.incr, **self.test_data)
        self.assertRaises(NotImplementedError, client.decr, **self.test_data)

        data = self.test_data
        serialized_data = client.serialize(data['name'], data['timestamp'], data['value'], data['filters'])

        decoded_data = json.loads(serialized_data)
        self.assertEqual(client.dt_to_ts(data.get('timestamp')),
                          decoded_data.get('ts'))

        self.assertEqual(data['name'], decoded_data['n'])
        self.assertEqual(data['value'], decoded_data['v'])
        self.assertEqual(data['filters'], decoded_data['f'])

    def test_sign(self):

        client = self.client

        ts = client.dt_to_ts(datetime.now())
        self.assertEquals(client.make_sign(ts), hmac.new(key=utf8(client._private_key),
                                                         msg=utf8(client.sign_msg(ts)),
                                                         digestmod=hashlib.md5).hexdigest())

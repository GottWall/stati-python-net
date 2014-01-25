#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati.tests
~~~~~~~~~~~~~~~~

Unittests for stati

:copyright: (c) 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
import json
from datetime import datetime
from .base import BaseTestCase

private_key = "gottwall_privatekey"
public_key = "project_public_key"
project = "test_gottwall_project"

from stati_net import Client


class ClientTestCase(BaseTestCase):

    test_data = {"name": "orders", "value": 2, "timestamp": datetime.now(),
                 "filters": {"status": ["Completed", "Test"]}}


    def test_default_methods(self):

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

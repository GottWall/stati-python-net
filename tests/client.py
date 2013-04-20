#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati.tests
~~~~~~~~~~~~~~~~

Unittests for stati

:copyright: (c) 2012 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
import json
from datetime import datetime
import os
from base import BaseTestCase
from stati_redis import Client, RedisClient
from redis import Redis

HOST = os.environ.get("STATI_REDIS_HOST", "10.8.9.8") # Redis in virtual machine

private_key = "gottwall_pricatekey"
public_key = "project_public_key"
project = "test_gottwall_project"



class ClientTestCase(BaseTestCase):

    def test_init(self):
        client = Client(project,
                        private_key,
                        public_key)


        self.assertRaises(NotImplementedError, client.incr,
                          name="orders", value=2, timestamp=datetime.now(),
                          filters={"current_status": "Completed"})
        ts = datetime.utcnow()
        data = dict(name="orders", value=2, timestamp=ts, filters={"current_status": "Completed"})

        serialized_data = client.serialize(data['name'], data['timestamp'], data['value'], data['filters'])

        decoded_data = json.loads(serialized_data)
        self.assertEquals(data.pop('timestamp').strftime("%Y-%m-%dT%H:%M:%S"),
                          decoded_data.pop('timestamp'))
        self.assertTrue("random" in decoded_data.keys())
        decoded_data.pop("random")
        self.assertEquals(decoded_data, data)


class RedisClientTestCase(BaseTestCase):

    def setUp(self):
        self.redis = Redis(host=HOST)
        self.redis.flushdb()

    def tearDown(self):
        self.redis.flushdb()

    def test_pubsub(self):

        check_pubsub = self.redis.pubsub()
        check_pubsub.psubscribe("gottwall:*")
        next(check_pubsub.listen())

        cli = RedisClient(
            private_key=private_key,
            public_key=public_key,
            project=project,
            host=HOST)
        ts = datetime.utcnow()

        self.assertEquals("gottwall:{0}:{1}:{2}".format(project, public_key, private_key), cli.channel)
        cli.incr(name="orders", value=2, timestamp=ts, filters={"current_status": "Completed"})

        message = next(check_pubsub.listen())

        self.assertEquals(message['channel'], 'gottwall:{0}:{1}:{2}'.format(project, public_key, private_key))

        notification_message = json.loads(message['data'])
        self.assertEquals(notification_message['type'], 'notification')

        data_dict = json.loads(self.redis.spop(cli.data_key))
        self.assertTrue(data_dict['name'], 'orders')
        self.assertTrue(data_dict['timestamp'], ts.strftime("%Y-%m-%dT%H:%M:%S"))
        self.assertTrue(data_dict['filters']['current_status'], 'Completed')

        self.assertEquals(self.redis.scard(cli.data_key), 0)

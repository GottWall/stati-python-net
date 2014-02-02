#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stati_net.example
~~~~~~~~~~~~~~~~~

HTTP client

:copyright: (c) 2012 - 2013 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-python-net
"""
import logging
from logging import getLogger

logger = getLogger('stati')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

from stati_net import HTTPClient

private_key = "secret_key"
public_key = "public_key"
project = "test_project"

host = "127.0.0.1"

cli = HTTPClient(
    private_key=private_key,
    public_key=public_key,
    project=project,
    host=host,
    port=8890,
    prefix="")

for x in xrange(100000):
    cli.incr(name="orders", value=2, filters={"current_status": "Completed"})

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stati_net.example
~~~~~~~~~~~~~~~~~

UDP client

:copyright: (c) 2012 - 2013 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-python-net
"""

from stati_net import UDPClient

private_key = "dwefwefwefwecwef"
public_key = "my_public_key"
project = "test_project"

host = "http://127.0.0.1:8890"

cli = UDPClient(
    private_key=private_key,
    public_key=public_key,
    project=project,
    host=host,
    prefix=None)

for x in xrange(10):
    cli.incr(name="orders", value=2, filters={"current_status": "Completed"})

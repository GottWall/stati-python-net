#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stati_http.example
~~~~~~~~~~~~~


:copyright: (c) 2012 - 2013 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-http-python
"""

from stati_http import HTTPClient

private_key = "gottwall_privatekey"
public_key = "project_public_key"
project = "test_gottwall_project"

host = "http://127.0.0.1/"

cli = HTTPClient(
    private_key=private_key,
    public_key=public_key,
    project=project, db=2,
    host=host,
    prefix=None)

cli.incr(metric="orders", value=2, filters={"current_status": "Completed"})

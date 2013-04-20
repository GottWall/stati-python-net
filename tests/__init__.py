#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati.tests
~~~~~~~~~~~

Unittests for stati

:copyright: (c) 2012 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

import unittest
from client import ClientTestCase, RedisClientTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RedisClientTestCase))
    suite.addTest(unittest.makeSuite(ClientTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="suite")

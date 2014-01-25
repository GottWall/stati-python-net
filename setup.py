#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati-python-net
~~~~~~~~~~~~~~~~~

Python client with  HTTP & UDP & TCP/IP transports for GottWall statistics aggregator

:copyright: (c) 2012 - 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/stati-python-net
"""


import sys
import os
from setuptools import  setup

try:
    readme_content = open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "README.rst")).read()
except Exception, e:
    print(e)
    readme_content = __doc__

VERSION = "0.0.1"


def run_tests():
    from tests import suite
    return suite()


install_require = ["requests==2.2.1"]

tests_require = ["mock==1.0.1",
                 "responses==0.2.0"] + install_require

setup(
    name="stati-net",
    version=VERSION,
    description="Python client with HTTP & UDP & TCP/IP transports for GottWall statistics aggregator",
    long_description=readme_content,
    author="Alex Lispython",
    author_email="alex@obout.ru",
    maintainer="Alexandr Lispython",
    maintainer_email="alex@obout.ru",
    url="https://github.com/GottWall/stati-python-net",
    packages=["stati_net"],
    install_requires=install_require,
    tests_require=tests_require,
    license="BSD",
    platforms = ['Linux', 'Mac'],
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries"
        ],
    test_suite = '__main__.run_tests')

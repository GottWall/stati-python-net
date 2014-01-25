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


import os
from setuptools import  setup

try:
    readme_content = open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "README.rst")).read()
except Exception as e:
    print(e)
    readme_content = __doc__

VERSION = "0.0.1"


def run_tests():
    from tests import suite
    return suite()


install_require = ["requests==2.2.1",
                   "six==1.5.2"]

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
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Monitoring"
        ],
    test_suite = '__main__.run_tests')

Welcome to stati-python-net's documentation!
============================================

stati-python-net is a python client with HTTP & UDP & TCP/IP  transports for `GottWall metrics aggregation platform <http://github.com/GottWall/GottWall>`_

.. image:: https://secure.travis-ci.org/GottWall/stati-python-net.png
	   :target: https://secure.travis-ci.org/GottWall/stati-python-net

INSTALLATION
------------

To use gottwall  use `pip` or `easy_install`:

``pip install stati-net``

or

``easy_install stati-net``


USAGE
-----


.. sourcecode:: python

   from stati_net import HTTPClient

   private_key = "gottwall_privatekey"
   public_key = "project_public_key"
   project = "test_gottwall_project"

   host = "http://127.0.0.1:8890"

   cli = HTTPClient(
       private_key=private_key,
       public_key=public_key,
       project=project,
       host=host,
       prefix=None)

   cli.incr(metric="orders", value=2, filters={"status": ["Completed", "Waiting"]})



CONTRIBUTE
----------

We need you help.

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
   There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the **develop** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published.

.. _`the repository`: https://github.com/GottWall/stati-python-net/

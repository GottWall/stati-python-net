Welcome to stati-http-python's documentation!
==============================================

stati-http is a python client with http transport for `GottWall metrics aggregation platform <http://github.com/GottWall/GottWall>`_

.. image:: https://secure.travis-ci.org/GottWall/stati-http-python.png
	   :target: https://secure.travis-ci.org/GottWall/stati-http-python

INSTALLATION
------------

To use gottwall  use `pip` or `easy_install`:

``pip install stati-http``

or

``easy_install stati-http``


USAGE
-----


.. sourcecode:: python

   from stati_http import HTTPClient

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

   cli.incr(metric="orders", value=2, filters={"current_status": "Completed"})




CONTRIBUTE
----------

Fork https://github.com/GottWall/stati-http-python/ , create commit and pull request.


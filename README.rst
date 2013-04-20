Welcome to stati-redis-python's documentation!
======================================

stati-redis is a python client with redis transport for `GottWall metrics aggregation platform <http://github.com/GottWall/GottWall>`_

.. image:: https://secure.travis-ci.org/GottWall/stati-redis-python.png
	   :target: https://secure.travis-ci.org/GottWall/stati-redis-python

INSTALLATION
------------

To use gottwall  use `pip` or `easy_install`:

``pip install stati-redis``

or

``easy_install stati-redis``


USAGE
-----


.. sourcecode:: python

   from stati_redis import RedisClient

   private_key = "gottwall_privatekey"
   public_key = "project_public_key"
   project = "test_gottwall_project"

   host = "10.8.9.8"

   cli = RedisClient(
       private_key=private_key,
       public_key=public_key,
       project=project, db=2,
       host=host)

   cli.incr(metric="orders", value=2, filters={"current_status": "Completed"})




CONTRIBUTE
----------

Fork https://github.com/GottWall/stati-redis-python/ , create commit and pull request.


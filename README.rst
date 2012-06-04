PyServe
=======

PyServe is the simple command interface for HTTP serving directories.

::
    
    $ python -m SimpleHTTPServer

VS

::

    $ serve


.. image:: example.png

.. contents::


Requirements
============
- python > 2.6
- Flask 0.8


Installation
============

Distribute_: ::

    $ easy_install PyServe

PIP_: ::

    $ pip install PyServe


Usage
=====
::

    $ serve --help
    usage: serve [-h] [-p PORT] [-s] [path]

    Serve current directory

    positional arguments:
    path                  Path to serve directory.

    optional arguments:
    -h, --help            show this help message and exit
    -p PORT, --port PORT  The port of the webserver.
    -s, --share           Make server available externally.


.. _Distribute: http://pypi.python.org/pypi/distribute
.. _PIP: http://pypi.python.org/pypi/pip

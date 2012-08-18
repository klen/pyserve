PyServe
=======

PyServe is the simple command interface for HTTP serving directories.

.. image:: https://secure.travis-ci.org/klen/pyserve.png?branch=develop
    :target: http://travis-ci.org/klen/pyserve
    :alt: Build Status

::
    
    # Python 2.*
    $ python -m SimpleHTTPServer

    # Python 3
    $ python -m http.server

VS

::

    # Python 2.*
    $ serve

    # Python 3
    $ serve


.. image:: pyserve/raw/master/example.png

.. contents::


Requirements
============
- python (2.6+ or 3.0+)


Installation
============

Distribute_: ::

    $ easy_install pyserve

PIP_: ::

    $ pip install pyserve


Usage
=====
::

    $ serve --help

    usage: serve [-h] [-p PORT] [-s] [-a] [path]

    Serve current directory

    positional arguments:
    path                  Path to serve directory.

    optional arguments:
    -h, --help            show this help message and exit
    -p PORT, --port PORT  The port of the webserver.
    -s, --share           Make server available externally.
    -a, --autoindex       Enable autoindex files.
    -d, --hidden          Hide system files


.. _Distribute: http://pypi.python.org/pypi/distribute
.. _PIP: http://pypi.python.org/pypi/pip

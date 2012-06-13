from argparse import ArgumentParser
from os import path as op

from .app import APP
from .bottle import run
from .core import Entry


MODULE_ROOT = op.abspath(op.dirname(__file__))


def serve(path, port=5000, share=False, autoindex=False):
    APP.config.root = Entry(path)
    APP.config.static = op.join(MODULE_ROOT, 'static')
    APP.config.port = port
    APP.config.host = '127.0.0.1' if not share else '0.0.0.0'
    APP.config.autoindex = autoindex
    run(APP, port=int(port), host=APP.config.host)


def main():
    parser = ArgumentParser(description='Serve current directory')
    parser.add_argument('path',
            default=op.curdir,
            nargs='?',
            help='Path to serve directory.')
    parser.add_argument('-p', '--port',
            default=5000,
            help='The port of the webserver.')
    parser.add_argument('-s', '--share',
            action='store_true',
            help='Make server available externally.')
    parser.add_argument('-a', '--autoindex',
            action='store_true',
            help='Enable autoindex files.')
    args = parser.parse_args()
    serve(args.path, port=args.port, share=args.share, autoindex=args.autoindex)

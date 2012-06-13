from argparse import ArgumentParser
from os import path as op

from .app import APP
from .bottle import run
from .core import Entry


MODULE_ROOT = op.abspath(op.dirname(__file__))


def serve(args):
    APP.config.root = Entry(args.path)
    APP.config.static = op.join(MODULE_ROOT, 'static')
    APP.config.port = args.port
    APP.config.host = '127.0.0.1' if not args.share else '0.0.0.0'
    APP.config.autoindex = args.autoindex
    APP.config.hidden = args.hidden
    run(APP, port=int(args.port), host=APP.config.host)


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
            action='store_false',
            help='Enable autoindex files.')
    parser.add_argument('-d', '--hidden',
            action='store_false',
            help='Hide system files.')
    args = parser.parse_args()
    serve(args)

from os import path as op

from argparse import ArgumentParser
from flask import Flask
from flaskext.autoindex import AutoIndex


def serve(path, port=5000, share=False):
    app = Flask(__name__)
    AutoIndex(app, browse_root=path)
    app.run(port=int(port), host='127.0.0.1' if not share else '0.0.0.0')


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
    args = parser.parse_args()
    serve(args.path, port=args.port, share=args.share)

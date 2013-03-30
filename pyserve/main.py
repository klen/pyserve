from argparse import ArgumentParser
from os import path as op

from .app import APP
from .bottle import run
from .core import Entry


MODULE_ROOT = op.abspath(op.dirname(__file__))


def setup(path='/', port=5000, share=False, autoindex=False, hidden=False):
    APP.config.root = Entry(path)
    APP.config.static = op.join(MODULE_ROOT, 'static')
    APP.config.port = port
    APP.config.host = '127.0.0.1' if not share else '0.0.0.0'
    APP.config.autoindex = autoindex
    APP.config.hidden = hidden


def main():
    import socket

    port = 80

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 80))
        s.shutdown(2)
    except socket.error:
        port = 5000

    parser = ArgumentParser(description='Serve current directory')
    parser.add_argument('path',
                        default=op.curdir,
                        nargs='?',
                        help='Path to serve directory.')
    parser.add_argument('-p', '--port',
                        default=port,
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

    setup(path=args.path, port=args.post, share=args.share,
          autoindex=args.autoindex, hidden=args.hidden)

    run(APP, port=int(APP.config.port), host=APP.config.host)


if __name__ == "__main__":
    main()

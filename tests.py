" Pyserve tests. "
from os import path as op

from unittest import TestCase
from webtest import TestApp

from pyserve.core import Entry, RootDirectory


class PyServeTest(TestCase):

    def test_test(self):
        root = op.join(op.dirname(__file__), 'tests')
        entry = Entry(root)
        self.assertTrue(isinstance(entry, RootDirectory))
        self.assertEqual(len(entry.entries), 2)

    def test_app(self):
        from pyserve.app import APP
        from pyserve.main import setup

        setup(path='pyserve')
        app = TestApp(APP)
        response = app.get('/')
        self.assertEqual(response.status_code, 200)

" Pyserve tests. "
from os import path as op

from unittest import TestCase

from pyserve.core import Entry, RootDirectory


class PyServeTest(TestCase):

    def test_test(self):
        root = op.join(op.dirname(__file__), 'tests')
        entry = Entry(root)
        self.assertTrue(isinstance(entry, RootDirectory))
        self.assertEqual(len(entry.entries), 2)

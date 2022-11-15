#!/usr/bin/env python

"""Tests for `pyluke` package."""


import unittest

from pyluke import array


class TestArray(unittest.TestCase):
    """Tests for `pyluke` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_popok(self):
        a = ["a", "b", "c"]
        b = ["c", "d", "e"]
        len_b = len(b)
        self.assertIsNotNone(array.pop_anyorNone(a, b))
        self.assertNotEqual(len(b), len_b)
    
    def test_popfromfirst(self):
        a = ["a", "b", "c"]
        b = []
        len_a = len(a)
        self.assertIsNotNone(array.pop_anyorNone(a, b))
        self.assertNotEqual(len(a), len_a)

    def test_popempty(self):
        a = []
        b = []
        self.assertIsNone(array.pop_anyorNone(a,b))
__author__ = 'wnzeng'

import unittest

import Identifier as id

class TestBackend(unittest.TestCase):

    def test_identify(self):

        self.assertEqual("A min", id.identify("x02210"))

        self.assertEqual("E dom7", id.identify("xx2434"))

        self.assertEqual("C Maj", id.identify("x32010"))

        self.assertEqual("C Maj7", id.identify("x32000"))

        self.assertEqual("A#/Bb min", id.identify("A# C# E#"))

        self.assertEqual("D Maj", id.identify("D F# A"))

        self.assertEqual("Unknown Chord", id.identify("x93010"))

        self.assertEqual("B dom7", id.identify("x21202"))

unittest.main()
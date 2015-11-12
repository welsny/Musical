__author__ = 'wnzeng'

import unittest

import Identifier as id

from Octave import *


class TestBackend(unittest.TestCase):

    def integration_tests(self):

        self.assertEqual("A min", id.identify("x02210"))

        self.assertEqual("E dom7", id.identify("xx2434"))

        self.assertEqual("C Maj", id.identify("x32010"))

        self.assertEqual("C Maj7", id.identify("x32000"))

        self.assertEqual("A#/Bb min", id.identify("A# C# E#"))

        self.assertEqual("D Maj", id.identify("D F# A"))

        self.assertEqual("Unknown Chord", id.identify("x93010"))

        self.assertEqual("B dom7", id.identify("x21202"))


class TestOctave(unittest.TestCase):

    def test_init(self):

        self.assertEqual("C Maj", str(Octave([0, 4, 7]).chord))

        self.assertEqual("A min", str(Octave([9, 4, 0]).chord))


if __name__ == "__main__":
    unittest.main()

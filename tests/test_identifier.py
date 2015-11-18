import unittest
from path import *
from identifier import *


class Test(unittest.TestCase):

    def test_identify(self):

        self.assertEqual("C Maj", identify("x32010"))

        self.assertEqual("A min", identify("x02210"))

        self.assertEqual("E dom7", identify("xx2434"))

        self.assertEqual("C Maj7", identify("x32000"))

        self.assertEqual("A#/Bb min", identify("A# C# E#"))

        self.assertEqual("D Maj", identify("D F# A"))

        self.assertEqual("Unknown Chord", identify("x93010"))

        self.assertEqual("B dom7", identify("x21202"))


if __name__ == "__main__":
    unittest.main()

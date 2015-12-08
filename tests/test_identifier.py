import unittest
from path import *
from identifier import *


class Test(unittest.TestCase):

    def test_guitar(self):

        self.assertEqual("C Maj", identify("x32010"))

        self.assertEqual("A min", identify("x02210"))

        self.assertEqual("E dom7", identify("xx2434"))

        self.assertEqual("C Maj7", identify("x32000"))

        self.assertEqual("Unknown Chord", identify("x93010"))

        self.assertEqual("B dom7", identify("x21202"))

    def test_piano(self):

        self.assertEqual("A#/Bb min", identify("A# C# E#"))

        self.assertEqual("D Maj", identify("D F# A"))

    def test_ukelele(self):

        self.assertEqual("C Maj7", identify("0002"))

        self.assertEqual("G min7", identify("0211"))

        self.assertEqual("G#/Ab Maj", identify("1343"))


if __name__ == "__main__":
    unittest.main()

from identifier import *
from octave import *
from chord import *
import unittest


class Test(unittest.TestCase):

    def test_integration(self):

        self.assertEqual("C Maj", identify("x32010"))

        self.assertEqual("A min", identify("x02210"))

        self.assertEqual("E dom7", identify("xx2434"))

        self.assertEqual("C Maj7", identify("x32000"))

        self.assertEqual("A#/Bb min", identify("A# C# E#"))

        self.assertEqual("D Maj", identify("D F# A"))

        self.assertEqual("Unknown Chord", identify("x93010"))

        self.assertEqual("B dom7", identify("x21202"))

    def test_init(self):

        self.assertEqual("C Maj", str(Octave([0, 4, 7]).chord))

        self.assertEqual("D Maj", str(Octave([2, 6, 9]).chord))

        self.assertEqual("A min", str(Octave([9, 4, 0]).chord))

    def test_chord(self):

        c = Note('C', 0)
        cmaj = Chord('Maj', [0, 4, 7], c)

        self.assertEqual(str(cmaj), str(Chord('Maj', [0, 4, 7]).with_root(c)))


if __name__ == "__main__":
    unittest.main()

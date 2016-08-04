#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from chord import *
from identifier import *
from octave import *


class TestChord(unittest.TestCase):

    def test_chord(self):

        c = Note('C', 0)
        cmaj = Chord('Maj', [0, 4, 7], c)

        self.assertEqual(cmaj, Chord('Maj', [0, 4, 7]).with_root(c))


class TestIdentifier(unittest.TestCase):

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


class Test(unittest.TestCase):

    def test_init(self):

        self.assertEqual("C Maj", str(Octave([0, 4, 7]).chord))

        self.assertEqual("D Maj", str(Octave([2, 6, 9]).chord))

        self.assertEqual("A min", str(Octave([9, 4, 0]).chord))


if __name__ == "__main__":
    unittest.main()


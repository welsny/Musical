import unittest
from chord import *


class Test(unittest.TestCase):

    def test_chord(self):

	    c = Note('C', 0)
	    cmaj = Chord('Maj', [0, 4, 7], c)

	    self.assertEqual(cmaj, Chord('Maj', [0, 4, 7]).with_root(c))


if __name__ == "__main__":
    unittest.main()

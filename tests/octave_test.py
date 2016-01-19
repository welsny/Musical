import unittest
from octave import *



class Test(unittest.TestCase):

    def test_init(self):

        self.assertEqual("C Maj", str(Octave([0, 4, 7]).chord))

        self.assertEqual("D Maj", str(Octave([2, 6, 9]).chord))

        self.assertEqual("A min", str(Octave([9, 4, 0]).chord))


if __name__ == "__main__":
    unittest.main()

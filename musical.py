import sys
from identifier import *

def identify_chord(argv):
        result = identify(''.join(argv[1:]))
	print('\n' + result + '\n')

if __name__ == "__main__":
	identify_chord(sys.argv)


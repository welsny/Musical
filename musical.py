import sys
from identifier import *

def identify_chord(argv):
	
	user_input = ''

	for i in argv[1:]:
		user_input += i

	result = identify(user_input)

	print('\n' + result + '\n')

if __name__ == "__main__":
	identify_chord(sys.argv)
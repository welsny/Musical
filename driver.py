__author__ = 'lola'

from Identifier import *

# A min
print (identify("x02210"))

# E Dom 7
print (identify("xx2434"))

# C Maj
print (identify("x32010"))

# C Maj 7
print (identify("x32000"))

# A# min
print (identify("A# C# E#"))

# F sus4
print (identify("D F# A"))

# Not an actual musical Chord:
print (identify("x93010"))

# B dom7
print (identify("x21202"))
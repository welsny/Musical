__author__ = 'lola'

from Identifier import *

amin = fromGuitar("x02210")

# A min
print (chord(fromGuitar("x02210")))

# E Dom 7
print (chord(fromGuitar("xx2434")))

# C Maj
print (chord(fromGuitar("x32010")))

# C Maj 7
print (chord(fromGuitar("x32000")))

# A# min
print (chord(fromString("A# C# E#")))

# F sus4
print (chord(fromString("D F# A")))

# Not an actual musical Chord:
print (chord(fromGuitar("x93010")))

# B dom7
print (chord(fromGuitar("x21202")))
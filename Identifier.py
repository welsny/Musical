__author__ = 'lola'

from Octave import *
from Chord import *

GUITAR = [4, 9, 2, 7, 11, 4]

# Translates an Octave into a String of notes.
def chord(myOctave):
    return str(myOctave.chord)

# Translates a String of notes into an Octave.
def _fromString(notes):

    indexes = []
    while notes: #is not empty

        for i in NOTES:
            if notes[0] == i.name:
                noteVal = i.value

                # Accidentals
                if len(notes) >= 2:
                    if notes[1] == '#':
                        noteVal += 1
                        notes = notes[1:]
                    elif notes[1] == 'b':
                        noteVal -= 1
                        notes = notes[1:]

        indexes.append(noteVal)

        notes = notes[1:]

    myOctave = Octave(indexes)

    return myOctave

# Translates a GuitarTab string to an Octave.
def _fromGuitar(tabString):

    indexes = []

    for i in range(6):
        if not tabString[i] == "x":
            noteIndex = (GUITAR[i] + int(tabString[i])) % 12
            indexes.append(noteIndex)

    return Octave(indexes)

def identify(user_input):
    try:
        return chord(_fromString(user_input))
    except:
        try:
            return chord(_fromGuitar(user_input))
        except:
            return "Illegal Input Detected"
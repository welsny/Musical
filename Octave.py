__author__ = 'lola'

from Chord import *

'''
Octave represents the active notes in an Octave as a list of Booleans.
Its constructor takes a list of indexes representing the numeric value of a set of notes.
'''
class Octave():
    def __init__(self, noteIndexes):
        self.activeNotes = []
        self.chord = None

        for i in range(12):
            self.activeNotes.append(False)
        for i in noteIndexes:
            self.activeNotes[i] = True

        keyCount = self.activeNotes.count(True)

        for offset in range(12):
            for c in CHORDS:
                if keyCount == c.count() and self.patternMatches(c.pattern):
                    c.setRoot = getNote(offset)
                    self.chord = c
                    break

            # If no chords match, rotates the list.
            self.activeNotes = self.activeNotes[1:] + self.activeNotes[:1]

            # Breaks when a chord is found.
            if (self.chord != None):
                break

        # If chord wasn't matched in above loop, sets chord as a Null Chord.
        if (self.chord == None):
            self.chord = UNKNOWN_CHORD

    def addNote(self, noteIndex):
        self.activeNotes[noteIndex] = True

    '''
    Takes a pattern and returns the matching chord if any.
    If found, sets self.rootNote to the root of the chord.

    PRE: The number of notes in self.chord and pattern are equal.
    '''
    def patternMatches(self, pattern):

        for i in pattern:
            if not self.activeNotes[i]:
                return False

        return True

    # Getter method for an Octave's chord.
    def getChord(self):
        return self.chord

    def toString(self):
        return self.chord.toString()
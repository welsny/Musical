__author__ = 'lola'

from Chord import *
from funcy.colls import *

'''
Octave represents the active notes in an Octave as a list of Booleans.
Its constructor takes a list of indexes representing the numeric value of a set of notes.
'''
class Octave():
    def __init__(self, noteIndexes):
        self.activeNotes = {}
        self.__chord = None
        self.keycount = 0

        for i in range(12):
            self.activeNotes[i] = False

        for i in noteIndexes:
            self.activeNotes[i] = True

        for key in self.activeNotes:
            if self.activeNotes[key]:
                self.keycount += 1

        for offset in range(12):
            for c in CHORDS:
                if self.keycount == c.count() and self.patternMatches(c.pattern):
                    root = getNote(offset)
                    c.setRoot(root)
                    self.__chord = c
                    break

            # If no chords match, rotate the list
            self.activeNotes = walk_keys(lambda key: 11 if key == 0 else key - 1, self.activeNotes)

            # Break when a chord is found
            if (self.__chord != None):
                break

        # If chord wasn't matched in above loop, sets chord as a Null Chord.
        if (self.__chord == None):
            self.__chord = UNKNOWN_CHORD

    @property
    def chord(self):
        '''Get the Chord object that this Octave represents'''
        return self.__chord

    def __str__(self):
        return str(self.activeNotes)

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

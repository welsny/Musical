from Chord import *
from funcy.colls import *


class Octave(object):
    """
    Octave organizes a list of notes into an abstract musical octave model.
    Its constructor takes a list of indexes representing the numeric value of a set of notes.
    """

    def __init__(self, notes_indexes):
        self.__active_notes = {}
        self.__chord = None
        self.__keycount = 0

        for i in range(12):
            self.__active_notes[i] = False

        for i in notes_indexes:
            self.__active_notes[i] = True

        for key in self.__active_notes:
            if self.__active_notes[key]:
                self.__keycount += 1

        self.__identify()

    @property
    def chord(self):
        return self.__chord

    def __str__(self):
        return str(self.__active_notes)

    def __identify(self):
        """
        Identifies the chord represented in the Octave. If the chord is unknown, sets self.__chord to UNKNOWN_CHORD.
        POST: self.__chord is not None
        """

        for offset in range(12):
            for c in CHORDS:
                if self.__keycount == c.count() and self.__pattern_matches(c.pattern):
                    root = get_note(offset)
                    c.setRoot(root)
                    self.__chord = c
                    break

            # If no chords match, rotate the list
            self.__active_notes = walk_keys(lambda key: 11 if key == 0 else key - 1, self.__active_notes)

            if self.__chord:
                break

        if not self.__chord:
            self.__chord = UNKNOWN_CHORD

    def __pattern_matches(self, pattern):
        """
        :return: 'True' iff the pattern matches the active notes in this Octave
        Precondition: the number of notes in pattern and active_notes are equal
        """

        for i in pattern:
            if not self.__active_notes[i]:
                return False

        return True

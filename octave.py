from chord import *
from funcy.colls import *


class Octave(object):
    """
    Octave organizes a list of notes into an abstract musical octave model.
    Its constructor takes a list of indexes representing the numeric value of a set of notes.
    """

    def __init__(self, notes_indexes):
        self._active_notes = {}
        self._chord = None
        self._keycount = 0

        for i in range(12):
            self._active_notes[i] = False

        for i in notes_indexes:
            self._active_notes[i] = True

        for key in self._active_notes:
            if self._active_notes[key]:
                self._keycount += 1

        self.__identify()

    @property
    def chord(self):
        return self._chord

    def __str__(self):
        return str(self._chord) if self._chord else str(self._active_notes)

    def __identify(self):
        """
        Identifies the chord represented in the Octave. If the chord is unknown, sets self.__chord to UNKNOWN_CHORD.
        POST: self.__chord is not None
        """

        for offset in range(12):
            if self._active_notes[0]:
                for c in CHORDS:
                    if self._keycount == c.count() and self.__pattern_matches(c.pattern):
                        root = get_note(offset)
                        self._chord = c.with_root(root)
                        break

            # If no chords match, rotate the list
            self._active_notes = walk_keys(lambda key: 11 if key == 0 else key - 1, self._active_notes)

            if self._chord:
                break

        if not self._chord:
            self._chord = UNKNOWN_CHORD

    def __pattern_matches(self, pattern):
        """
        :return: 'True' iff the pattern matches the active notes in this Octave
        Precondition: the number of notes in pattern and active_notes are equal
        """

        return all(self._active_notes[i] for i in pattern)


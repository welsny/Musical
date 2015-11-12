__author__ = 'lola'


class Chord(object):
    def __init__(self, type, pattern, root=None):
        self.type = type
        self.pattern = pattern
        self.root = root

    def setRoot(self, root):
        self.root = root

    def __str__(self):
        if self.root is None:
            return self.type

        return self.root.name + " " + self.type

    def count(self):
        return len(self.pattern)


class Note(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


def get_note(noteval):
    """:return: The Note the corresponds to the given note value modulo 12. """
    for n in NOTES:
        if noteval % 12 == n.value:
            return n

''' CONSTANTS: '''

NOTES = [Note("C", 0), Note("C#/Db", 1), Note("D", 2),
         Note("D#/Eb", 3), Note("E", 4), Note("F", 5),
         Note("F#/Gb", 6), Note("G", 7), Note("G#/Ab", 8),
         Note("A", 9), Note("A#/Bb", 10), Note("B", 11)]

# TODO: Add more (useful) chords?
CHORDS = [Chord("Maj", [0,4,7]), Chord("min", [0,3,7]),
          Chord("dim", [0,3,6]), Chord("aug", [0,4,8]),
          Chord("sus2",[0,2,7]), Chord("sus4", [0,5,7]),
          Chord("Maj7", [0,4,7,11]), Chord("min7", [0,3,7,10]),
          Chord("dom7", [0,4,7,10]), Chord("dim7", [0,3,6,9])]

# An unknown chord that is returned when a chord cannot be identified.
UNKNOWN_CHORD = Chord("Unknown Chord", None)
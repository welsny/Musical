__author__ = 'lola'


class Chord(object):
    def __init__(self, quality, pattern, root=None):
        self._quality = quality
        self._pattern = pattern
        self._root = root

    @property
    def pattern(self):
        return self._pattern

    @property
    def quality(self):
        return self._quality

    @property
    def root(self):
        return self._root

    def with_root(self, new_root):
        return Chord(self._quality, self._pattern, new_root)

    def __str__(self):
        if not self._root:
            return self._quality

        return '{0} {1}'.format(self.root, self.quality)

    def __eq__(self, other):
        return isinstance(other, Chord) and \
               self._quality == other.quality and \
               self._pattern == other.pattern and \
               self._root == other.root

    def count(self):
        return len(self._pattern)


class Note(object):
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Note) and \
               self._name == other.name and \
               self._value == other.value


def get_note(noteval):
    """:return: The Note corresponding to the input value modulo 12."""
    for n in NOTES:
        if noteval % 12 == n.value:
            return n

''' CONSTANTS: '''

NOTES = [Note("C", 0), Note("C#/Db", 1), Note("D", 2),
         Note("D#/Eb", 3), Note("E", 4), Note("F", 5),
         Note("F#/Gb", 6), Note("G", 7), Note("G#/Ab", 8),
         Note("A", 9), Note("A#/Bb", 10), Note("B", 11)]

# TODO: Add more (useful) chords?
CHORDS = [Chord("Maj", [0, 4, 7]), Chord("min", [0, 3, 7]),
          Chord("dim", [0, 3, 6]), Chord("aug", [0, 4, 8]),
          Chord("sus2", [0, 2, 7]), Chord("sus4", [0, 5, 7]),
          Chord("Maj7", [0, 4, 7, 11]), Chord("min7", [0, 3, 7, 10]),
          Chord("dom7", [0, 4, 7, 10]), Chord("dim7", [0, 3, 6, 9])]

# Flag object representing an unknown chord, to be returned when a sequence of notes cannot be identified.
UNKNOWN_CHORD = Chord("Unknown Chord", None)

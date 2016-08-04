from octave import *
from chord import *

GUITAR = [4, 9, 2, 7, 11, 4]
UKELELE = [7, 0, 4, 9]

def chord(octave):
    """
    :param: An Octave instance
    :return: A string detailing the Chord that the Octave represents
    """
    return str(octave.chord)

def _from_string(notes):
    """
    :param: A String of notes: i.e. capital letters from A to G inclusive, including accidentals '#' and 'b'
    :return: An Octave instance representation of the input String
    """

    piano = {}
    while notes:

        for i in NOTES:
            if notes[0] == i.name:
                note_index = i.value

                if len(notes) >= 2:
                    if notes[1] == '#':
                        note_index += 1
                        notes = notes[1:]
                    elif notes[1] == 'b':
                        note_index -= 1
                        notes = notes[1:]

        piano[note_index] = True

        notes = notes[1:]

    return Octave(piano.keys())

def _from_tab(tab_string, instrument):
    """
    :param: A tab string and the instrument that the tab is being played on.
            py(ex. 'x32010' and GUITAR, or '0002' and UKELELE)
    :return: An Octave instance representation of the input String
    """

    piano = {}

    for i, e in enumerate(instrument):
        if tab_string[i] != 'x':
            note_index = (e + int(tab_string[i])) % 12
            piano[note_index] = True

    return Octave(piano.keys())


def identify(user_input):
    try:
        return chord(_from_string(user_input))
    except:
        try:
            if len(user_input) == 6:
                return chord(_from_tab(user_input, GUITAR))
            return chord(_from_tab(user_input, UKELELE))
        except:
            return 'Invalid Input'


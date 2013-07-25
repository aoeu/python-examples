'''Simple program to show MIDI note number (key) transposition.'''
import midi_util
from midi_util import NoteTransposer
from pyportmidi import midi

if __name__ == '__main__':
    midi.init()

    TRANSPOSITION_MAP = {37: 47,
                         38: 48,
                         39: 49,
                         40: 50,
                         41: 51,
                         42: 52,
                         43: 53,
                         44: 54,
                         45: 55,
                         46: 56,
                         47: 57,
                         48: 58,
                         49: 59}

    nanopad_transposer = NoteTransposer("nanoPAD2 PAD", 
                                        "IAC Driver Bus 1",
                                        TRANSPOSITION_MAP)
    nanopad_transposer.run()
    midi.quit()

'''Simple program to pretty print the available MIDI devices available on the system.'''
from pyportmidi import midi
import midi_util
from pprint import pprint

if __name__ == '__main__':
    midi.init()
    pprint(midi_util.describe_devices(), indent=4)
    midi.quit()

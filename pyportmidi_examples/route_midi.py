import midi_util
from midi_util import MidiRouter
from pyportmidi import midi

if __name__ == '__main__':
    midi.init()
    router = MidiRouter("nanoPAD2 PAD", "IAC Driver Bus 1")
    router.run()
    midi.quit()

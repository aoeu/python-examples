'''Simple utility class for more simply interacting with pyportmidi.'''
from pyportmidi import midi
from time import sleep

# Because everyone loves magic numbers...
NOTE_ON  = 144
NOTE_OFF = 128 

def get_device_id(device_name, input_device=False, output_device=False):
    '''Gets a MIDI input or output device ID from the system.'''
    if input_device or output_device:
        offset = 2 if input_device else 3
    for i in range(midi.get_count()):
        info = midi.get_device_info(i)
        if info[1] == device_name:
            if input_device or output_device:
                if info[offset] == 1:
                    return i
            else:
                return i

def get_device(device_name, input_device=False, output_device=False):
    '''Gets a MIDI input or output device from the system by device name.'''
    device_id = get_device_id(device_name, 
                       input_device=input_device, 
                       output_device=output_device)
    if output_device:
        return midi.Output(device_id)
    return midi.Input(device_id)

def get_input_device(device_name):
    '''Gets a MIDI input device object from the system by name.'''
    device_id = get_device_id(device_name, input_device=True)
    return midi.Input(device_id)

def get_output_device(device_name):
    '''Gets a MIDI output device object from the system by name.'''
    device_id = get_device_id(device_name, output_device=True)
    return midi.Output(device_id)

def describe_devices():
    '''Describes names and status of all MIDI devices available on the system.'''
    keys='id,interface,device_name,is_input_device,is_output_device,is_opened'.split(',')
    devices_info = [list(midi.get_device_info(x)) for x in range(midi.get_count())]
    devices = []
    device_id = 0
    for info in devices_info:
        info.insert(0, device_id)
        device_id += 1
        devices.append(dict(zip(keys,info)))
    return devices

class MidiRouter(object):
    '''Object for simply routing MIDI from one device to another.'''
    def __init__(self, from_device_name, to_device_name):
        self.from_device_name = from_device_name
        self.to_device_name = to_device_name
        self.input_device = get_input_device(from_device_name)
        self.output_device = get_output_device(to_device_name)
        self.midi_events = []

    def run(self):
        '''Runs the MidiRouter in an infinite loop.'''
        while True:
            if self.input_device.poll():
                self.midi_events = self.input_device.read(1)
                self.modify_data()
                self.output_device.write(self.midi_events)
            sleep(0.05)

    def modify_data(self):
        '''Meant to be overloaded in subclasses.'''
        pass

class NoteTransposer(MidiRouter):
    '''Object for transposing MIDI note data pitches and routing them.'''
    def __init__(self, from_device_name, to_device_name, transpose_map):
        super(NoteTransposer, self).__init__(from_device_name, to_device_name)
        self.transpose_map = transpose_map
    
    def modify_data(self):
        modified_events = []
        for event in self.midi_events: 
            msg_type = event[0][0]
            if msg_type is NOTE_ON or msg_type is NOTE_OFF:
                note_num = event[0][1]
                if note_num in self.transpose_map.keys():
                    event[0][1] = self.transpose_map[note_num] 
        print self.midi_events

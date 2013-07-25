pyportmidi examples
==================

###ab out###

These are some very quick sketches to explore the usability of the portmidi bindings in python (pyportmidi). 

It is here for example purposes since pyportmidi came with less examples than I wanted.

I did not continue exploring pyportmidi and instead wrote my own MIDI libraries in Go. 

###in stall at ion### 

Getting the necessary packages in place will probably be a pain. 

If on a mac, do something like: 
	% brew install portmidi
	% sudo pip install pyPortMidi

Fortunately, portmidi is in homebrew now, so installation is easier than it was years ago.
Try installing portmidi, then compile `print_devices.c` to ensure it works on your system.

`pyPortMidi` likely will have problems. It requires pyrex to be installed, portmidi, and seems to not work correctly in pip.

Hints:
-- `pip install pyPortMidi` fails, but `pip search pyPortMidi` works.
-- It works on my system, maybe because I downloaded the pyportmidi source and installed it.
-- http://alumni.media.mit.edu/~harrison/pyportmidi.html
-- gl;hf

###us age###

Just run the `print_devices.py` to see if things are working properly.

`import midi_util` to use stuff in taht file.

I highly recommend setting up some IAC buses in Mac OS X's MIDI settings.
This will enable you to route pieces of software or hardware to eachother through the IAC buses.

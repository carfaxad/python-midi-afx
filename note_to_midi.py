# %%

import rtmidi
import time

from mido import open_output
from mido.messages import Message
from mido.ports import BaseOutput
from scales import ScaleModes


# TODO add support for bemol
class NoteToMidi(ScaleModes):

    def __init__(self):
        super().__init__()
        self.mapping = self._build_mapping()

    def _build_mapping(self):
        mapping = {}
        octave = -2
        scale = self.scales['C']
        for i in range(128):
            mod = i % len(scale)
            if mod == 0:
                octave += 1
            mapping[f'{scale[i - ((octave + 1) * len(scale))]}{octave}'] = i

        return mapping

class SoundNotes(NoteToMidi):

    def __init__(self):
        super().__init__()
        self.m = self.mapping
        self.midiout = rtmidi.MidiOut()
        self.port = open_output(self.midiout.get_ports()[0])

    def close(self):
        if self.port and not self.port.closed:
            self.port.close()

    def play(self, notes, velocity=64, lapse=0):
        print(notes)
        for note in notes:
            self.port.send(Message('note_on', note=self.m[note], time=lapse, velocity=64))
            if lapse:
                time.sleep(lapse)

# %%
from scales import ScaleModes

sm = ScaleModes()
sn = SoundNotes()
mode1 = sm.create_mode('jonico', 'F', 4)
mode2 = sm.create_mode('lidio', 'F', 4)



# %%

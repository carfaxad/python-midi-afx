import rtmidi
import time

from mido import open_output
from mido.messages import Message
from mido.ports import BaseOutput
from scales import ScaleModes


class MappingMixin(ScaleModes):

    def __init__(self):
        super().__init__()
        self.mapping_sharp = self._build_mapping(self.scales['C'])

        self.bemol = True
        self.mapping_bemol = self._build_mapping(self._build_scales()['C'])

    def _build_mapping(self, scale):
        mapping = {}
        octave = -2
        for i in range(128):
            mod = i % len(scale)
            if mod == 0:
                octave += 1
            mapping[f'{scale[i - ((octave + 1) * len(scale))]}{octave}'] = i

        return mapping

class PlayNotes(MappingMixin):
    """ Play a list of notes """
    def __init__(self):
        super().__init__()
        self.midiout = rtmidi.MidiOut()
        self.port = open_output(self.midiout.get_ports()[0])

    def play(self, notes, velocity=64, lapse=0):
        """ Play an array of notes. Support sharp and bemol notation

            Parameters:
                notes (List):       ['C', 'A', ...]
                velocity (int):     Volume (see `mido` specification)
                lapse (int):        time between each note in array

            Returns:
                Sound (Midi Output)

            Example:
                ```python
                p = PlayNotes()
                p.play(p.create_mode('lidio', 'A', 3), lapse=0.5)
                ```
        """
        for note in notes:
            midinote = self.mapping_bemol[note] if 'b' in note else self.mapping_sharp[note]
            print(note, midinote)
            self.port.send(Message('note_on', note=midinote, time=lapse, velocity=64))
            if lapse:
                time.sleep(lapse)

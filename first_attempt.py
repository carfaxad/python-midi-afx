# %%
import mido
import time
import rtmidi

# %%
midiout = rtmidi.MidiOut()
port = mido.open_output(midiout.get_ports()[0])

# %%
for note in range(40, 80, 1):
    port.send(mido.Message('note_on', note=note, time=100))
    if note % 2 == 0:
        port.send(mido.Message('note_on', note=note + 4, time=100))
    if note % 3 == 0:
        port.send(mido.Message('note_on', note=note+7, time=100))
    time.sleep(0.2)
    # port.send(mido.Message('note_off'))
    # time.sleep(0.1)

# # %%
# from mido import Message, MidiFile, MidiTrack


# mid = MidiFile()
# track = MidiTrack()
# mid.tracks.append(track)

# track.append(Message('program_change', program=12, time=0))
# track.append(Message('note_on', note=64, velocity=64, time=100))
# track.append(Message('note_off', note=64, velocity=127, time=100))
# track.append(Message('note_on', note=64, velocity=64, time=100))
# track.append(Message('note_off', note=64, velocity=127, time=100))
# track.append(Message('note_on', note=64, velocity=64, time=100))
# track.append(Message('note_off', note=64, velocity=127, time=100))
# track.append(Message('note_on', note=64, velocity=64, time=100))
# track.append(Message('note_off', note=64, velocity=127, time=100))

# mid.save('new_song.mid')


# %%
import json
from collections import defaultdict

rules = [1, 1, 0, 1, 1, 1, 0]
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
base_scale_rules = list(zip(rules, notes))

# %%
scales = defaultdict(list)
actual_scale_rules = []
for i, key_note in enumerate(notes):
    actual_scale_rules = base_scale_rules[i:] + base_scale_rules[:i]

    for rule, note in actual_scale_rules:
        scales[key_note] += [note, note + '#'] if rule else [note]

# %%
mode_name = [
    'jonico',        # major mode/natural major
    'dorico',
    'frigio',
    'lidio',
    'mixolidio',
    'eolico',        # minor mode/natural minor
    'locrio'
]
modes = {mode_name[i]: rules[i:] + rules[:i] for i in range(7)}

def create_mode(mode, note):
    scale = scales[note]

    def _bemol(r):
        return [scale[scale.index(note) + 1] + 'b' if '#' in note else note for note in r]

    result = [scale[0]]
    position = 0
    for rule in modes[mode]:
        try:
            # print(rule, position)
            skip = 2 if rule else 1
            position += skip
            result.append(scale[position])
        except:
            continue

    print(modes[mode])
    return result if mode in ['jonico', 'lidio'] else _bemol(result)

# %%

create_mode('mixolidio', 'G')

# %%

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

# # %%

# notes = {
#     0: 'C',
#     1: 'D',
#     2: 'E',
#     3: 'F',
#     4: 'G',
#     5: 'A',
#     6: 'B',
# }

# notes_rules = {notes[i]: base[i:] + base[:i] for i in range(len(base))}
# print(notes_rules)

# # %%
# from collections import defaultdict
# rules = [1, 1, 0, 1, 1, 1, 0]
# notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
# nr = list(zip(rules, notes))
# print(nr)

# # %%
# for i, n, in nr:
    

# # %%
# scales_base = {note: base[i:] + base[:i] for i, note in enumerate(notes)}

# scales = defaultdict(list)
# for note, rules in scales_base.items():
#     n =
#     for rule in rules:
#         scales[note] += [notes[i], notes[i] + '#'] if rule else [notes[i]]

# print(scales)

# # for note, rules in notes_rules.items():
# #     for i, rule in enumerate(rules):
# #         scales[note] += [notes[i], notes[i] + '#'] if rule else [notes[i]]
# # print(scales)

# # %%
# octave = []
# for i, note in notes.items():
#     octave += [note, note + '#'] if base[i] else [note]
# print(octave)

# # %%

# scales = {notes[i]: octave[i:] + octave[:i] for i in range(len(notes))}
# print(scales)

# # %%
# mode_name = {
#     0: 'jonico',        # major mode/natural major
#     1: 'dorico',
#     2: 'frigio',
#     3: 'lidio',
#     4: 'mixolidio',
#     5: 'eolico',        # minor mode/natural minor
#     6: 'locrio'
# }
# modes_b = {mode_name[i]: base[i:] + base[:i] for i in range(len(base))}

# # %%
# for

# # %%
# base_note = '12'  # C0
# octave = ['C', 'C#', 'R', R]
# for i in range(base_note, 168, octave):

#     if i % octave_len == 0:
#         notes.update({current_note: i})
#     current_octave += 1
# print(notes)

# # %%


# # %%


# %%

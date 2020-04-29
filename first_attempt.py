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
from scales import ScaleModes
s = ScaleModes()
s.create_mode('dorico', 'C')

# %%

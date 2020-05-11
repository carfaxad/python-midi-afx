from time import sleep
from scales import MusicalBases
from note_to_midi import PlayNotes

p = PlayNotes()
mb = MusicalBases()

p.play(mb.create_chord(mb.create_mode('eolico', 'F'), num_notes=4, octave=3), lapse=0.4)

p.play(mb.create_chord(mb.create_mode('eolico', 'A'), num_notes=3, octave=3), lapse=0.4)
p.play(mb.create_chord(mb.create_mode('eolico', 'A'), num_notes=4, octave=3), duration=0.4)

p.play(mb.create_chord(mb.create_mode('eolico', 'C'), num_notes=4, octave=4), lapse=0.4)

p.play(mb.create_chord(mb.create_mode('eolico', 'D'), num_notes=3, octave=4), lapse=0.4)
p.play(mb.create_chord(mb.create_mode('eolico', 'D'), num_notes=4, octave=4), duration=0.4)

p.play(mb.create_chord(mb.create_mode('eolico', 'F'), num_notes=4, octave=3), duration=1.6)
p.play(mb.create_chord(mb.create_mode('eolico', 'A'), num_notes=4, octave=3), duration=1.6)
p.play(mb.create_chord(mb.create_mode('eolico', 'C'), num_notes=4, octave=4), duration=1.6)
p.play(mb.create_chord(mb.create_mode('eolico', 'D'), num_notes=4, octave=4), duration=1.6)

p.play(mb.create_chord(mb.create_mode('locrio', 'F'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('locrio', 'F'), num_notes=3, octave=3), lapse=0.266)
p.play(mb.create_chord(mb.create_mode('locrio', 'C'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('locrio', 'C'), num_notes=3, octave=4), lapse=0.266)
p.play(mb.create_chord(mb.create_mode('locrio', 'D'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('locrio', 'D'), num_notes=3, octave=4), lapse=0.266)
p.play(mb.create_chord(mb.create_mode('locrio', 'A'), num_notes=4, octave=5), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('locrio', 'A'), num_notes=3, octave=5), lapse=0.266)

p.play(mb.create_chord(mb.create_mode('jonico', 'F'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'A'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'C'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'D'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'F'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'A'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'C'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'D'), num_notes=4, octave=4), lapse=0.2)

mb.fix_octaves = False
p.play(mb.create_chord(mb.create_mode('jonico', 'F'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'A'), num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'C'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'D'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('dorico', 'F'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('dorico', 'A'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'C'), num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('mixolidio', 'D'), num_notes=4, octave=4), lapse=0.2)

mb.fix_octaves = True
p.play(mb.create_chord(mb.create_mode('jonico', 'F'), mode='augmented', num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'F'), mode='major', num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'F'), mode='minor', num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'F'), mode='diminished', num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'C'), mode='diminished', num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'C'), mode='minor', num_notes=4, octave=3), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'A'), mode='augmented', num_notes=4, octave=4), lapse=0.2)
p.play(mb.create_chord(mb.create_mode('jonico', 'D'), mode='major', num_notes=4, octave=4), lapse=0.2, duration=3.2)


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
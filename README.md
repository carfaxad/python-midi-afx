# python-midi-afx
Python MIDI utils for music lessons

Consider using a virtual env _midi_ and set `settings.json`

- [Usage](#Usage)
  * [Create modes](#.scales.MusicalBases.create_mode)
  * [Create scales](#.scales.MusicalBases.create_chord)
  * [Play notes](#.note_to_midi.PlayNotes.play)
- [Final example](#.finalexample)

<a name=".Usage"></a>
# Usage

<a name=".scales"></a>
## scales.py

<a name=".scales.MusicalBases"></a>
### `MusicalBases` Class

```python
mb = MusicalBases(bemol=False)
```

Builds scales, scale modes, chords, and more

**Arguments**:

- `bemol` _bool_ - Default False for scales in `#` way, True for scales in `b` way
- `fix_octaves` _bool_ - Preserve natural regular scales order if True.

<a name=".scales.MusicalBases.create_mode"></a>
### `create\_mode` method

```python
create_mode(mode, note, octave=None)
```

Create mode with `b` if scale is minor else with `#`

**Arguments**:

- `mode` _str_ - jonico, dorico, frigio, lidio, mixolidio, eolico, locrio
- `note` _str_ - C, D, E, F, G, A, B
- `octave` _int_ - Octave in keyboard way


**Returns**:

- `List` - octave in specified mode


**Examples**:

  ```python
  mb = MusicalBases(bemol=True)
  mb.create_mode('dorico', 'C', 3)
  # returns: ['C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 'Bb3', 'C4']
  ```

<a name=".scales.MusicalBases.create_chord"></a>
### `create\_chord` method

```python
create_chord(scale, mode='major', octave=4, num_notes=3)
```

Create chord with given scale

**Arguments**:

- `scale` _List_ - ['C', 'E', ...]
- `mode` _str='major'_ - major, minor, diminished, augmented
- `octave` _int=4_ - Octave in keyboard way
- `num_notes` _int=3_ - Number of containing notes


**Returns**:

- `List` - Chord


**Examples**:

  ```python
  mb = MusicalBases()
  mb.create_chord(mb.scales['B'], num_notes=4, octave=3)
  # returns: ['B3', 'D#3', 'F#3', 'A3']
  ```


<a name=".note_to_midi"></a>
## note_to_midi.py

<a name=".note_to_midi.PlayNotes"></a>
### `PlayNotes` Class

```python
p = PlayNotes()
```

Play a list of notes

<a name=".note_to_midi.PlayNotes.play"></a>
### `play` method

```python
play(notes, velocity=64, lapse=0)
```

Play an array of notes. Support sharp and bemol notation

**Arguments**:

- `notes` _List_ - ['C', 'A', ...]
- `velocity` _int_ - Volume (see `mido` specification)
- `lapse` _int_ - Sequential: Time between each note in array to create sequential sound
- `duration` _int_ - Chords: Time at the end of sounding all notes in the array to create chord like sound


**Returns**:

  Sound (Midi Output)


**Examples**:

  ```python
  p = PlayNotes()
  p.play(p.create_mode('lidio', 'A', 3), lapse=0.5)
  ```

<a name=".finalexample"></a>
# Final example

```python
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

```

# Thanks to
This README.md was partially created with https://github.com/NiklasRosenstein/pydoc-markdown/

Usage:
```
pydoc-markdown -m [YOUR CLASS] -I .
```
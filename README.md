# MIDI
MIDI tests for music lessons

Consider using a virtual env _midi_ and set `settings.json`

# Usage
<a name=".scales"></a>
## scales

<a name=".scales.ScaleModes"></a>
### ScaleModes

```python
sm = ScaleModes(bemol=False)
```

Builds scales and scale modes

**Arguments**:

- `bemol` _bool_ - Default False for scales in `#` way, True for scales in `b` way

<a name=".scales.ScaleModes.create_mode"></a>
### create\_mode

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
  sm = ScaleModes(bemol=True)
  sm.create_mode('dorico', 'C', 3)
  # returns: ['C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 'Bb3', 'C4']
  ```

<a name=".note_to_midi"></a>
## note\_to\_midi

<a name=".note_to_midi.SoundNotes"></a>
### SoundNotes

```python
sn = SoundNotes()
```

Play a list of notes

<a name=".note_to_midi.SoundNotes.play"></a>
#### play

```python
play(notes, velocity=64, lapse=0)
```

Play an array of notes. Support sharp and bemol notation

**Arguments**:

- `notes` _List_ - ['C', 'A', ...]
- `velocity` _int_ - Volume (see `mido` specification)
- `lapse` _int_ - time between each note in array


**Returns**:

  Sound (Midi Output)


**Examples**:

  ```python
  sn = SoundNotes()
  sn.play(sn.create_mode('lidio', 'A', 3), lapse=0.5)
  ```

# Thanks to
This README.md was partially created with https://github.com/NiklasRosenstein/pydoc-markdown/

Usage:
```
pydoc-markdown -m [YOUR CLASS] -I .
```
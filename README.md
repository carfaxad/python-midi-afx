# MIDI
MIDI tests for music lessons

# Virtual env
Consider using a virtual env _midi_ and set `settings.json`

# Usage
<a name=".scales"></a>
## scales.py

<a name=".scales.ScaleModes.__init__"></a>
### \_\_init\_\_

```python
 | __init__(bemol=False)
```

Builds scales and modes

**Arguments**:

- `bemol` _bool_ - Default False for scales in `#` way, True for scales in `b` way

<a name=".scales.ScaleModes.create_mode"></a>
### create\_mode

```python
 | create_mode(mode, note, octave=None)
```

Create mode with `b` if scale is minor else with `#`

**Arguments**:

- `mode` _str_ - jonico, dorico, frigio, lidio, mixolidio, eolico, locrio
- `note` _str_ - C, D, E, F, G, A, B
- `octave` _int_ - Octave in keyboard way


**Returns**:

- `List` - octave in specified mode

# Thanks to
This README.md was partially created with https://github.com/NiklasRosenstein/pydoc-markdown/

Usage:
```
pydoc-markdown -m [YOUR CLASS] -I .
```
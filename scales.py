import json
from collections import defaultdict


class ScaleModes:

    def __init__(self, bemol=False):
        """ Builds scales and scale modes

        Parameters:
        bemol (bool): Default False for scales in `#` way, True for scales in `b` way
        """
        self.bemol = bemol
        self.notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.rules = [1, 1, 0, 1, 1, 1, 0]
        self.base_rules = list(zip(self.rules, self.notes))
        self.modes = self._build_modes()
        self.scales = self._build_scales()

    def _build_scales(self):
        """ Private method: Build natural scales for each note """
        scales = defaultdict(list)
        actual = []
        for i, key_note in enumerate(self.notes):
            actual = self.base_rules[i:] + self.base_rules[:i]

            for rule, note in actual:
                if self.bemol:
                    try:
                        scales[key_note] += [note, actual[actual.index((rule, note)) + 1][1] + 'b'] if rule else [note]
                    except:
                        scales[key_note] += [note, actual[0][1] + 'b'] if rule else [note]
                else:
                    scales[key_note] += [note, note + '#'] if rule else [note]
        return scales

    def _build_modes(self):
        """ Private method: Create rules for each mode """
        mode_name = [
            'jonico',        # major mode/natural major
            'dorico',
            'frigio',
            'lidio',
            'mixolidio',
            'eolico',        # minor mode/natural minor
            'locrio'
        ]
        return {mode_name[i]: self.rules[i:] + self.rules[:i] for i in range(7)}


    def create_mode(self, mode, note, octave=None):
        """ Create mode with `b` if scale is minor else with `#`

            Parameters:
                mode (str):     jonico, dorico, frigio, lidio, mixolidio, eolico, locrio
                note (str):     C, D, E, F, G, A, B
                octave (int):   Octave in keyboard way

            Returns:
                List: octave in specified mode

            Example:
                ```python
                sm = ScaleModes(bemol=True)
                sm.create_mode('dorico', 'C', 3)
                # returns: ['C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 'Bb3', 'C4']
                ```

        """
        scale = self.scales[note]

        def _bemol(r):
            return [scale[scale.index(note) + 1] + 'b' if '#' in note else note for note in r]

        result = [scale[0]]
        position = 0
        for rule in self.modes[mode]:
            try:
                skip = 2 if rule else 1
                position += skip
                result.append(scale[position])
            except:
                continue

        print(self.modes[mode])
        actual_mode = result if mode in ['jonico', 'lidio'] else _bemol(result)
        return actual_mode + [note] if not octave else list(map(lambda x: f'{x}{octave}', actual_mode)) + [f'{note}{octave + 1}']

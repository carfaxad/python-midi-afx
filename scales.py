import json
from collections import defaultdict


class ScaleModes:

    def __init__(self):
        self.rules = [1, 1, 0, 1, 1, 1, 0]
        self.notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.base_scale_rules = list(zip(self.rules, self.notes))
        self.scales = self._build_scales()
        self.modes = self._build_modes()

    def _build_scales(self):
        scales = defaultdict(list)
        actual_scale_rules = []
        for i, key_note in enumerate(self.notes):
            actual_scale_rules = self.base_scale_rules[i:] + self.base_scale_rules[:i]

            for rule, note in actual_scale_rules:
                scales[key_note] += [note, note + '#'] if rule else [note]
        return scales

    def _build_modes(self):
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


    # TODO add plus one after B in each scale
    def create_mode(self, mode, note, octave=None):
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

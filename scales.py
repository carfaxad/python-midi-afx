import json
from collections import defaultdict
from copy import deepcopy

class MusicalBases:
    """ Builds scales, scale modes, chords, and more

    Parameters:
    bemol (bool): Default False for scales in `#` way, True for scales in `b` way
    fix_octaves (bool): Preserve natural regular scales order if True.
    """

    def __init__(self):
        self.bemol = False
        self.fix_octaves = True

        self.notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.rules = [1, 1, 0, 1, 1, 1, 0]  # 1 = Tone, 0 = Semi
        self.base_rules = list(zip(self.rules, self.notes))

        self.modes = self._build_modes()
        self.scales = self._build_scales()

    def _validate_note(self, note):
        assert note in self.notes, 'Value of note does not exist'

    def _set_octaves(self, m, octave):
        if self.fix_octaves:
            octave_m = []
            for i, n in enumerate(m):
                octave_m.append(f'{n}{octave}')
                if ord(n[0]) == ord('B') and ord((m + m[:-1])[i + 1][0]) != ord('B'):
                    octave += 1
                # TODO
                # elif ord(n[0]) > ord((m + m[:-1])[i + 1][0]):
                #     octave += 1
                else:
                    continue
            return octave_m
        else:
            return list(map(lambda x: f'{x}{octave}', m))

    def _build_modes(self):
        """ Build modes

            Parameters:
                None

            Returns:
                Dict: Mode as key and a List of 7 notes of the scale mode
        """
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

    def _build_scales(self):
        """ Build natural scales for each note

            Parameters:
                None

            Returns:
                Dict: base note as key and a List of 12 notes of the scale
        """
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
                mb = MusicalBases(bemol=True)
                mb.create_mode('dorico', 'C', 3)
                # returns: ['C3', 'D3', 'Eb3', 'F3', 'G3', 'A3', 'Bb3', 'C4']
                ```

        """
        self._validate_note(note)
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
        return actual_mode if not octave else self._set_octaves(actual_mode, octave)

    def create_chord(self, scale, mode='major', octave=4, num_notes=3):
        """ Create chord with given scale

            Parameters:
                scale (List):               ['C', 'E', ...]
                mode (str='major'):         major, minor, diminished, augmented
                octave (int=4):             Octave in keyboard way
                num_notes (int=3):          Number of containing notes

            Returns:
                List: Chord

            Example:
                ```python
                mb = MusicalBases()
                mb.create_chord(mb.scales['B'], num_notes=4, octave=3)
                # returns: ['B3', 'D#3', 'F#3', 'A3']
                ```

        """
        
        assert num_notes <= 7, 'Scales bigger than thirteenth are not supported yet'

        names_by_position = [
            'first',
            'third',
            'fifth',
            'seventh',
            'nineth',
            'eleventh',
            'thirteenth',
        ]
        rules = {
            'major': [ # Fundamental
                (4, 'third'),
                (3, 'third minor'),
                (3, 'third minor'),
                (4, 'third'),
                (3, 'third minor'),
                (4, 'third')
            ],
            'minor': [
                (3, 'third minor'),
                (4, 'third'),
                (3, 'third minor'),
                (4, 'third'),
                (3, 'third minor'),
                (4, 'third')
            ],
            'diminished': [
                (3, 'third minor'),
                (3, 'third minor'),
                (4, 'third'),
                (4, 'third'),
                (3, 'third minor'),
                (4, 'third')
            ],
            'augmented': [
                (4, 'third'),
                (4, 'third'),
                (2, 'third minor'),
                (4, 'third'),
                (3, 'third minor'),
                (4, 'third')
            ]
        }

        i = 0
        j = 1
        dcs = self._set_octaves(scale + scale, octave)
        actual = [dcs[i]]
        study = [(dcs[i], 'fundamental', names_by_position[0])]
        for step, tag in rules[mode][:num_notes - 1]:
            i += step
            study.append((dcs[i], tag, names_by_position[j]))
            actual.append(dcs[i])
            j += 1
        print(dcs)
        print(mode)
        print(study)
        return actual

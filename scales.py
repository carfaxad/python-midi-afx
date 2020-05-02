import json
from collections import defaultdict
from copy import deepcopy

class MusicalBases:
    """ Builds scales, scale modes, chords, and more

    Parameters:
    bemol (bool): Default False for scales in `#` way, True for scales in `b` way
    """

    def __init__(self, bemol=False):
        self.bemol = bemol

        self.notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.rules = [1, 1, 0, 1, 1, 1, 0]  # 1 = Tone, 0 = Semi
        self.base_rules = list(zip(self.rules, self.notes))

        self.modes = self._build_modes()
        self.scales = self._build_scales()

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
                sm = MusicalBases(bemol=True)
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
        # TODO: Handle incremental octaves
        actual_mode = result if mode in ['jonico', 'lidio'] else _bemol(result)
        return actual_mode if not octave else list(map(lambda x: f'{x}{octave}', actual_mode))

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
        # TODO: Handle incremental octaves
        dcs = list(map(lambda x: x + f'{octave}', scale)) + \
              list(map(lambda x: x + f'{octave + 1}', scale))
        actual = [dcs[i]]
        study = [(dcs[i], 'fundamental', names_by_position[0])]
        for step, tag in rules[mode][:num_notes - 1]:
            i += step
            study.append((dcs[i], tag, names_by_position[j]))
            actual.append(dcs[i])
            j += 1
        print(study)
        return actual

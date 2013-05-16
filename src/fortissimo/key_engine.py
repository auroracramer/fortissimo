import sys
NAMED_SCALES = {
  'major': (2, 2, 1, 2, 2, 2, 1),
  'minor': (2, 1, 2, 2, 1, 2, 2),
  'melodicminor': (2, 1, 2, 2, 2, 2, 1),
  'harmonicminor': (2, 1, 2, 2, 1, 3, 1),
  'pentatonicmajor': (2, 2, 3, 2, 3),
  'bluesmajor': (3, 2, 1, 1, 2, 3),
  'pentatonicminor': (3, 2, 2, 3, 2),
  'bluesminor': (3, 2, 1, 1, 3, 2),
  'augmented': (3, 1, 3, 1, 3, 1),
  'diminished': (2, 1, 2, 1, 2, 1, 2, 1),
  'chromatic': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
  'wholehalf': (2, 1, 2, 1, 2, 1, 2, 1),
  'halfwhole': (1, 2, 1, 2, 1, 2, 1, 2),
  'wholetone': (2, 2, 2, 2, 2, 2),
  'augmentedfifth': (2, 2, 1, 2, 1, 1, 2, 1),
  'japanese': (1, 4, 2, 1, 4),
  'oriental': (1, 3, 1, 1, 3, 1, 2),
  'ionian': (2, 2, 1, 2, 2, 2, 1),
  'dorian': (2, 1, 2, 2, 2, 1, 2),
  'phrygian': (1, 2, 2, 2, 1, 2, 2),
  'lydian': (2, 2, 2, 1, 2, 2, 1),
  'mixolydian': (2, 2, 1, 2, 2, 1, 2),
  'aeolian': (2, 1, 2, 2, 1, 2, 2),
  'locrian': (1, 2, 2, 1, 2, 2, 2),
}

chromatic_scale_sharp = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
chromatic_scale_flat = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]

def key_engine(note, scale_name):
    '''
    Dynamically generates the notes in a scale based on the tonic
    '''
    scale = []
    scale_name = scale_name.lower()
    if note in chromatic_scale_sharp:
        start = chromatic_scale_sharp.index(note)
        full_scale = chromatic_scale_sharp[start:] + chromatic_scale_sharp[:start]
    elif note in chromatic_scale_flat:
        start = chromatic_scale_flat.index(note)
        full_scale = chromatic_scale_flat[start:] + chromatic_scale_flat[:start]
    # API for names
    if scale_name in NAMED_SCALES.keys():
        index = 0        
        for x in NAMED_SCALES[scale_name]:
            scale.append(full_scale[index])
            index = index + x
    else:
        print "Key not defined"
    return scale

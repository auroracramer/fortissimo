from overtonepy import *

def make_note(pitch, duration, tempo, instr):
    return {'instr': instr, 'pitch': pitch, 'duration': duration, 'tempo': tempo}

def test():
    notes = []
    notes.append(make_note("C5", 1, 180, "piano"))
    notes.append(make_note("D5", 1, 180, "piano"))
    notes.append(make_note("E5", 1, 180, "piano"))
    notes.append(make_note("F5", 1, 180, "piano"))
    notes.append(make_note("G5", 1, 180, "piano"))
    notes.append(make_note("A5", 1, 180, "piano"))
    notes.append(make_note("B5", 1, 180, "piano"))
    notes.append(make_note("C6", 1, 180, "piano"))
    
    playNotes(notes)

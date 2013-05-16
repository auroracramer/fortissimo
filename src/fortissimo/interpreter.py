#!/usr/bin/env python
import sys
from key_engine import key_engine
import parser_generator
import pprint
import overtonepy as ot
import java.lang.ClassLoader
import java.io.InputStreamReader
import java.io.BufferedReader
import java

class Phrase:
    '''
    An object representing a phrase, which is essentially a closure.
    Contains an environment and a list of args it can receive, along
    with the body of the Phrase.
    '''
    def __init__(self, name, body, args, env):
        self.name = name
        self.body = body
        self.args = args
        self.outer_env = env

def ReadFile(filepath):
    '''
    Gets a resource from the jar and returns the contents as a string.
    '''
    loader = java.lang.ClassLoader.getSystemClassLoader()
    stream = loader.getResourceAsStream(filepath)
    reader = java.io.BufferedReader(java.io.InputStreamReader(stream))
    string = ""
    line = reader.readLine()
    while line != None:
        string += line + "\n"
        line = reader.readLine()
    return string

class Interpreter:
    '''
    The interpreter that interprets our languages syntax.
    '''
    def __init__(self, recording=False):
        '''
        Set the global environment to be the default scale, octave,
        instrument, duration, tempo, and meter, and makes an empty notelist.
        '''
        self.global_env = {"_scale": ["C","D","E","F","G","A","B"], \
        "_octave": 4, "_currInstr": "Piano", "_duration": "q", \
        "_tempo": 120, "_meter": (4,4), "_notes": [{}], "__up__": None, "Piano": "Piano", "Guitar": "Guitar", "Bass": "Bass", "Overpad": "Overpad", "Ping": "Ping", "SawWave": "SawWave", "Synth": "Synth"}
        self.recording = recording
    
    def resetNotes(self):
        '''
        Deletes the notes in the environment. Used by the REPL loop to clear
        the list of notes so they don't get played again.
        '''
        self.global_env["_notes"] = [{}]

    def lookup(self, name, env):
        '''
        Lookup a binding in an environment.
        '''
        if not env:
            print "variable not found: ", name
            sys.exit(1)
        if name in env:
            return env[name]
        else:
            return self.lookup(name, env['__up__'])

    def evalStmt(self, stmts, env):
        '''
        Evaluates a list of statements in a given environment.
        '''
        def doCall(phrase, args):
            '''
            "Calls" a phrase. Essentially evaluates the phrase
            and returns its environment, typically to retreive the notelist.
            '''
            new_env = {}
            new_env['__up__'] = phrase.outer_env
            new_env["_notes"] = [{}]
            for i in range(len(args)):
                new_env[phrase.args[i]] = args[i]
            return self.evalStmt(phrase.body, new_env)
        def doCall2(phrase, args):
            '''
            "Calls" a phrase. This uses the language construct we have to
            specify the key, scale, instrument, etc to be used in the 
            Phrases.
            '''
            new_env = {}
            new_env['__up__'] = phrase.outer_env
            new_env["_notes"] = [{}]
            for arg in args:
                if arg[0] == "key":
                    new_env["_scale"] = key_engine(arg[1], arg[2])
                elif arg[0] == "instr":
                    new_env[arg[1]] = arg[2]
                else:
                    new_env["_" + arg[0]] = arg[1]
            return self.evalStmt(phrase.body, new_env)

        def update(name,env,val):
            '''
            Updates a binding in the environment to a given value.
            '''
            if not env:
                sys.exit(1)
            elif name in env:
                env[name] = val
            else:
                update(name,env['__up__'],val)
        # Evaluate the statements
        for s in stmts:
            if s[0] == 'phrase-def':
                # Phrase definition, binds a phrase to a name in
                # the environment
                env[s[1]] = Phrase(s[1], s[3], s[2], env)
            elif s[0] == "play":
                # Play each phrase sequentially
                for p in s[1]:
                    phrase = self.lookup(p, env)
                    val = doCall(phrase, phrase.args)
                    if self.recording == True:
                        env["_notes"] = val["_notes"]
                    else:
                        if env["_notes"][0] == {}:
                            env["_notes"] = val["_notes"]
                        else:
                            env["_notes"].extend(val["_notes"])
            elif s[0] == 'play-with': # only one phrase can follow after
                phrase = self.lookup(s[1], env)
                val = doCall2(phrase, s[2])
                if self.recording == True:
                    env["_notes"] = val["_notes"]
                else:
                    if env["_notes"][0] == {}:
                        env["_notes"] = val["_notes"]
                    else:
                        env["_notes"].extend(val["_notes"])
            elif s[0] == 'loop':
                # Loops a set of phrases
                self.evalStmt(s[1], env)
            elif s[0] == "asgn":
                # Assign a binding in the environment
                env[s[1]] = s[2]
            elif s[0] == "playing":
                # Sets the current instrument to be played 
                if s[1] in env.keys():
                    env["_currInstr"] = env[s[1]]
                else:
                    env["_currInstr"] = s[1]
            elif s[0] == "playing-in":
                # Sets the current instrument to be played and the
                # octave it will be played in
                if s[1] in env.keys():
                    env["_currInstr"] = env[s[1]]
                else:
                    env["_currInstr"] = s[1]
                if "_octave"in env.keys() and env["__up__"] is not None:
                    pass
                else:
                    env["_octave"] = s[2]
            elif s[0] == "key":
                # Declare the key to be played
                if "_scale" in env.keys() and env["__up__"] is not None:
                    print "passing"
                    pass
                else:
                    # Calls the key engine to dynamically generate the
                    # notes in the scale
                    env["_scale"] = key_engine(s[1], s[2])
            elif s[0] == "meter":
                # Declare the meter
                if "_meter" in env.keys() and env["__up__"] is not None:
                    pass
                else:
                    env["_meter"] = s[1]
            elif s[0] == "tempo":
                # Declare the tempo
                if "_tempo" in env.keys() and env["__up__"] is not None:
                    env["_tempo"] = s[1]
            elif s[0] == "duration":
                # Declare the default duration to be played
                if "_duration" in env.keys() and env["__up__"] is not None:
                    pass
                else:
                    env["_duration"] = s[1]
            elif s[0] == 'import-instr':
                # Imports an instrument that can be used in writing songs
                filename = s[1]
                ot.importInstrument(filename)
            elif s[0] == 'include':
                # Include phrases from another file
                filename = s[1]
                try:
                    # Parse and interpret the phrase to get the notelist and environment
                    fil = open(filename, "r")
                    text = fil.read()
                    fil.close()
                    grammar_file = ReadFile("fortissimo/fortissimo.grm")
                    parser = parser_generator.makeParser(grammar_parser.parse(cs164_grammar_file))
                    input_ast = parser.parse(text)
                    interpr = Intepreter(False)
                    new_env = interpr.evalStmt(input_ast, interpr.global_env)
                    self.global_env.update(new_env)
                except:
                    print "Could not include file '" + filename + "'."
            elif s[0] == "notes":
                # Adds notes to the environments notelist
                self.addNotesToQueue(s[1], env)
            else:
                raise SyntaxError("Illegal or Unimplemented AST node: " + str(s))        
        return env

    def addNotesToQueue(self, newNotes, env):
        '''
        Adds a list user defined notes to the notelist of the environment
        '''
        def noteMod(n, scale):
            '''
            Given a scale number, returns the 'mod', or the scale number
            of a note, disregarding the octave
            '''
            scaleLen = len(scale)
            if n < 0:
                # if negative, we have to add one, since we don't
                # use 0 as a scale number
                if (n+1) % scaleLen == 0:
                    return scaleLen
                else:
                    return (n+1) % scaleLen
            elif n % scaleLen == 0:
                return scaleLen
            else:
                return n % scaleLen

        def getOctave(n, octv, scale):
            '''
            Calculates the octave of a scale note, given an octave.
            '''
            note = scale[noteMod(n, scale) - 1]
            scaleLen = len(scale)

            def getBaseNote(note):
                '''
                Returns the letter of the note
                '''
                return note[0:1]

            def beforeC(curr, root):
                '''
                Returns if the note is after C (after the root note)
                '''
                letters = ["C", "D", "E", "F", "G", "A", "B"]
                return curr in letters[letters.index(root):]

            octave = octv

            if n < 0:
                octave = octave + (n+1)/scaleLen - 1 # remember that this uses int division
            else:
                octave = octave + (n-1)/scaleLen

            if not beforeC(getBaseNote(note), getBaseNote(scale[0])):
                octave = octave + 1

            return str(octave)

        def noteDuration(noteValue, meter):
            '''
            Calculates the duration in beats of a note based on the meter
            '''
            beatNote = meter[1]
            baseVals = {"w": 1, "h": 0.5, "q": 0.25, "e": 0.125, "s": 0.0625, "t": 0.03125}
            if len(noteValue) == 2:
                dotted = True
            else:
                dotted = False
            beats = baseVals[noteValue] * beatNote
            if dotted:
                beats = beats * 1.5
            return beats

        notesDict = self.lookup("_notes", env)[0] # Assume there is nothing after play stmt
        currInstr = self.lookup("_currInstr", env)
        if currInstr not in notesDict:
            notesDict[currInstr] = []
        notes = notesDict[currInstr]

        def makeNote(pitch, duration):
            '''
            Returns a dictionary for a note to be used in the Clojure interop
            '''
            return {'type': 'note', 'instr':self.lookup(currInstr, env),'pitch':pitch, 'duration':duration,'tempo': self.lookup("_tempo", env)}

        def makeChord(notes, duration):
            '''
            Makes a chord dictionary and returns it
            '''
            return {'type': 'chord', 'instr':self.lookup(currInstr, env),'notes':notes, 'duration':duration, 'tempo': self.lookup("_tempo", env)}
        def makeRest(duration):
            '''
            Makes a rest dictionary and returns it.
            '''
            return {'type': 'rest', 'duration': duration, 'tempo': self.lookup("_tempo", env)}

        def handleNote(note):
            '''
            Handles adding notes to the notelist
            '''
            if note[0] == "scale-note":
                '''
                Add a scale-note
                '''
                scale = self.lookup("_scale", env)
                pitch = scale[noteMod(note[1], scale) - 1] + getOctave(note[1], self.lookup("_octave", env), scale)

                duration = noteDuration(self.lookup("_duration", env), self.lookup("_meter", env))
                return makeNote(pitch, duration)
            
            if note[0] == "scale-duration-note":
                '''
                Add a dictionary scale note and a duration
                '''
                scale = self.lookup("_scale", env)
                pitch = scale[noteMod(note[1], scale) - 1] + getOctave(note[1], self.lookup("_octave", env), scale)
                duration = noteDuration(note[2], self.lookup("_meter", env))
                if note[3]:
                    # Dotted
                    duration = duration * 1.5
                
                return makeNote(pitch, duration)
                
            if note[0] == 'chord':
                '''
                Add a dictionary representing a chord
                '''
                notes = [handleNote(n) for n in note[1]]
                duration = reduce(lambda x,y: min(x, y['duration']), notes, 100)
                return makeChord(notes, duration)

            if note[0] == 'abs-note':
                '''
                Adds an absolute note
                '''
                pitch = note[1]
                duration = noteDuration(self.lookup("_duration", env), self.lookup("_meter", env))
                return makeNote(pitch, duration)

            if note[0] == 'abs-duration-note':
                '''
                Adds an absolute note with a duration
                '''
                pitch = note[1]
                duration = noteDuration(note[2], self.lookup("_meter", env))
                if note[3]:
                    # Dotted
                    duration = duration * 1.5
        
                return makeNote(pitch, duration)
            if note[0] == 'rest-note':
                '''
                Add a rest to be played
                '''
                duration = noteDuration(note[1], self.lookup("_meter", env))
                return makeRest(duration)

        for note in newNotes:
            notes.append(handleNote(note))

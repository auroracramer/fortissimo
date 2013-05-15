#!/usr/bin/env python
import sys
from key_engine import key_engine
import pprint
#from overtonepy import *

class Phrase:
    def __init__(self, name, body, args, env):
        self.name = name
        self.body = body
        self.args = args
        self.outer_env = env

class Interpreter:
    def __init__(self, recording=False):
        self.global_env = {"_scale": ["C","D","E","F","G","A","B"], \
        "_octave": 4, "_currInstr": "Piano", "_duration": "q", \
        "_tempo": 120, "_meter": (4,4), "_notes": [{}], "__up__": None}
        self.recording = recording

    def lookup(self, name, env):
        if not env:
            print "variable not found: ", name
            sys.exit(1)
        if name in env:
            return env[name]
        else:
            return self.lookup(name, env['__up__'])

    def evalStmt(self, stmts, env):
        def doCall(phrase, args):
            new_env = {}
            new_env['__up__'] = phrase.outer_env
            new_env["_notes"] = [{}]
            for i in range(len(args)):
                new_env[phrase.args[i]] = args[i]
            return self.evalStmt(phrase.body, new_env)
        def doCall2(phrase, args):
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
            if not env:
                sys.exit(1)
            elif name in env:
                env[name] = val
            else:
                update(name,env['__up__'],val)
        for s in stmts:
            if s[0] == 'phrase-def':
                env[s[1]] = Phrase(s[1], s[3], s[2], env)
            elif s[0] == "play":
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
                for p in s[1:]:                        
                    if s[1][0] == 'play-with':
                        phrase = self.lookup(s[1][1], env)
                        val = doCall2(phrase, s[1][2])
                        if self.recording == True:
                            env["_notes"] = val["_notes"]
                        else:
                            if env["_notes"][0] == {}:
                                env["_notes"] = val["_notes"]
                            else:
                                env["_notes"].extend(val["_notes"])
                    elif s[1][0] == 'play':
                        phrase = self.lookup(s[1][1], env)
                        val = doCall(phrase, [])
                        if self.recording == True:
                            env["_notes"] = val["_notes"]
                        else:
                            if env["_notes"][0] == {}:
                                env["_notes"] = val["_notes"]
                            else:
                                env["_notes"].extend(val["_notes"])
            elif s[0] == "asgn":
                env[s[1]] = s[2]
            elif s[0] == "playing":
                if s[1] in env.keys():
                    env["_currInstr"] = env[s[1]]
                else:
                    env["_currInstr"] = s[1]
            elif s[0] == "playing-in":
                if s[1] in env.keys():
                    env["_currInstr"] = env[s[1]]
                else:
                    env["_currInstr"] = s[1]
                if "_octave"in env.keys() and env["__up__"] is not None:
                    pass
                else:
                    env["_octave"] = s[2]
            elif s[0] == "key":
                if "_scale" in env.keys() and env["__up__"] is not None:
                    print "passing"
                    pass
                else:
                    env["_scale"] = key_engine(s[1], s[2])
            elif s[0] == "meter":
                if "_meter" in env.keys() and env["__up__"] is not None:
                    pass
                else:
                    env["_meter"] = s[1]
            elif s[0] == "notes":
                # print
                # print
                # print "ADDING NOTES TO :"
                #pprint.pprint(env)
                self.addNotesToQueue(s[1], env)
            else:
                raise SyntaxError("Illegal or Unimplemented AST node: " + str(s))        
        return env

    def addNotesToQueue(self, newNotes, env):
        def noteMod(n, scale):
            scaleLen = len(scale)
            if n < 0:
                if (n+1) % scaleLen == 0:
                    return scaleLen
                else:
                    return (n+1) % scaleLen
            elif n % scaleLen == 0:
                return scaleLen
            else:
                return n % scaleLen

        def getOctave(n, octv, scale):
            note = scale[noteMod(n, scale) - 1]
            scaleLen = len(scale)

            def getBaseNote(note):
                return note[0:1]

            def beforeC(curr, root):
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
        duration = self.lookup("_duration", env)
        for note in newNotes:
            if note[0] == "scale-note":
                scale = self.lookup("_scale", env)

                notes.append({'instr':self.lookup(currInstr, env),'pitch': scale[noteMod(note[1], scale) - 1] + getOctave(note[1], self.lookup("_octave", env), scale), 'duration':noteDuration(duration, self.lookup("_meter", env)),'tempo': self.lookup("_tempo", env)})
            if note[0] == "scale-duration-note":
                scale = self.lookup("_scale", env)
                notes.append({'instr':self.lookup(currInstr, env),'pitch': scale[noteMod(note[1], scale) - 1] + getOctave(note[1], self.lookup("_octave", env), scale), 'duration':noteDuration(note[2], self.lookup("_meter", env)), 'tempo':self.lookup("_tempo", env)})

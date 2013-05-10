#!/usr/bin/env python
import sys
from key_engine import key_engine

class Phrase:
    def __init__(self, name, body, args, env):
        self.name = name
        self.body = body
        self.args = args
        self.outer_env = env

def Exec(stmts):
    def lookup(name,env):
        if not env:
            print "variable not found: ", name
            sys.exit(1)
        if name in env:
            return env[name]
        else:
            return lookup(name, env['__up__'])
            
    def evalStmt(stmts,env):
        def doCall(phrase, args):
            new_env = {}
            new_env['__up__'] = phrase.outer_env
            new_env["_notes"] = [{}]
            for i in range(len(args)):
                new_env[phrase.args[i]] = args[i]
            return evalStmt(phrase.body, new_env)
            
        def update(name,env,val):
            if not env:
                #print "variable not found: ", name
                sys.exit(1)
            elif name in env:
                env[name] = val
            else:
                update(name,env['__up__'],val)
        for s in stmts:
            #print "current statement: ", s
            if s[0] == 'phrase-def':
                #print "defining phrase: ", s[1]
                env[s[1]] = Phrase(s[1], s[3], s[2], env)
            elif s[0] == "play":
                for p in s[1]:
                    phrase = lookup(p, env)
                    val = doCall(phrase, phrase.args)
                    #print "PRINTING ENVIRONMENT"
                    #pprint.pprint(env)
                    if env["_notes"][0] == {}:
                        env["_notes"] = val
                    else:
                        env["_notes"].extend(val)
            elif s[0] == "asgn":
                #print "assigning :", s[2], "to ", s[1]
                env[s[1]] = s[2]
            elif s[0] == "playing":
                #print "playing: ", s[1]
                env["_currInstr"] = s[1]
            elif s[0] == "playing-in":
                env["_currInstr"] = s[1]
                env["_octave"] = s[2]
            elif s[0] == "key":
                env["_scale"] = key_engine(s[1], s[2])
            elif s[0] == "meter":
                env["_meter"] = s[1]
            elif s[0] == "notes":
                #print "defining notelist: ", s[1]
                # call add notes to queue
                addNotesToQueue(s[1], env)
            else:
                raise SyntaxError("Illegal or Unimplemented AST node: " + str(s))
        return env["_notes"]
        
    def addNotesToQueue(newNotes, env):
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
        
        notesDict = lookup("_notes", env)[0] # Assume there is nothing after play stmt
        currInstr = lookup("_currInstr", env)
        if currInstr not in notesDict:
            notesDict[currInstr] = []
        notes = notesDict[currInstr]
        duration = lookup("_duration", env)
        for note in newNotes:
            if note[0] == "scale-note":
                scale = lookup("_scale", env)

                notes.append({'pitch': scale[noteMod(note[1], scale) - 1] + getOctave(note[1], lookup("_octave", env), scale), 'duration':noteDuration(duration, lookup("_meter", env)),'tempo': lookup("_tempo", env)})
            if note[0] == "scale-duration-note":
                scale = lookup("_scale", env)
                notes.append({'pitch': scale[noteMod(note[1], scale) - 1] + getOctave(note[1], lookup("_octave", env), scale), 'duration':noteDuration(note[2], lookup("_meter", env)), 'tempo':lookup("_tempo", env)})
                
    return evalStmt(stmts, {"_scale": ["C","D","E","F","G","A","B"], "_octave": 4, "_currInstr": "Piano", "_duration": "q", "_tempo": 120, "_meter": (4,4), "_notes": [{}], "__up__": None})

def Run(sast):
    #print "The AST is "
    #print ast
    #sast = Desugar(ast)
    #print "The simplified AST is "
    #print sast
    
    Exec(sast)

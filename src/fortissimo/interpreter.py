#!/usr/bin/env python
import sys
sast = [['asgn', 'Inst1', 'Piano'], ['phrase-def', 'CScale', [], [['playing', 'Inst1'], ['notes', [['scale-note', 1], ['scale-note', 2], ['scale-note', 3], ['scale-note', 4], ['scale-note', 5], ['scale-note', 6], ['scale-note', 7], ['scale-note', 8]]]]], ['play', 'CScale']]

"""
[
    ['asgn', 'Inst1', 'Piano'], 
    ['phrase-def', 'CScale', [], 
        [
            ['playing', 'Inst1'], 
            ['notes', 
                [
                    ['scale-note', 1], 
                    ['scale-note', 2], 
                    ['scale-note', 3], 
                    ['scale-note', 4], 
                    ['scale-note', 5],
                    ['scale-note', 6], 
                    ['scale-note', 7], 
                    ['scale-note', 8]
                ]
            ]
        ]
    ], 
    ['play', 'CScale']
]
"""

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
        def update(name,env,val):
            if not env:
                print "variable not found: ", name
                sys.exit(1)
            elif name in env:
                env[name] = val
            else:
                update(name,env['__up__'],val)
                
        for s in stmts:
            print "current statement: ", s
            if s[0] == 'phrase-def':
                print "defining phrase: ", s[1]
                env[s[1]] = Phrase(s[1], s[3], s[2], env)
            elif s[0] == "play": # 
                print "play ", s[1]
                # like a function call
                phrase = lookup(s[1], env)
                evalStmt(phrase.body, env)
            elif s[0] == "asgn":
                print "assigning :", s[2], "to ", s[1]
                env[s[1]] = s[2]
            elif s[0] == "playing":
                print "playing: ", s[1]
                env["_currInstr"] = s[1]
            elif s[0] == "notes":
                print "defining notelist: ", s[1]
                # call add notes to queue
                addNotesToQueue(s[1], env)
            else:
                raise SyntaxError("Illegal or Unimplemented AST node: " + str(s))
        print env["_notes"]
        
        
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
                octv = octv + (n+1)/scaleLen - 1 # remember that this uses int division
            else:
                octv = octv + (n-1)/scaleLen

            if not beforeC(getBaseNote(note), getBaseNote(scale[0])):
                octv = octv + 1

            return str(octv)

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
        
        notesDict = lookup("_notes", env)
        currInstr = lookup("_currInstr", env)
        if currInstr not in notesDict:
            notesDict[currInstr] = []
        notes = notesDict[currInstr]

        for note in newNotes:
            if note[0] == "scale-note":
                scale = lookup("_scale", env)
                notes.append((scale[noteMod(note[1], scale) - 1] + getOctave(note[1], lookup("_octave", env), scale), noteDuration(lookup("_duration", env), lookup("_meter", env)), lookup("_tempo", env)))
                
    return evalStmt(stmts, {"_scale": ["C","D","E","F","G","A","B"], "_octave": 4, "_currInstr": "Piano", "_duration": "q", "_tempo": 120, "_meter": (4,4), "_notes": dict(), "__up__": None})
     
def Run(sast):
    #print "The AST is "
    #print ast
    #sast = Desugar(ast)
    #print "The simplified AST is "
    #print sast
    
    Exec(sast)


Run(sast)

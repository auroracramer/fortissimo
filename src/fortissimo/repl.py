#!/usr/bin/env python
from key_engine import key_engine
import sys, getopt, parser_generator, grammar_parser, pprint

class Phrase:
    def __init__(self, name, body, args, env):
        self.name = name
        self.body = body
        self.args = args
        self.outer_env = env

class Interpreter:
    def __init__(self):
        self.global_env = {"_scale": ["C","D","E","F","G","A","B"], \
        "_octave": 4, "_currInstr": "Piano", "_duration": "q", \
        "_tempo": 120, "_meter": (4,4), "_notes": [{}], "__up__": None}

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
                    if env["_notes"][0] == {}:
                        env["_notes"] = val["_notes"]
                    else:
                        env["_notes"].extend(val["_notes"])

            elif s[0] == 'play-with': # only one phrase can follow after
                phrase = self.lookup(s[1], env)
                val = doCall2(phrase, s[2])
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

                notes.append({'instr':currInstr,'pitch': scale[noteMod(note[1], scale) - 1] + getOctave(note[1], self.lookup("_octave", env), scale), 'duration':noteDuration(duration, self.lookup("_meter", env)),'tempo': self.lookup("_tempo", env)})
            if note[0] == "scale-duration-note":
                scale = self.lookup("_scale", env)
                notes.append({'instr':currInstr,'pitch': scale[noteMod(note[1], scale) - 1] + getOctave(note[1], self.lookup("_octave", env), scale), 'duration':noteDuration(note[2], self.lookup("_meter", env)), 'tempo':self.lookup("_tempo", env)})

def rep_loop():
    interp = Interpreter()
    recognizer = parser_generator.makeParser(grammar_parser.parse(open('./fortissimo_repl.grm').read()))
    parser = parser_generator.makeParser(grammar_parser.parse(open('./fortissimo.grm').read()))
    line = ""
    depth, num_phrases = 0, 0
    phrase_list = [""]
    while(True):
        line = raw_input("> ")
        if line == "quit" or line == "exit":
            sys.exit()
        elif line == "save":
            f = open("saved_phrases", "w")
            for x in phrase_list:
                f.write(x + " ")
        elif line == "load":
            f = open("saved_phrases", "r")
            ast = parser.parse(f.read())
            interp.evalStmt(ast, interp.global_env)
        elif line == "print env":
            pprint.pprint(interp.global_env)
        elif line == "print phrases":
            if len(phrase_list) == 1:
                print "No phrases created"
            else:
                for x in phrase_list[:-1]:
                    print "Printing phrase: ",phrase_list.index(x) + 1
                    print x
        else:
            try:
                ast = recognizer.parse(line)
                #print ast
            except:
                print ": command not recognized"
                continue
            if depth == 0:
                if line[0:2] == "||":
                    print "Cannot end phrase here"
                    continue
                if line[0] == "|":
                    depth += 1
                    phrase_list[num_phrases] += line + " "
                else:
                    interp.evalStmt(ast, interp.global_env)
            else:
                if line[0:2] == "||" and depth == 1:
                    phrase_list[num_phrases] += line
                    phrase_ast = parser.parse(phrase_list[num_phrases])
                    #print phrase_ast
                    interp.evalStmt(phrase_ast, interp.global_env)
                    
                    depth -= 1
                    num_phrases += 1
                    phrase_list.append("")
                elif line[0:2] == "||":
                    phrase_list[num_phrases] += line + " "
                    depth -= 1
                elif line[0] == "|":
                    depth += 1
                    phrase_list[num_phrases] += line + " "
                else:
                    phrase_list[num_phrases] += line + " "

rep_loop()

#!/usr/bin/env python
from key_engine import key_engine
import sys, getopt, parser_generator, grammar_parser

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

    def lookup(self, name,env):
        print "lookup"

    def evalStmt(self, stmts,env):
        print "evalStmt"

    def addNotesToQueue(self, newNotes, env):
        print "addNotesToQueue"

def rep_loop():
    interp = Interpreter()
    cs164parser = parser_generator.makeParser(grammar_parser.parse(open('./fortissimo_repl.grm').read()))
    line = ""
    depth, num_phrases = 0, 0
    phrase_list = [""]
    while(True):
        line = raw_input("> ")
        if line == "quit" or line == "exit":
            sys.exit()
        elif line == "print":
            if len(phrase_list) == 1:
                print "No phrases created"
            else:
                for x in phrase_list[:-1]:
                    print "Printing phrase: ",phrase_list.index(x) + 1
                    print x
        else:
            try:
                ast = cs164parser.parse(line)
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
                    try:
                        interp.evalStmt(ast, interp.global_env)
                    except:
                        print "Could not execute statement"
                        continue
            else:
                if line[0:2] == "||" and depth < 1:
                    print "Cannot end phrase here"
                    continue
                if line[0:2] == "||" and depth == 1:
                    phrase_list[num_phrases] += line
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

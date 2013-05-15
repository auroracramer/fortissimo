#!/usr/bin/env python
from key_engine import key_engine
import java.lang.ClassLoader
import java.io.InputStreamReader
import java.io.BufferedReader
import java
import sys, getopt, interpreter, parser_generator, grammar_parser, pprint
#import overtonepy as overtone

def ReadFile(filepath):
    loader = java.lang.ClassLoader.getSystemClassLoader()
    stream = loader.getResourceAsStream(filepath)
    reader = java.io.BufferedReader(java.io.InputStreamReader(stream))
    string = ""
    line = reader.readLine()
    while line != None:
        string += line + "\n"
        line = reader.readLine()
    return string

def rep_loop():
    #overtone.startOvertone()
    recognizer_grm = ReadFile('fortissimo/fortissimo_repl.grm')
    parser_grm = ReadFile('fortissimo/fortissimo.grm')
    interp = interpreter.Interpreter()
    recognizer = parser_generator.makeParser(grammar_parser.parse(recognizer_grm))
    parser = parser_generator.makeParser(grammar_parser.parse(parser_grm))
    line = ""
    depth, num_phrases = 0, 0
    phrase_list = [""]
    while(True):
        line = raw_input("ff > ")
        try:
            ast = recognizer.parse(line)
            s = ast[0]
            #print ast
        except:
            print ": command not recognized"
            continue
        if s[0] == "quit" or s[0] == "exit":
            sys.exit()
        elif s[0] == "save": #REDO
            #with open("saved_phrases", "w") as f:
            #    for x in phrase_list:
            #        f.write(x + "\n")
            f = open("saved_phrases", "w")
            try:
                for x in phrase_list:
                    f.write(x + "\n")
            except:
                print "Could not save phrases."
        elif s[0] == "load": #REDO
            f = open("saved_phrases", "r")
            s = parser.parse(f.read())
            interp.evalStmt(ast, interp.global_env)
        elif line == "print env": #DEBUG ONLY REMOVE LATER
            pprint.pprint(interp.global_env)
        elif s[0] == "print": #REDO
            if len(phrase_list) == 1:
                print "No phrases created"
            else:
                for x in phrase_list[:-1]:
                    print "Printing phrase: ",phrase_list.index(x) + 1
                    print x
        elif s[0] == "phrase-end":
            if depth == 0:
                print "Cannot end phrase here"
            elif depth == 1:
                phrase_list[num_phrases] += line
                phrase_ast = parser.parse(phrase_list[num_phrases])
                interp.evalStmt(phrase_ast, interp.global_env)
                depth -= 1
                num_phrases += 1
                phrase_list.append("")
            else:
                phrase_list[num_phrases] += line + " "
                depth -= 1
        elif s[0] == "phrase-start":
            depth += 1
            phrase_list[num_phrases] += line + " "
        else:
            if depth == 0:
                interp.evalStmt(ast, interp.global_env)
            else:
                phrase_list[num_phrases] += line + " "
                
#rep_loop()

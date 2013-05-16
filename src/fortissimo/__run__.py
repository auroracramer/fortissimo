#!/usr/bin/env jython

import sys
import java.lang.ClassLoader
import java.io.InputStreamReader
import java.io.BufferedReader
from collections import defaultdict
import overtonepy as ot
import parser_generator, grammar_parser, interpreter
import pprint
import repl
import java

def ReadFile(filepath):
    """
    Loads a jar resource as string.
    """
    loader = java.lang.ClassLoader.getSystemClassLoader()
    stream = loader.getResourceAsStream(filepath)
    reader = java.io.BufferedReader(java.io.InputStreamReader(stream))
    string = ""
    line = reader.readLine()
    while line != None:
        string += line + "\n"
        line = reader.readLine()
    return string


      
def EvalNotes(phrases, output_filepath=None):
    '''
    Evaluates notes and plays them
    '''
    a = ot.startOvertone()

    if output_filepath:
        a = ot.startRecording(output_filepath)
    masterlist = defaultdict(list) 
    for phrase in phrases:
        # Add notes to the master notelist
        for instr in phrase.keys():
            masterlist[instr].extend(phrase[instr])
    # Get a common time
    commonTime = ot.getCommonTime()
    for index, notelist in enumerate(masterlist.values()):
        # Play the notes!
        try:
            if index == len(masterlist.values()) - 1:
                ot.playNotes(notelist, True, commonTime, True)
            else:
                ot.playNotes(notelist, False, commonTime, False)
        except Exception:
            pass

def ExecScript(cs164_input_file, outputfilepath = None):        
        cs164_grammar_file = ReadFile("fortissimo/fortissimo.grm") 
        cs164parser = parser_generator.makeParser(grammar_parser.parse(cs164_grammar_file))
        # Load program into the cs164interpreter
        input_ast = cs164parser.parse(open(cs164_input_file).read())
        # pprint.pprint(input_ast)
        if input_ast == None:
            print "Could not parse input file."
            exit(-1)
        interpretr = interpreter.Interpreter(False)
        evaled = interpretr.evalStmt(input_ast, interpretr.global_env)
        #evaled = interpreter.Exec(input_ast)
        EvalNotes(evaled["_notes"], outputfilepath)
#if __name__ == '__main__':
if True:

    welcome = """

        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @8iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii8@
        @0 0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@@@@@@@@@@@     '@@@@@@@     '@@@0 0@
        @0 0@@@@@@@@@@@@@@@@@@@@;   0@;  .@@@;   0@;  .@@0 0@
        @0 0@@@@@@@@@@@@@@@@@@L    0@;   @@L    0@;   @@@0 0@
        @0 0@@@@@@@@@@@@@@@@@;    f@@@@GB@1    ;@@@@G8@@@0 0@
        @0 0@@@@@@@@@@@@@@@@;    :@@@@@@@;    ,@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@;                          ;@@@@@@0 0@
        @0 0@@@@@@@@@@@@@@.     1@@@@@@@.    ;@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@@;    ,@@@@@@@;    ,@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@G     G@@@@@@G     G@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@,    ;@@@@@@@:    ;@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@;    ;@@@@@@@;    ;@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@8    ;@@@@@@@8    ;@@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@:   ;@@@@@@@@;   :@@@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@;   ;@@@@@@@@;   ;@@@@@@@@@@@@@@@@@0 0@
        @0 0@@;   G@@;   ;@1   G@@;   ;@@@@@@@@@@@@@@@@@@0 0@
        @0 0@@,       .;@@@:        ;@@@@@@@@@@@@@@@@@@@@0 0@
        @0 0@@@L:,,,,;@@@@@@L:,,,;@@@@@@@@@@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0 0@
        @0 0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0 0@
        @G iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii G@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 

             Fortissimo - Simplified Programmatic Music.
    
                        Powered by Overtone.
"""
    print welcome
    if len(sys.argv) > 3:
        print "Too many arguments specified"
        print "USAGE: python main.py <ff file name> | python main.py"
        sys.exit(1)
    elif len(sys.argv) == 1:
        print "Starting REPL Loop"
        repl.rep_loop()
    elif (len(sys.argv) == 2) or (len(sys.argv) == 3):
        if len(sys.argv) == 3:
            outfile = sys.argv[2]
        else:
            outfile = None
        ExecScript(sys.argv[1], outfile)



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
    a = ot.startOvertone()

    if output_filepath:
        a = ot.startRecording(output_filepath)
    masterlist = defaultdict(list) 
    for phrase in phrases:
        for instr in phrase.keys():
            masterlist[instr].extend(phrase[instr])
    commonTime = ot.getCommonTime()
    for index, notelist in enumerate(masterlist.values()):
        try:
            if index == len(masterlist.values()) - 1:
                ot.playNotes(notelist, True, commonTime, True)
            else:
                ot.playNotes(notelist, False, commonTime, False)
        except:
            pass

def ExecScript(cs164_input_file, outputfilepath = None):
        cs164_grammar_file = ReadFile("fortissimo/fortissimo.grm") 
        cs164parser = parser_generator.makeParser(grammar_parser.parse(cs164_grammar_file))
    
        # Load program into the cs164interpreter
        input_ast = cs164parser.parse(open(cs164_input_file).read())
        # pprint.pprint(input_ast)
        
        '''Uncomment when the interpreter object is made'''
        interpretr = interpreter.Interpreter(False)
        evaled = interpretr.evalStmt(input_ast, interpretr.global_env)

        #evaled = interpreter.Exec(input_ast)
        EvalNotes(evaled["_notes"], outputfilepath)
 
#if __name__ == '__main__':
if True:
    print "Fortissimo - Simplified Programmatic Music\nPowered by Overtone.\n\n"
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



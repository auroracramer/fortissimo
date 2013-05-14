#!/usr/bin/env python

import sys
import parser_generator, grammar_parser, interpreter
import pprint
import repl
if __name__ == '__main__':
    if len(sys.argv) > 3:
        print "Too many arguments specified"
        print "USAGE: python main.py <ff file name> | python main.py"
        sys.exit(1)
    elif len(sys.argv) == 1:
        print "Starting REPL Loop"
        repl.rep_loop()
    elif (len(sys.argv) == 2) or (len(sys.argv) == 3):
        cs164_grammar_file = './fortissimo.grm'
        cs164_input_file = sys.argv[1]
        outputfilepath = sys.argv[2]
        cs164parser = parser_generator.makeParser(grammar_parser.parse(open(cs164_grammar_file).read()))
    
    
        # Load program into the cs164interpreter
        input_ast = cs164parser.parse(open(cs164_input_file).read())
        # pprint.pprint(input_ast)
        a = interpreter.Exec(input_ast)
        pprint.pprint(a)
        

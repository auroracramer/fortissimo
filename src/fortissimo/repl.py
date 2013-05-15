#!/usr/bin/env python
from key_engine import key_engine
import java.lang.ClassLoader
import java.io.InputStreamReader
import java.io.BufferedReader
from collections import defaultdict
import java
import sys, getopt, interpreter, parser_generator, grammar_parser, pprint
import overtonepy as ot

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
                ot.playNotes(notelist, True, commonTime, False)
            else:
                ot.playNotes(notelist, False, commonTime, False)
        except:
            pass

def rep_loop():
    ot.startOvertone()
    recognizer_grm = ReadFile('fortissimo/fortissimo_repl.grm')
    parser_grm = ReadFile('fortissimo/fortissimo.grm')
    interp = interpreter.Interpreter()
    recognizer = parser_generator.makeParser(grammar_parser.parse(recognizer_grm))
    parser = parser_generator.makeParser(grammar_parser.parse(parser_grm))
    line = ""
    depth, num_phrases = 0, 0
    phrase_list = [""]
    prompt = "ff > "
    while(True):
        line = raw_input(prompt)
        if not line.strip():
            continue
        try:
            ast = recognizer.parse(line)
            s = ast[0]
        except Exception:
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
            try:
                interp.evalStmt(ast, interp.global_env)
            except Exception:
                print "Could not load."
                continue
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
                prompt = "ff > "
                phrase_list[num_phrases] += line
                phrase_ast = parser.parse(phrase_list[num_phrases])
                try:
                    interp.evalStmt(phrase_ast, interp.global_env)
                    depth -= 1
                    num_phrases += 1
                    phrase_list.append("")
                except Exception:
                    print "Could not define phrase."
                
            else:
                phrase_list[num_phrases] += line + " "
                depth -= 1
        elif s[0] == "phrase-start":
            prompt = "... "
            depth += 1
            phrase_list[num_phrases] += line + " "
        elif s[0] == "play" and depth == 0:
            try:
                play_env = interp.evalStmt(ast, interp.global_env)
                phrases = play_env["_notes"]
                interp.resetNotes()
                EvalNotes(phrases)
            except Exception:
                print "Could not play phrase."
            
        elif s[0] == "loop" and depth == 0:
            try:
                play_env = interp.evalStmt(ast, interp.global_env)
                phrases = play_env["_notes"]
                interp.resetNotes()
                EvalNotes(phrases)
            except Exception:
                print "Could not loop phrase."
        elif s[0] == "record" and depth == 0:
                ot.startRecording("./ff-out.wav")
        elif s[0] == "stop-record" and depth == 0:
                ot.stopRecording()
        elif s[0] == "record-phrase" and depth == 0:
            try:
                ot.startRecording()
                play_env = interp.evalStmt(ast, interp.global_env)
                phrases = play_env["_notes"]
                interp.resetNotes()
                EvalNotes(phrases, "./ff-out.wav")
            except Exception:
                print "Could not record phrase."
        elif s[0] == "help" and depth == 0:
            help_message = """

Fortissimo Usage
================

REPL-Only Commands:

record -- starts recording to ff-out.wav
stop recording -- stops recording
record <Phrase Name> -- starts recording a phrase
help -- print this help message
exit/quit -- quit the Fortissimo REPL

Language Usage
==============

Phrase Definition:

| <Phrase Name>
<Statements>
||



Statements:

Add a list of notes -- notes <list of notes>
Set the current scale -- key of <Letter> <Scale Name>
Set the current tempo -- tempo of <Tempo>
Set the current meter -- meter of <Notes per Measure>/<Note Getting Beat>
Set the current instrument playing -- playing <Instrument Name> (with <Optional List of Arguments>)
Play a phrase -- play <Phrase Name>
Play a phrase and set the phrases attributes -- play <Phrase Name> with
    -- Parameters
        -- key <Key>
        -- meter <Meter>
        -- octave <Octave>
        -- instrument <Instrument Name>
        -- tempo <Tempo>
Declare an instrument -- <Instrument Name> is <Instrument>



Note Types:

Scale Number Note
    -- Corresponds to number in scale
    -- Form of <Scale Number>(Optional Duration)
    -- e.g. 4q
Scientific Notation 
    -- The absolute name of a note
    -- Form of <Letter><Octave>(Optional Duration)
    -- e.g. c4w
Chords             
    -- Plays a group of notes concurrently
    -- Form of (<List of Notes>)
    -- e.g. (c4q e4q g4q)

Valid Durations:
    w -- whole
    h -- half
    q -- quarter
    e -- eighth
    s -- sixteenth
    t -- thirty-second
    

Available Instruments
    -- Piano
    -- Guitar
    -- SawWave
    -- Synth
    -- Overpad
    -- Bass
    -- Ping

Available Scales
    -- major
    -- minor
    -- melodicminor
    -- harmonicminor
    -- pentatonicmajor
    -- bluesmajor
    -- pentatonicminor
    -- bluesminor
    -- augmented
    -- diminished
    -- chromatic
    -- wholehalf
    -- halfwhole
    -- wholetone
    -- augmentedfifth
    -- japanese
    -- oriental
    -- ionian
    -- dorian
    -- phrygian
    -- lydian
    -- mixolydian
    -- aeolian
    -- locrian
            """

            print help_message
        else:
            if depth == 0:
                try:
                    interp.evalStmt(ast, interp.global_env)
                except Exception:
                    print "Could not execute statement."
            else:
                phrase_list[num_phrases] += line + " "
                
#rep_loop()

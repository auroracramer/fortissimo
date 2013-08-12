**FORTISSIMO**
*A programming language for writing programmatic music simply.*


[Project Proposal](https://docs.google.com/document/d/1jS_Cu1iDw-KZr1t3BK9n76HLKLK-Fn_DQCDGweRkw5w/edit?usp=sharing)

[Design Document](https://docs.google.com/document/d/1gbBn_fXmtp3yyG3Zmrfuj2geCGiNKF_wAaJlWRb9Vqc/edit?usp=sharing)

[Presentation Slides](https://docs.google.com/presentation/d/13mlyPJAdxTrLPu_hRg9c5fR0XI3muT7Rl7okjpwvQ5k/edit?usp=sharing)

[Poster Slides(ppt format)](https://docs.google.com/file/d/0B2qe6XvFiStTbThJeklPbVdVclk/edit?usp=sharing)

[Poster Slides(odf format)](https://docs.google.com/file/d/0B2qe6XvFiStTbThJeklPbVdVclk/edit?usp=sharing)

[Demo Screencast](http://www.youtube.com/watch?v=gMa7SlkcTrg&feature=youtu.be)

[Bonus Song (Tetris)](http://www.youtube.com/watch?v=9nNWx5gFwcA)


# Fortissimo Features #

## REPL-Only Commands: ##

* record -- starts recording to ff-out.wav
* stop recording -- stops recording
* record <Phrase Name> -- starts recording a phrase
* help -- print this help message
* exit/quit -- quit the Fortissimo REPL

# Language Usage #

## Phrase Definition: ##


```
#!

| <Phrase Name>
<Statements>
||
```

## Statements: ##

* Add a list of notes -- notes <list of notes>
* Set the current scale -- key of <Letter> <Scale Name>
* Set the current tempo -- tempo of <Tempo>
* Set the current meter -- meter of <Notes per Measure>/<Note Getting Beat>
* Set the current instrument playing -- playing <Instrument Name> (with <Optional List of Arguments>)
* Play a phrase -- play <Phrase Name>
* Play a phrase and set the phrases attributes -- play <Phrase Name> with
    * Parameters
        * key <Key>
        * meter <Meter>
        * octave <Octave>
        * instrument <Instrument Name>
        * tempo <Tempo>
* Declare an instrument -- <Instrument Name> is <Instrument>



# Note Types: #

## Scale Number Note ##
*      Corresponds to number in scale
*      Form of <Scale Number>(Optional Duration)
*      e.g. 4q

## Scientific Notation ## 
*      The absolute name of a note
*      Form of <Letter><Octave>(Optional Duration)
*      e.g. c4w

## Chords ##             
*      Plays a group of notes concurrently
*      Form of (<List of Notes>)
*      e.g. (c4q e4q g4q)

## Valid Durations: ##
*     w -- whole
*     h -- half
*     q -- quarter
*     e -- eighth
*     s -- sixteenth
*     t -- thirty-second
    

## Available Instruments ##
*      Piano
*      Guitar
*      SawWave
*      Synth
*      Overpad
*      Bass
*      Ping

## Available Scales ##
*      major
*      minor
*      melodicminor
*      harmonicminor
*      pentatonicmajor
*      bluesmajor
*      pentatonicminor
*      bluesminor
*      augmented
*      diminished
*      chromatic
*      wholehalf
*      halfwhole
*      wholetone
*      augmentedfifth
*      japanese
*      oriental
*      ionian
*      dorian
*      phrygian
*      lydian
*      mixolydian
*      aeolian
*      locrian


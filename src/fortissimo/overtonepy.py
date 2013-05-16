import pyclj

# Start Overtone
@pyclj.clojure
def startOvertone():
    '''
    (defn startOvertone [] 
        (use 'overtone.live) 
        (use 'fortissimo.instruments))
    '''

# Start recording audio output
@pyclj.clojure
def startRecording(filepath):
    '''
    (use 'overtone.live)
    (defn startRecording [filepath] 
        (overtone.live/recording-start filepath))
    '''

# import an instrument
@pyclj.clojure
def importInstrument(filepath):
    '''
    ;; For user defined instruments, must accept keyword parameters, the very least being freq and sustain.
    (defn importInstrument [filename]
        (load-file filename))
    '''

# Stop playing all sounds
@pyclj.clojure
def stopSound():
    '''
    (use 'overtone.live)
    (defn stopSound [] 
        (overtone.live/stop))
    '''

# Stop recording audio output
@pyclj.clojure
def stopRecording():
    '''
    (use 'overtone.live)
    (defn stopRecording [] 
        (overtone.live/recording-stop))
    '''

# Gets a time and returns it
@pyclj.clojure
def getCommonTime():
    '''
    (use 'overtone.live)
    (defn getCommonTime [] (+ ((metronome 120) 16)))
    '''

# Makes a placeholder metronome and returns it
@pyclj.clojure
def getMetronome():
    '''
    (use 'overtone.live)
    (defn getMetronome [] (metronome -1))
    '''

# Plays notes
@pyclj.clojure
def playNotes(notes, recording, commonTime, exit):
    '''
    (use 'overtone.live)
    (use 'fortissimo.instruments)
    (defn playNotes [notes recording commonTime exit]
        (loop [process (fn process [notes offset metro]
            (cond
                (empty? notes) (cond
                    recording (do 
                        (overtone.live/apply-at (metro (+ offset 8) ) (fn [] (overtone.live/recording-stop)))
                        (cond exit (apply-at (metro (+ offset 8)) (fn [] (System/exit 0))))))
                (= (get (first notes) "tempo") (overtone.live/metro-bpm metro)) (let [noote (first notes)]

                    (overtone.live/at (metro offset) ((get fortissimo.instruments/instrs (get noote "instr")) (get noote "pitch") (get noote "duration") (get noote "tempo"))) ; Add a library of instrs
                    (process (rest notes) (+ offset (get noote "duration")) metro))
                :else (overtone.live/apply-at (metro offset) (fn [] (let [noote (first notes) metro (overtone.live/metronome (get noote "tempo"))]

                    (overtone.live/at (metro (metro)) ((get fortissimo.instruments/instrs (get noote "instr")) (get noote "pitch") (get noote "duration") (get noote "tempo")))
                    (process (rest notes) (+ (metro) (get noote "duration")) metro))))))]
            (apply-at commonTime (process notes 0 (metronome -1)))))
    ''' 

#@pyclj.clojure    
#def playNotes(notes, recording, commonTime, exit):
def blah():




    '''
    (use 'overtone.live)
    (use 'fortissimo.instruments)
    (defn playNotes [notes recording commonTime exit]
        (loop [process (fn process [notes offset metro]
            (cond
                (empty? notes) (cond
                    recording (do 
                        (overtone.live/apply-at (metro (+ offset 8) ) (fn [] (overtone.live/recording-stop)))
                        (cond exit (apply-at (metro (+ offset 8)) (fn [] (System/exit 0))))))
                (= (get (first notes) "tempo") (overtone.live/metro-bpm metro)) (let [noote (first notes)]
                    ; Hacky quote speedup
                    (eval (get {"note" `(overtone.live/at (metro offset) ((get fortissimo.instruments/instrs (get ~noote "instr")) (get ~noote "pitch") (get ~noote "duration") (get ~noote "tempo"))), "chord" `(overtone.live/at (metro offset) (doseq [n (get ~noote "notes")] ((get fortissimo.instruments/instrs (get n "instr")) (get n "pitch") (get n "duration") (get n "tempo")))), "rest", '(do)} (get ~noote "type")))
                    (process (rest notes) (+ offset (get noote "duration")) metro))
                :else (overtone.live/at (metro offset) (let [noote (first notes) metro (overtone.live/metronome (get noote "tempo"))]
                    (eval (get {"note" `(overtone.live/at (metro offset) ((get fortissimo.instruments/instrs (get ~noote "instr")) (get ~noote "pitch") (get ~noote "duration") (get ~noote "tempo"))), "chord" `(overtone.live/at ((metronome (get ~noote "tempo")) offset) (doseq [n (get ~noote "notes")] ((get fortissimo.instruments/instrs (get n "instr")) (get n "pitch") (get n "duration") (get n "tempo")))), "rest" '(do)} (get ~noote "type")))
                    
                    (process (rest notes) (+ (metro) (get noote "duration")) metro)))))]
            (apply-at commonTime (process notes 0 (metronome (get (first notes) "tempo"))))))
    '''


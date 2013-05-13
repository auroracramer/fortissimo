import pyclj

@pyclj.clojure
def startOvertone():
    '''
    (defn startOvertone [] (use 'overtone.live) (use 'fortissimo.instruments))
    '''

@pyclj.clojure
def startRecording(filepath):
    '''
    (use 'overtone.live)
    (defn startRecording [filepath] 
        (overtone.live/recording-start filepath))
    '''

@pyclj.clojure
def importInstrument(filepath):
    '''
    ;; For user defined instruments, must accept keyword parameters, the very least being freq and sustain.
    (defn importInstrument [filename]
        (load-file filename))
    '''

@pyclj.clojure
def stopSound():
    '''
    (use 'overtone.live)
    (defn stopSound [] 
        (overtone.live/stop))
    '''

@pyclj.clojure
def stopRecording():
    '''
    (use 'overtone.live)
    (defn stopRecording [] 
        (overtone.live/recording-stop))
    '''

@pyclj.clojure
def playNotes(notes):
    '''
    (use 'overtone.live)
    (use 'fortissimo.instruments)
    (defn playNotes [notes]
        (loop [process (fn process [notes offset metro]
            (cond
                (empty? notes) (fn [] (do))
                (= (get (first notes) "tempo") (overtone.live/metro-bpm metro)) (let [noote (first notes)]

                    (overtone.live/at (metro offset) ((get fortissimo.instruments/instrs (get noote "instr")) (get noote "pitch") (get noote "duration") (get noote "tempo"))) ; Add a library of instrs
                    (process (rest notes) (+ offset (get noote "duration")) metro))
                :else (overtone.live/apply-at (metro offset) (fn [] (let [noote (first notes) metro (overtone.live/metronome (get noote "tempo"))]

                    (overtone.live/at (metro (metro)) ((get fortissimo.instruments/instrs (get noote "instr")) (get noote "pitch") (get noote "duration") (get noote "tempo")))
                    (process (rest notes) (+ (metro) (get noote "duration")) metro))))))]
            (process notes 0 (metronome -1))))
    '''


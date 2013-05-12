import pyclj

@pyclj.clojure
def startOvertone():
    '''
    (use 'overtone.live)
    (use 'fortissimo.instruments)
    '''

@pyclj.clojure
def startRecording(filepath):
    '''
    (defn startRecording [filepath] (recording-start filepath))
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
    (defn stopSound [] (stop))
    '''

@pyclj.clojure
def stopRecording():
    '''
    (defn stopRecording [] (recording-stop))
    '''

@pyclj.clojure
def playNotes(notes):
    '''
    (defn playNotes [notes]
        (loop [process (fn process [notes offset metro]
            (cond
                (empty? notes) (fn [] (do))
                (= ((first notes) "tempo") (metro-bpm metro)) (let [noote (first notes)]
                    (at (metro offset) ((instrs (noote "instr")) (noote "pitch") (noote "duration") (noote "tempo"))) ; Add a library of instrs
                    (process (rest notes) (+ offset (noote "duration")) metro))
                :else (apply-at (metro offset) (fn [] (let [noote (first notes) metro (metronome (noote "tempo"))]
                    
                    (at (metro (metro)) ((instrs (noote "instr")) (noote "pitch") (noote "duration") (noote "tempo")))
                    (process (rest notes) (+ (metro) (noote "duration")) metro))))))]
            (process notes 0 (metronome -1))))
    '''


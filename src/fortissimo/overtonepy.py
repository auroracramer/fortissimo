import pyclj

@pyclj.clojure
def startOvertone():
    '''
    (defn startOvertone [] 
        (use 'overtone.live) 
        (use 'fortissimo.instruments))
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
def getCommonTime():
    '''
    (use 'overtone.live)
    (defn getCommonTime [] (+ (now) 1000000000))
    '''

@pyclj.clojure
def getMetronome():
    '''
    (use 'overtone.live)
    (defn getMetronome [] (metronome -1))
    '''

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
                    (cond
                        (= (get noote "type") "note") (overtone.live/at (metro offset) ((get fortissimo.instruments/instrs (get noote "instr")) (get noote "pitch") (get noote "duration") (get noote "tempo")))
                        (= (get noote "type") "chord") (overtone.live/at ((metronome (get noote "tempo")) offset) (doseq [n (get noote "notes")] 
                             ((get fortissimo.instruments/instrs (get n "instr")) (get n "pitch") (get n "duration") (get n "tempo"))))
                        (= (get noote "type") "rest") (do))
                    (process (rest notes) (+ offset (get noote "duration")) metro))
                :else (overtone.live/at (metro offset) (let [noote (first notes) metro (overtone.live/metronome (get noote "tempo"))]
                    (cond
                        (= (get noote "type") "note") (overtone.live/at (metro offset) ((get fortissimo.instruments/instrs (get noote "instr")) (get noote "pitch") (get noote "duration") (get noote "tempo")))
                        (= (get noote "type") "chord") (overtone.live/at ((metronome (get noote "tempo")) offset) (doseq [n (get noote "notes")] 
                            ((get fortissimo.instruments/instrs (get n "instr")) (get n "pitch") (get n "duration") (get n "tempo"))))
                        (= (get noote "type") "rest") (do))

                    
                    (process (rest notes) (+ (metro) (get noote "duration")) metro)))))]
            (apply-at commonTime (process notes 0 (metronome (get (first notes) "tempo"))))))
    '''


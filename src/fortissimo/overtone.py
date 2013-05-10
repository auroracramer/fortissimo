import pyclj

@pyclj.clojure
def startOvertone():
    '''
    (use 'overtone.live)
    '''

@pyclj.clojure
def playNotes(notes):
    '''
    (defn playNotes [notes]
        (let [process (fn [notes offset metro]
            (cond
                (empty? notes) (fn [] (do))
                (= (notes "tempo") (metro-bpm metro)) (let [note (first notes)]
                    (at (metro offset) ((instrs (load-string (note "instr"))) (note "pitch") (note "duration"))) ; Add a library of instrs
                    (process (rest notes) (+ offset (note "duration")) metro))
                :else (apply-at (metro offset) (let [note (first notes)]
                    (def metro (metronome (note "tempo")))
                    (at (metro) ((instrs (load-string (note "instr"))) (note "pitch") (note "duration")))
                    (process (rest notes) (+ offset (note "duration")) metro)))))]
            (process notes 0 (metronome 120))))
    '''

